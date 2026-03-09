from flask import Flask, render_template, request, jsonify
from halix_cpu import HalixCPU
from ai_helper import explain_instruction

app = Flask(__name__, template_folder="templates", static_folder="static")

cpu = HalixCPU()

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/load", methods=["POST"])
def load_program():

    data = request.get_json()

    code = data["code"]

    cpu.load_program(code)

    return jsonify({"status":"loaded"})


@app.route("/step", methods=["GET"])
def step():

    print("STEP CALLED")

    instr = cpu.step()

    explanation = explain_instruction(instr)

    return jsonify({
        "instruction": instr,
        "explanation": explanation,
        "registers": cpu.registers,
        "pc": cpu.pc
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9600, debug=True)
