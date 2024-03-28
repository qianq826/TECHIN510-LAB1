from pathlib import Path

import streamlit as st
from PIL import Image
#import matplotlib.pyplot as plt
import numpy as np

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir /"assets"/"Sebastian_Resume.pdf"
profile_pic = current_dir / "assets" / "Me.jpg"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Qiyuan(Sebastian) Qian"
PAGE_ICON = ":wave:"
NAME = "Qiyuan(Sebastian) Qian"
DESCRIPTION = """
Currently a Master’s student in MSTI at the University of Washington with a field studying technology-focused and user-centered design. Completed my BFA in Product Design from Parsons. I possess a passion for user-centered design and technology, complemented by a strong foundation in fine arts and art history. My academic and practical experiences converge on designing innovative solutions for environmental sustainability and social inclusion.
"""
EMAIL = "qianq826@uw.edu"
SOCIAL_MEDIA = {
    "💻 LinkedIn": "https://www.linkedin.com/in/qiyuan-qian-a919921b6/",
    "📊 GitHub": "https://github.com/qianq826",
}
PROJECTS = {
    "📁Check out my projects HERE": "http://sebstudio414.cn",

   
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")



# --- SKILLS ---
st.write('\n')
st.subheader("Skills")
st.write(
    """
- 📊 UIUX: Figma, User Research
- 📚 3D Modeling: Fusion360, Rhino, Keyshot
- 👩‍💻 Programming: Python
- 🗄️ Other Skills: Indesgin, Electrical Engineering
"""
)



# --- Education ---
st.write('\n')
st.subheader("Education")
st.write("---")

# --- Edu 1
st.write("📚", "**University of Washington | MSTI (Technology of Innovation)**")
st.write("09/2023 -present ")
st.write(
    """
- ► Major Computer Science in Technology of Innovation
- ► Mutidisciplinaries in Engineering, Desgin, and Business
- ► Skill tool kits: UI&UX, Coding, Design, and Business
"""
)

# --- Edu 2
st.write('\n')
st.write("📚", "**Parsons, The New school of Design  | BFA Product Design**")
st.write("08/2019 - 05/2023")
st.write(
    """
- ► BFA in Product Design
- ► Salt Shed Public Library Design, NY: Feb 2022 - May 2022
- ► Parsons X Drawdown Curator at New York Now: Aug 2022 - Nov 2022
- ► Skill tool kits: 3D Modeling, Sketch, 3D Printing
"""
)




# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Product Design Intern  | Shanghai Jahwa**")
st.write("Jul 2021 - Aug 2021 ")
st.write(
    """
- ► Rapid sketching skills: used Procreate to show effective visual packaging solutions for the SixGod travel set product.
- ► Fusion360 & Rhino: specialized in utilizing 3D software to craft innovative cosmetic packaging solutions. 
- ► Design Communication: necessitated seamless communication with various teams, including graphics, engineering, and manufacturing, to ensure successful product launching. 
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Product Manager Intern | Unilever**")
st.write("May 2023 - Jul 2023")
st.write(
    """
- ► Product Manager Assistance: collaborated closely with the product management team to evaluate and select innovative design proposals for the upcoming Clear Men’s Shampoo Set. 
- ► Keyshot Rendering: detailed renderings and finishing concepts; Rendered refined product designs used for post-strategic discussions on product material finishing, label design, and package layout.
- ► Conduct Meetinsg and Discussions: communicate effectively to ensure design decisions were aligned with both user needs and business goals with the design team and market team. 
"""
)

# --- JOB 3
st.write('\n')
st.write("🚧", "**Market and Design Intern | ColorWorks, Avient**")
st.write("Jul 2023 - Sep 2023")
st.write(
    """
- ► Market Research: conduct online research and offline research for Clear Men’s Shampoo products in retail space from small-scale to large-scale business.
- ► User Research: conduct secondary user research and interviews to provide specific personas of target consumers for the Shampoo brand, Clear. 
- ► Color Analysis and Proposal: utilizing data analysis from field insights and creating color palates, provide innovative color design proposals that match Clear’s brand strategy and market trends. 

"""
)