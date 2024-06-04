<h1 align="center">Olympics Data Dive: Unveiling Performance Trends</h1>

### INTRODUCTION<hr>
- The Olympics are a premier international sports event uniting athletes globally, with a rich history dating back to ancient Greece. 
- Data analytics plays a crucial role in understanding and enhancing athletes' performance, training methods, and overall outcomes.
- This project employs Power BI for analyzing Olympic data, providing interactive visualization and advanced statistical modeling.
- The project aims to analyze athlete and country performance across Olympic events, identifying trends and correlations to inform sports management and training strategies.


### LITERATURE REVIEW<hr>
![image](https://github.com/krishnaura45/Olympics_Data_Dive/assets/118080140/127d42c4-429f-4a3c-9472-2b18752033b8)


### OBJECTIVES<hr>
- Explore historical performance trends.
- Study data analytics using tools such as Power BI  
- Develop interactive dashboards for intuitive exploration.
- Utilize Python for statistical analysis and modeling.
- Build interactive app


### WORKING<hr>
<b>Step 1: Collection of Required Data</b>
- Utilized our newly constructed dataset ‘Olympics Legacy: 1896-2020’.
- It includes comprehensive data spanning 124 years of Olympics.
- It’s primary file has 12 features and 2,86,238 records.

Dataset Link - <a href="https://www.kaggle.com/datasets/krishd123/olympics-legacy-1896-2020" target="_blank">Olympics Legacy</a>

<img src='https://github.com/krishnaura45/Olympics_Data_Dive/blob/main/dataset.png' alt='Main csv file'> all_athete_games.csv</img>

<b>Step 2: Data Analysis and Dashboard Creation using Power BI</b>
- Transform Data: Into a final dataframe by
  - Removing columns
  - Defining relationships / Merging
  - Other measures
   
- Analyzing Olympics data using various charts such as-
  - Table chart: Medal Tally
  - Ribbon chart: Age-wise Performance
  - Pie chart: Gender-wise participation
  - Cards for specific stats

<b>Step 3: Python Analysis</b>
- Performed operations such as:
  - Merging files on the basis of specific features
  - Extracting summer olympics data
  - Calculating number and names of countries participated
  - Handling missing and duplicate values
  - One Hot Encoding of Medals
  - Grouping encoded data along with original on the basis of specific features
  - Calculating two different medal tallies with respect to accuracy
 
- Performed four types of analysis:
  - *Medal Tally Analysis*
    1) ***Overall Tally***: Displays the total medal count for all countries across all years.
    2) ***Year-wise Tally***: Shows the medal count for all countries for a particular year.
    3) ***Year-over-Year Tally***: Presents the medal count for all countries over multiple years.
    4) ***Country-specific Tally***: Provides the medal count for a particular year and country.

  - *Athlete-wise Analysis*
    1) ***Distribution of Age vs. Medals***: Examines the distribution of athlete ages concerning the number of medals won.
    2) ***Distribution of Age vs. Sports (Gold Medalist)***: Analyzes the age distribution of gold medalists across different sports.
    3) ***Men vs. Women Participation Over Years***: Visualizes the participation trends of men and women athletes over various editions of the Olympics.

  - *Country-wise Analysis*
    1) ***Medal Tally Over Years***: Visualizes the medal tally for a specific country across different editions of the Olympics.
    2) ***Sports Excellence***: Identifies the sports in which a particular country excels based on medal counts.
    3) ***Top 10 Athletes***: Highlights the top 10 athletes from a specific country based on their performance in the Olympics.

  - *Overall Analysis*
    1) ***Top Statistics***: Evaluates key metrics such as the number of editions, hosting countries, sports, events, nations participated, and athletes.
    2) ***Participating Nations Over Years***: Visualizes the trend of participating nations over different editions of the Olympics.
    3) ***Events Over Years***: Illustrates the evolution of Olympic events over time using line plots.
    4) ***Athletes Over Years***: Depicts the growth in the number of athletes participating in the Olympics across editions.
    5) ***Number of Events Over Time*** and ***Most Successful Athletes***

<b>Step 4: Web App Development</b>
- Developed web app using ***Streamlit***, simplifying interactive data exploration with minimal code.
- Scripted Python functions for preprocessing, analysis, and visualization, ***enhancing modularity***.
- Created helper modules (helper.py and preprocessor.py) for ***streamlined data manipulation*** and ***maintenance***.
- Utilized Streamlit's intuitive interface for ***user-friendly data visualization*** and dashboard creation.

<b>Step 5: Deployment</b>
- Prepare the locally developed web app for deployment on a cloud platform, prioritizing ***Heroku*** for its ***user-friendly interface*** and ***Python support***.
- Create necessary files including ***requirements.txt*** and ***Procfile*** to ensure Heroku can install dependencies and execute the application seamlessly.
- Push the application code and required files to a Git repository for version control and collaboration.
- Deploy the application on Heroku using either the ***CLI*** or web dashboard, initiating automatic build and deployment processes to generate a unique ***URL for access***.


<h3 align="left">RESULTS AND VISUALIZATIONS</h3><hr>
<h4 align="left">Complete Power BI Dashboard - Overview</h4>
<img src='https://github.com/krishnaura45/Olympics_Data_Dive/blob/main/power_bi_dashboard.jpeg' align='center'><br>

<h4 align="left">Web App Interface - Overall Medal Tally</h4>
<img src='https://github.com/krishnaura45/Olympics_Data_Dive/assets/118080140/549caaec-e5f1-4ba0-8272-9b45cc37f4b9' align='center'><br>

<h4 align="left">Overall Analysis Page</h4>
<img src='https://github.com/krishnaura45/Olympics_Data_Dive/assets/118080140/24a21301-0442-4580-a51b-236e3bba9a6c' align='center'><br>

<h4 align="left">Country specific Analysis (India)</h4>
<img src='https://github.com/krishnaura45/Olympics_Data_Dive/assets/118080140/69dcbcd5-2c1a-4e65-ab63-2f537c25f767' align='center'><br>

<h4 align="left">India's Overall Performance</h4>
<img src='https://github.com/krishnaura45/Olympics_Data_Dive/assets/118080140/91b8293e-049d-4f54-96b2-5b725666cb03' align='center'><br>


### CONCLUSIONS/OUTCOMES<hr>
- **Comprehensive Dataset Formation**: Through meticulous exploration of 3-4 datasets, curated a comprehensive repository of Olympic data spanning various aspects, including athlete performances and other logistical details.

- **Insightful Dashboard Creation with Power BI**: Utilizing Power BI, transformed our analytical findings into interactive and visually appealing dashboard, offering stakeholders a user-friendly platform to explore and understand the intricacies of Olympic performance trends.
  
- **Enriched understanding via Python analysis**, delving into medal tallies, overall trends, country-specific performances, and athlete characteristics.
- Extension of analysis reach through **development and deployment** of a **user-friendly web app using Streamlit and Heroku**, facilitating real-time exploration of Olympic datasets.
- **Strategic implications** can be identified for countries, enabling optimization of training programs, resource allocation, and strategic partnerships to enhance competitiveness on the global Olympic stage.


### FUTURE SCOPE<hr>
- Analyze data through Tableau.
- Enabling dynamic and up-to-date analysis.
- Enhance predictive modeling capabilities to forecast athlete performances.


### REFERENCES<hr>
1) Geurin, Andrea N., and Michael L. Naraine. "20 years of Olympic media research: trends and future directions." Frontiers in Sports and Active Living 2 (2020): 572495.
2) P. Johnson and S. Lee, "The Evolution of Gender Parity in the Olympic Games," Gender & Sport, vol. 8, no. 1, pp. 17-28, 2018.
3) M. Garcia and F. Rodriguez, "Impact of Hosting the Olympics on National Performance," J. Sport Econ., vol. 20, no. 4, pp. 301-315, 2019.
4) G. Becker and D. Stevens, "Olympic Medals and Economic Development: A 120-Year Perspective," J. Econ. Dev., vol. 15, no. 2, pp. 87-101, 2014.
5) Y. Kim and J. Park, "Climate and Its Effect on Olympic Performance," Clim. Change Sports, vol. 5, no. 3, pp. 210-225, 2021.


### TECH STACKS INVOLVED<hr>
- Python
- Power BI
- Streamlit

# TEAM THE BOYS<hr>
Krishna Dubey (Data Collection, Dashboard and Analysis), Pankaj Kumar Giri (Data Collection), Nayandeep (Android)
