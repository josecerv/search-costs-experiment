#!/usr/bin/env python3
import pandas as pd
import time
import json
import requests

# API key should be set as environment variable
import os
API_KEY = os.environ.get("PERPLEXITY_API_KEY")
if not API_KEY:
    raise ValueError("PERPLEXITY_API_KEY environment variable is not set")

def search_faculty_url_perplexity(university, department):
    """
    Searches for the direct faculty directory URL using the Perplexity API chat completions endpoint.
    Uses model "sonar" with fine tuned parameters for high accuracy and less randomness.
    Returns the first citation (URL) if available, or an empty string.
    """
    query = f"Return the direct link to the faculty directory page for {university} {department}."
    print(f"Perplexity API query: {query}")

    api_url = "https://api.perplexity.ai/chat/completions"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "sonar",
        "messages": [
            {"role": "system", "content": "Be precise and concise."},
            {"role": "user", "content": query}
        ],
        "max_tokens": 150,
        "temperature": 0.2,
        "top_p": 0.9,
        "top_k": 0,
        "stream": False,
        "presence_penalty": 0,
        "frequency_penalty": 1,
        "return_images": False,
        "return_related_questions": False,
        "search_recency_filter": ""
    }

    try:
        response = requests.post(api_url, headers=headers, data=json.dumps(payload))
        response.raise_for_status()
        result = response.json()
        # Extract citations and return the first one if available.
        citations = result.get("citations", [])
        if citations:
            url = citations[0]
            print(f"Found URL: {url}")
            return url
        else:
            print("No citations found in response.")
            return ""
    except Exception as e:
        print(f"Error during Perplexity API call: {e}")
        return ""

def main():
    # Pre-defined mapping for (University, Department) pairs.
    faculty_url_mapping = {
        ("Baylor University", "Mathematics"): "https://math.artsandsciences.baylor.edu/people/faculty",
        ("Colorado School of Mines", "Physics"): "https://physics.mines.edu/faculty-and-staff/",
        ("University of Houston", "Computer Science"): "https://uh.edu/nsm/computer-science/people/faculty/",
        ("University of Utah", "Mathematics"): "http://www.math.utah.edu/directory/faculty.php",
        ("Johns Hopkins University", "Mechanical Engineering"): "https://me.jhu.edu/faculty/",
        ("Dartmouth College", "Mathematics"): "https://math.dartmouth.edu/people/people-select.php?list=permanent",
        ("Kent State University", "Mathematics"): "https://www.kent.edu/math/tenure-track-faculty",
        ("Rice University", "Physics"): "https://physics.rice.edu/core-faculty",
        ("Columbia University", "Physics"): "https://www.physics.columbia.edu/content/faculty",
        ("University of South Florida", "Mechanical Engineering"): "https://www.usf.edu/engineering/me/people/",
        ("University of Virginia", "Mathematics"): "https://math.virginia.edu/faculty/",
        ("University of Colorado Boulder", "Mathematics"): "https://www.colorado.edu/math/people-mathematics-appointment",
        ("University of Iowa", "Computer Science"): "https://cs.uiowa.edu/people/faculty",
        ("University of Pittsburgh", "Computer Science"): "https://www.sci.pitt.edu/people/department-computer-science-faculty",
        ("Kent State University", "Physics"): "https://www.kent.edu/physics/faculty-and-staff",
        ("University of Washington", "Physics"): "https://phys.washington.edu/people/faculty",
        ("New York University", "Mathematics"): "https://math.nyu.edu/dynamic/people/faculty/",
        ("Carnegie Mellon University", "Mathematics"): "https://www.cmu.edu/math/people/faculty/",
        ("University of Michigan", "Physics"): "https://lsa.umich.edu/physics/people/faculty.directory.html",
        ("University of Louisiana at Lafayette", "Mathematics"): "https://math.louisiana.edu/",
        ("Texas A&M University", "Mathematics"): "https://www.math.tamu.edu/people/",
        ("University at Albany, SUNY", "Mathematics"): "https://www.albany.edu/math/",
        ("Auburn University", "Computer Science"): "https://eng.auburn.edu/csse/people/",
        ("North Carolina State University", "Mathematics"): "https://math.sciences.ncsu.edu/group/faculty/",
        ("Rensselaer Polytechnic Institute", "Computer Science"): "https://faculty.rpi.edu/departments/computer-science",
        ("Tufts University", "Mathematics"): "https://math.tufts.edu/people/faculty",
        ("University of Cincinnati", "Mathematics"): "https://www.artsci.uc.edu/departments/math/fac-staff.html",
        ("Michigan State University", "Computer Science"): "https://at3.cse.msu.edu/People/Faculty_Staff/",
        ("University of Pennsylvania", "Mathematics"): "https://www.math.upenn.edu/people/standing-faculty",
        ("Arizona State University", "Chemistry"): "https://sms.asu.edu/Research/Faculty",
        ("Georgia Institute of Technology", "Computer Science"): "https://www.cc.gatech.edu/people",
        ("Graduate Center, CUNY", "Mathematics"): "https://www.gc.cuny.edu/mathematics/faculty",
        ("University of Missouri", "Chemistry"): "https://chemistry.missouri.edu/research-areas",
        ("Virginia Tech", "Physics"): "https://www.phys.vt.edu/About/people/Faculty.html",
        ("University of Hawaii at Manoa", "Physics"): "https://www.phys.hawaii.edu/faculty/",
        ("University of Michigan", "Computer Science"): "https://cse.engin.umich.edu/people/faculty/",
        ("University of Minnesota", "Mathematics"): "https://cse.umn.edu/math/faculty",
        ("Princeton University", "Mathematics"): "https://www.pacm.princeton.edu/directory/all-faculty",
        ("Drexel University", "Mathematics"): "https://drexel.edu/coas/academics/departments-centers/mathematics/faculty/",
        ("University of California, Davis", "Physics"): "https://physics.ucdavis.edu/directory/faculty",
        ("Stanford University", "Mathematics"): "https://mathematics.stanford.edu/people/faculty-lecturers",
        ("University of California, San Diego", "Mathematics"): "https://math.ucsd.edu/people/faculty",
        ("Wayne State University", "Chemistry"): "https://clas.wayne.edu/chemistry/people",
        ("University of Maryland, College Park", "Mechanical Engineering"): "https://enme.umd.edu/clark/facultydir",
        ("Colorado School of Mines", "Chemistry"): "https://chemistry.mines.edu/faculty-and-staff/",
        ("University of Maryland, College Park", "Mathematics"): "https://www-math.umd.edu/people/faculty.html",
        ("New Jersey Institute of Technology", "Physics"): "https://physics.njit.edu/people",
        ("Graduate Center, CUNY", "Mechanical Engineering"): "",  # No mapping provided.
        ("University of California, Riverside", "Chemistry"): "https://chem.ucr.edu/people/faculty",
        ("Harvard University", "Chemistry"): "https://www.chemistry.harvard.edu/our-faculty",
        ("University of North Carolina at Chapel Hill", "Chemistry"): "https://chem.unc.edu/faculty-alpha/",
        ("University of Southern California", "Physics"): "https://dornsife.usc.edu/physics/",
        ("University of Connecticut", "Mathematics"): "https://math.uconn.edu",
        ("Clemson University", "Chemistry"): "https://www.clemson.edu/science/academics/departments/chemistry/about/people.html",
        ("Case Western Reserve University", "Chemistry"): "https://chemistry.case.edu/people/faculty/",
        ("Old Dominion University", "Mathematics"): "https://www.odu.edu/math/directory",
        ("Texas Tech University", "Mathematics"): "https://www.depts.ttu.edu/math/facultystaff/",
        ("Ohio University", "Chemistry"): "https://www.ohio.edu/cas/chemistry/contact/faculty-directory",
        ("Massachusetts Institute of Technology", "Mathematics"): "https://math.mit.edu/directory/faculty/",
        ("Temple University", "Mathematics"): "https://www.math.temple.edu/people/directory/faculty/",
        ("University of Houston", "Mathematics"): "https://uh.edu/nsm/math/people/listed_view/",
        ("Florida State University", "Chemistry"): "https://chem.fsu.edu",
        ("Stony Brook University", "Physics"): "https://www.stonybrook.edu/commcms/physics/people/faculty/facultyabc",
        ("University of Notre Dame", "Mathematics"): "https://math.nd.edu/",
        ("Brown University", "Mathematics"): "https://www.brown.edu/academics/math/faculty",
        ("University at Buffalo", "Mathematics"): "https://www.buffalo.edu/cas/math/people.html",
        ("Johns Hopkins University", "Physics"): "https://physics-astronomy.jhu.edu/people/",
        ("Texas Tech University", "Computer Science"): "https://www.depts.ttu.edu/cs/faculty/",
        ("Mississippi State University", "Chemistry"): "https://www.chemistry.msstate.edu/about/directory",
        ("Michigan State University", "Chemistry"): "https://www.chemistry.msu.edu/faculty-research/faculty-members/index.aspx",
        ("University of Texas at Austin", "Physics"): "https://zippy.ph.utexas.edu/directory.html?view=faculty",
        ("University of Chicago", "Mathematics"): "https://mathematics.uchicago.edu/people/"
    }

    # Read the CSV file that contains 'department' in "University-Department" format.
    df = pd.read_csv('email-launch.csv')
    departments = df['department'].unique()

    data_rows = []
    for dept in departments:
        parts = dept.split('-', 1)
        if len(parts) == 2:
            university, department = parts
        else:
            university, department = parts[0], ''
        university = university.strip()
        department = department.strip()

        # Check static mapping first.
        url = faculty_url_mapping.get((university, department), "")
        if not url:
            # Use the Perplexity API if no static mapping is found.
            url = search_faculty_url_perplexity(university, department)
            # Pause to avoid throttling.
            time.sleep(1.5)
        
        # Append our data row.
        data_rows.append([university, department, url, '', '', '', '', '', ''])
    
    # Create the DataFrame.
    output_df = pd.DataFrame(data_rows, columns=[
        'University', 
        'Department',
        'Faculty Directory URL',
        'Total Faculty Count (2024)', 
        'URM Faculty Count (2024)', 
        'Women Faculty Count (2024)', 
        'URM Fraction', 
        'Women Fraction',
        'Notes'
    ])
    
    # Write data to an Excel file with an Instructions sheet and formula cells.
    with pd.ExcelWriter('faculty_demographics_template.xlsx', engine='openpyxl') as writer:
        instructions = pd.DataFrame([
            ['INSTRUCTIONS FOR RESEARCH ASSISTANTS:'],
            [''],
            ['1. Click the Faculty Directory URL to visit the department website and count faculty for 2024.'],
            ['2. URM faculty are those who appear to be Black, Hispanic, or Native American.'],
            ['3. Count faculty who appear to be women.'],
            ['4. The URM and Women fractions will calculate automatically.'],
            ['5. Use the Notes column for any clarifications or issues.']
        ])
        instructions.to_excel(writer, sheet_name='Instructions', header=False, index=False)
        output_df.to_excel(writer, sheet_name='Faculty Demographics', index=False)
        
        workbook = writer.book
        worksheet = writer.sheets['Faculty Demographics']
        # Set formulas for columns G (URM Fraction) and H (Women Fraction)
        for i in range(2, len(data_rows) + 2):
            worksheet[f'G{i}'] = f'=IF(D{i}>0, E{i}/D{i}, "")'
            worksheet[f'H{i}'] = f'=IF(D{i}>0, F{i}/D{i}, "")'
    
    print("Excel template with faculty directory URLs created successfully!")

if __name__ == '__main__':
    main()
