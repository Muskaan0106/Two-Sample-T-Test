from flask import Flask, request, jsonify, send_from_directory
import numpy as np
from scipy import stats
from statistics import stdev
from scipy.stats import t
import os

app = Flask(__name__, static_folder=".")

def two_sample(a, b, alternative):
    n1 = len(a)
    n2 = len(b)
    xbar1 = np.mean(a)
    xbar2 = np.mean(b)
    sd1 = stdev(a)
    sd2 = stdev(b)
    alpha = 0.05 / 2
    df = n1 + n2 - 2
    se = np.sqrt((sd1**2) / n1 + (sd2**2) / n2)

    t_table_pos = t.ppf(1 - alpha, df)
    t_table_neg = t.ppf(alpha, df)
    tcal = ((xbar1 - xbar2) - 0) / se

    if alternative == "two-sided":
        p_value = 2 * (1 - t.cdf(abs(tcal), df))
    elif alternative == "left":
        p_value = t.cdf(tcal, df)
    elif alternative == "right":
        p_value = 1 - t.cdf(tcal, df)
    else:
        p_value = None

    scipy_result = stats.ttest_ind(a, b, equal_var=False, alternative="two-sided")

    conclusion = "Reject the Null Hypothesis" if p_value < 0.05 else "Fail to Reject the Null Hypothesis"

    return {
        "n1": n1,
        "n2": n2,
        "mean1": round(xbar1, 6),
        "mean2": round(xbar2, 6),
        "sd1": round(sd1, 6),
        "sd2": round(sd2, 6),
        "se": round(se, 6),
        "df": df,
        "t_critical_pos": round(t_table_pos, 6),
        "t_critical_neg": round(t_table_neg, 6),
        "t_calculated": round(tcal, 6),
        "p_value": round(p_value, 6),
        "scipy_t_stat": round(scipy_result.statistic, 6),
        "scipy_p_value": round(scipy_result.pvalue, 6),
        "conclusion": conclusion
    }


@app.route("/")
def index():
    return send_from_directory(".", "index.html")


@app.route("/compute", methods=["POST"])
def compute():
    try:
        data = request.get_json()
        sample_a = [float(x) for x in data["sample_a"].split(",") if x.strip()]
        sample_b = [float(x) for x in data["sample_b"].split(",") if x.strip()]
        alternative = data.get("alternative", "two-sided")

        if len(sample_a) < 2 or len(sample_b) < 2:
            return jsonify({"error": "Each sample must have at least 2 values."}), 400

        result = two_sample(sample_a, sample_b, alternative)
        return jsonify(result)
    except ValueError as e:
        return jsonify({"error": f"Invalid input: {str(e)}"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
