# LLM x VLSI: Automated Verilog Design and Simulation with Gemini

This repository showcases a simple yet powerful tool that leverages Large Language Models (LLMs) like Gemini 2.0 to automatically generate Verilog code for digital circuits, simulate them using Icarus Verilog, and summarize the simulation results using the LLM itself.

## YouTube Channel: [@wt_bug](https://www.youtube.com/@wt_bug)

## Overview

This project demonstrates how LLMs can be integrated into the VLSI design workflow to accelerate development and testing. The workflow involves the following steps:

1.  **Prompt Engineering:** A prompt is used to instruct the LLM to generate Verilog code for a specific digital circuit (DUT) and its corresponding testbench.
2.  **Code Generation:** The LLM generates the Verilog code based on the prompt.
3.  **Post Processing:** Remove any language tags by LLM
4.  **Simulation:**  Icarus Verilog is used to compile and simulate the generated Verilog code.
5.  **Result Logging:**  Compilation & Simulation results output, errors and summary is saved to result.txt
6.  **Summarization:** The output logs from the simulation are passed back to the LLM to generate a concise summary of the simulation results.  This is useful for quickly understanding the behavior of the design.

## Requirements

*   **Python 3.6+**
*   **Google Generative AI package:** `pip install google-generativeai`
*   **Icarus Verilog:** (Must be installed and accessible in your system's PATH)
*   **Gemini API Key:** You need a Gemini API key from Google AI Studio. Create an API key at [https://aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey).
    **Important:** Replace `"YOUR_API_KEY"` in the `llmXvlsi.py` file with your actual API key.

## Usage

1.  **Clone the Repository:**

    ```bash
    git clone https://github.com/rpjayaraman/LLMxVLSI.git
    cd LLMxVLSI
    ```

2.  **Install Dependencies:**

    ```bash
    pip install google-generativeai
    ```

3.  **Set your Gemini API key by updating YOUR_API_KEY**

4.  **Run the Script:**

    ```bash
    python3 llmXvlsi.py
    ```

    This script will:

    *   Generate Verilog code.
    *   Save it to a file (e.g., `d_flipflop.v`).
    *   Compile and simulate the code using Icarus Verilog.
    *   Generate a simulation dump file (`d_flipflop.out`).
    *   Summarize the log using Gemini (Summarized result in the simulation_results.txt).

## Project Files

*   `llmXvlsi.py`:  The main Python script that drives the automated workflow.
*   `simulation_results.txt`: Combined results file


