'''
MIT License

Copyright (c) 2025 Jayaraman R P

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

'''
import google.generativeai as genai
import subprocess

# Configure Google Generative AI
genai.configure(api_key="YOUR_API_KEP")  # Replace with your actual API key
model = genai.GenerativeModel("gemini-2.0-flash")

def generate_and_run(prompt):
    """Generates Verilog code, simulates it, logs the output, and summarizes the log."""

    filename = "d_flipflop.v"

    # 1. Generate Verilog code
    try:
        response = model.generate_content(prompt)
        verilog_code = response.text.replace("```verilog", "").replace("```", "")
        #print("Generated Verilog code:\n", verilog_code)
        print("Generated Verilog code\n")
    except Exception as e:
        print(f"Error during code generation:\n{e}")
        return

    # 2. Save code to file
    try:
        with open(filename, "w") as f:
            f.write(verilog_code)
        print(f"Verilog code saved to {filename}")
    except Exception as e:
        print(f"Error saving code to file:\n{e}")
        return

    # 3. Compile and simulate the code
    try:
        compile_command = ["iverilog", "-o", "d_flipflop.out", filename]
        compile_result = subprocess.run(compile_command, capture_output=True, text=True, check=True)

        simulate_command = ["vvp", "d_flipflop.out"]
        simulate_result = subprocess.run(simulate_command, capture_output=True, text=True, check=True)

        # 4. Log the results and summarize
        log_filename = "simulation_results.txt"  # Combined results file
        try:
            with open(log_filename, "w") as log_file:
                log_file.write("Generated Verilog Code:\n")
                log_file.write(verilog_code)
                log_file.write("\n\nCompilation Output:\n")
                log_file.write(compile_result.stdout)
                log_file.write("\n\nCompilation Errors:\n")
                log_file.write(compile_result.stderr)
                log_file.write("\n\nSimulation Output:\n")
                log_file.write(simulate_result.stdout)
                log_file.write("\n\nSimulation Errors:\n")
                log_file.write(simulate_result.stderr)

                # 5. Summarize the log with GenAI
                try:
                    summary_prompt = f"Summarize the following Icarus Verilog simulation results:\nCompilation Output:\n{compile_result.stdout}\nCompilation Errors:\n{compile_result.stderr}\nSimulation Output:\n{simulate_result.stdout}\nSimulation Errors:\n{simulate_result.stderr}"
                    summary = model.generate_content(summary_prompt).text
                    log_file.write("\n\nSimulation Summary:\n")
                    log_file.write(summary)
                    print("\nSimulation Summary:\n", summary)

                except Exception as e:
                    print(f"Error during log summarization:\n{e}")

            print(f"Simulation results (including summary) saved to {log_filename}")

        except Exception as e:
            print(f"Error during logging:\n{e}")

    except subprocess.CalledProcessError as e:
        print(f"Error during compilation or simulation:\n{e}\nStdout:\n{e.stdout}\nStderr:\n{e.stderr}")
    except FileNotFoundError as e:
        print(f"Error: Icarus Verilog or VVP not found. Ensure they are installed and in your PATH.\n{e}")
    except Exception as e:
        print(f"An unexpected error occurred during simulation:\n{e}")

# Main 
prompt = "Create a simple d flip-flop design and testbench in Verilog without explanation. Include a $finish statement."
generate_and_run(prompt)
