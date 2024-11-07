"""
Main page for the OpenMS Template App.

This module sets up and displays the Streamlit app for the OpenMS Template App.
It includes:
- Setting the app title.
- Displaying a description.
- Providing a download button for the Windows version of the app.

Usage:
Run this script to launch the OpenMS Template App.

Note:
- If run in local mode, the CAPTCHA control is not applied.
- If not in local mode, CAPTCHA control is applied to verify the user.

Returns:
    None
"""

from pathlib import Path
import streamlit as st

from src.common.common import page_setup

page_setup(page="main")

st.title("NASEWEIS App")
st.info("""
This repository contains a simple NucleicAcidSearchEngine workflow in a web application using the **streamlit** framework. It includes solutions for handling user data and parameters in workspaces as well as deployment with docker-compose.
""")
st.subheader("Features")
st.markdown("""
- Workspaces for user data with unique shareable IDs
- Persistent parameters and input files within a workspace
- Captcha control
- Packaged executables for Windows
- framework for workflows with OpenMS TOPP tools
- Deployment [with docker-compose](https://github.com/OpenMS/streamlit-deployment)
""")
st.subheader("Quick Start")
st.markdown("""
                    1. Select "NASEWEIS" in the sidebar.
                                
                    2. Load the example mzML (raw data) by clicking the "Load Example Data" button under the "MS data" tab of "📁File Upload".
                
                    3. Load the example RNA sequence file by clicking the "Load Example Data" button under the "Nucleotide sequences" tab of "📁File Upload".
                
                    4. Go to the ⚙️ Configure tab and Select the example files in the "mzML-files" and "fasta-files" entries.
                
                    5. Click on the 🚀 **Run** tab and hit "Run" and click "Start Workflow"
                
                    6. Go to the📊 **Results** tab and scroll through the results table. You can also download the table, a mzTab formatted version of the results, and a TOPPView idXML set of results.
                """)
if Path("OpenMS-App.zip").exists():
    st.markdown("""
Download the latest version for Windows here by clicking the button below.
""")
    with open("OpenMS-App.zip", "rb") as file:
        st.download_button(
            label="Download for Windows",
            data=file,
            file_name="OpenMS-App.zip",
            mime="archive/zip",
            type="primary",
        )
    st.markdown("""
Extract the zip file and run the batch script (run_app.bat) file to launch the app. Since every dependency is compressed and packacked the app will take a while to launch (up to one minute).
""")