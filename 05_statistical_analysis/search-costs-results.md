---
title: "Search Costs Field Experiment"
date: "2025-06-03"
output:
  pdf_document:
    toc: true
    toc_depth: 3
    number_sections: true
    fig_caption: true
    keep_tex: true
    keep_md: true
header-includes:
  - \usepackage{booktabs}
  - \usepackage{longtable}
  - \usepackage{array}
  - \usepackage{multirow}
  - \usepackage{float}
  - \usepackage{pdflscape}
  - \newcommand{\blandscape}{\begin{landscape}}
  - \newcommand{\elandscape}{\end{landscape}}
  - \usepackage{caption}
  - \captionsetup[table]{position=below,skip=10pt}
  - \usepackage{dcolumn}
  - \usepackage{adjustbox}
  - \usepackage{tabularx}
  - \newcolumntype{C}[1]{>{\centering\arraybackslash}p{#1}}
---





\newpage

# Summary Statistics

## Overall Summary Statistics

### Seminar Speaker Demographics

\begin{table}[H]
\caption{Overall Seminar Statistics}
\label{tab:summary_seminars_basic}
\centering
\begin{tabular}{lr}
\toprule
Statistic & Value \\
\midrule
Number of seminars & 1656 \\
Number of unique departments & 530 \\
Total speakers across all seminars & 23168 \\
Mean speakers per seminar & 13.99 \\
SD speakers per seminar & 9.95 \\
Min speakers in a seminar & 1 \\
Max speakers in a seminar & 76 \\
\bottomrule
\end{tabular}
\end{table}

\begin{table}[H]
\caption{Seminar Speaker Demographics (Across All Seminars)}
\label{tab:summary_seminar_demographics}
\centering
\footnotesize
\begin{tabular}{lccccc}
\toprule
Demographic Group & Mean \% & SD \% & Mean Count & SD Count & Pct. Any \\
\midrule
URM & 7.91 & 11.44 & 1.08 & 1.35 & 56.0 \\
Black & 2.28 & 5.99 & 0.32 & 0.70 & 24.0 \\
Hispanic & 5.60 & 9.76 & 0.75 & 1.09 & 45.4 \\
Female & 16.89 & 16.18 & 2.38 & 2.50 & 75.8 \\
\bottomrule
\end{tabular}
\parbox{\linewidth}{\footnotesize Note: N =  1656  seminars. Percentages calculated among speakers with demographic data available. 'Pct. Any' indicates the percentage of seminars that have at least one speaker from that demographic group.}
\end{table}

### Department Faculty Demographics


\begin{table}[H]
\caption{Department Faculty Demographics}
\label{tab:summary_dept_faculty}
\centering
\begin{tabular}{lcc}
\toprule
Statistic & Mean & SD \\
\midrule
Total faculty per department & 32.3 & 18.7 \\
\% URM faculty & 3.97 & 4.42 \\
\% Women faculty & 19.50 & 8.44 \\
\bottomrule
\end{tabular}
\parbox{\linewidth}{\footnotesize Note: N =  530  unique departments. Department faculty demographics based on 2024 coding.}
\end{table}

## Summary Statistics by Discipline

### Seminar Speaker Demographics by Discipline


\begin{table}[H]
\caption{Seminar Statistics by Discipline}
\label{tab:summary_disc_basic}
\centering
\footnotesize
\begin{tabular}{lcccc}
\toprule
Discipline & N Seminars & N Depts & Mean Speakers & SD Speakers \\
\midrule
Chemistry & 271 & 123 & 14.7 & 11.1 \\
Computer Science & 142 & 82 & 13.1 & 10.3 \\
Mathematics & 811 & 134 & 13.2 & 9.1 \\
Mechanical Engineering & 82 & 66 & 12.9 & 10.2 \\
Physics & 350 & 125 & 15.9 & 10.4 \\
\bottomrule
\end{tabular}
\end{table}

\begin{table}[H]
\caption{Seminar Speaker Demographics by Discipline: URM}
\label{tab:summary_disc_urm}
\centering
\footnotesize
\begin{tabular}{lccccc}
\toprule
Discipline & N Seminars & Mean \% & SD \% & Mean Count & Pct. Has Any \\
\midrule
Chemistry & 271 & 9.36 & 10.59 & 1.34 & 66.1 \\
Computer Science & 142 & 4.86 & 9.01 & 0.61 & 38.0 \\
Mathematics & 811 & 7.43 & 11.10 & 1.00 & 51.5 \\
Mechanical Engineering & 82 & 8.50 & 9.22 & 1.17 & 63.4 \\
Physics & 350 & 8.99 & 13.72 & 1.25 & 64.3 \\
\bottomrule
\end{tabular}
\parbox{\linewidth}{\footnotesize Note: Statistics are for seminar speakers. 'Pct. Has Any' indicates percentage of seminars with at least one URM speaker.}
\end{table}

\begin{table}[H]
\caption{Seminar Speaker Demographics by Discipline: Other Groups}
\label{tab:summary_disc_other}
\centering
\footnotesize
\begin{tabular}{lcccccc}
\toprule
 & \multicolumn{2}{c}{Black} & \multicolumn{2}{c}{Hispanic} & \multicolumn{2}{c}{Female} \\
Discipline & Mean \% & Pct. Any & Mean \% & Pct. Any & Mean \% & Pct. Any \\
\midrule
Chemistry & 4.34 & 40.6 & 4.91 & 48.0 & 23.66 & 86.7 \\
Computer Science & 1.46 & 16.9 & 3.41 & 27.5 & 19.09 & 79.6 \\
Mathematics & 1.75 & 19.6 & 5.67 & 43.6 & 13.93 & 70.3 \\
Mechanical Engineering & 3.40 & 32.9 & 5.10 & 46.3 & 19.32 & 75.6 \\
Physics & 1.99 & 22.3 & 7.00 & 54.6 & 17.03 & 78.9 \\
\bottomrule
\end{tabular}
\parbox{\linewidth}{\footnotesize Note: Statistics are for seminar speakers. 'Pct. Any' indicates percentage of seminars with at least one speaker from that group.}
\end{table}

### Department Faculty Demographics by Discipline


\begin{table}[H]
\caption{Department Faculty Demographics by Discipline}
\label{tab:summary_disc_dept_faculty}
\centering
\footnotesize
\begin{tabular}{lccccccc}
\toprule
 & & \multicolumn{2}{c}{Faculty Size} & \multicolumn{2}{c}{\% URM Faculty} & \multicolumn{2}{c}{\% Women Faculty} \\
Discipline & N Depts & Mean & SD & Mean & SD & Mean & SD \\
\midrule
Chemistry & 123 & 27.2 & 13.0 & 4.66 & 4.53 & 23.39 & 8.45 \\
Computer Science & 82 & 41.3 & 25.5 & 2.79 & 3.27 & 19.34 & 8.19 \\
Mathematics & 134 & 32.4 & 17.0 & 3.56 & 3.56 & 18.95 & 8.26 \\
Mechanical Engineering & 66 & 34.0 & 20.3 & 5.32 & 5.54 & 18.78 & 8.47 \\
Physics & 125 & 30.5 & 17.2 & 3.79 & 4.88 & 16.76 & 7.46 \\
\bottomrule
\end{tabular}
\parbox{\linewidth}{\footnotesize Note: Department faculty demographics based on 2024 coding.}
\end{table}

## Summary Statistics by Semester


\begin{table}[H]
\caption{Summary Statistics by Semester}
\label{tab:summary_semester}
\centering
\footnotesize
\begin{tabular}{lccccccc}
\toprule
 & \multicolumn{3}{c}{URM} & \multicolumn{2}{c}{Black} & \multicolumn{2}{c}{Hispanic} \\
Semester (N) & Mean \% & Mean Count & Pct. Any & Mean \% & Pct. Any & Mean \% & Pct. Any \\
\midrule
Fall (1448) & 7.47 & 0.57 & 38.5 & 1.78 & 12.1 & 5.67 & 30.9 \\
Spring (1397) & 8.10 & 0.69 & 43.5 & 2.72 & 18.5 & 5.36 & 32.1 \\
\midrule
 & \multicolumn{3}{c}{Female} & \multicolumn{2}{c}{Total Speakers} & & \\
Semester & Mean \% & Mean Count & Pct. Any & Mean & SD & & \\
\midrule
Fall & 15.93 & 1.26 & 61.5 & 7.75 & 5.50 & & \\
Spring & 17.85 & 1.52 & 64.4 & 8.56 & 6.92 & & \\
\bottomrule
\end{tabular}
\end{table}

\newpage

# Main Effects Analysis

## Main Question 1: URM Speaker Representation

\begin{table}[H]
\caption{Main Question 1: Effect on URM Speaker Representation}
\label{tab:mq1_urm}
\centering
\scriptsize
\begin{tabularx}{\textwidth}{l*{6}{>{\centering\arraybackslash}X}}
\toprule
 & \% URM & \% URM & Count URM & Count URM & Any URM & Any URM \\
 &  (1) & (2) & (3) & (4) & (5) & (6)  \\
\midrule
Treatment  &  0.658$^{}$ & 0.651$^{}$ & 0.090$^{}$ & 0.069$^{}$ & 0.009$^{}$ & 0.007$^{}$  \\
 &  (0.539) & (0.535) & (0.070) & (0.068) & (0.025) & (0.023)  \\
Constant  &  8.523$^{***}$ & 4.387$^{*}$ & 1.251$^{***}$ & 0.357$^{}$ & 0.635$^{***}$ & 0.298$^{**}$  \\
 &  (1.580) & (1.954) & (0.176) & (0.269) & (0.063) & (0.100)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,656 & 1,656 & 1,656 & 1,656 & 1,656 & 1,656  \\
Adjusted $R^2$ &  0.011 & 0.016 & 0.026 & 0.034 & 0.032 & 0.047  \\
\bottomrule
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize \vspace{2pt}Clustered standard errors at department level in parentheses.}}\\
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize $^{+}p<0.1$; $^{*}p<0.05$; $^{**}p<0.01$; $^{***}p<0.001$\vspace{2pt}}}\\
\end{tabularx}
\end{table}

\newpage

## Main Questions 2a-2c: Effects on Speaker Counts

\begin{table}[H]
\caption{Main Questions 2a-2c: Effects on Speaker Counts}
\label{tab:mq2_all}
\centering
\scriptsize
\begin{tabularx}{\textwidth}{l*{6}{>{\centering\arraybackslash}X}}
\toprule
 & \% Count & \% Count & Count Count & Count Count & Any Count & Any Count \\
 &  (1) & (2) & (3) & (4) & (5) & (6)  \\
\midrule
Treatment  &  -0.461$^{}$ & -0.502$^{}$ & 0.090$^{}$ & 0.069$^{}$ & -0.542$^{}$ & -0.565$^{}$  \\
 &  (0.554) & (0.542) & (0.070) & (0.068) & (0.524) & (0.512)  \\
Constant  &  16.810$^{***}$ & 12.854$^{***}$ & 1.251$^{***}$ & 0.357$^{}$ & 15.529$^{***}$ & 12.440$^{***}$  \\
 &  (1.313) & (2.276) & (0.176) & (0.269) & (1.234) & (2.132)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,656 & 1,656 & 1,656 & 1,656 & 1,656 & 1,656  \\
Adjusted $R^2$ &  0.031 & 0.058 & 0.026 & 0.034 & 0.029 & 0.058  \\
\bottomrule
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize \vspace{2pt}Clustered standard errors at department level in parentheses.}}\\
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize $^{+}p<0.1$; $^{*}p<0.05$; $^{**}p<0.01$; $^{***}p<0.001$\vspace{2pt}}}\\
\end{tabularx}
\end{table}

## Seemingly Unrelated Regression (SUR) Analysis


\begin{table}[H]
\caption{SUR Analysis: Testing Substitution Between URM and Non-URM Speakers}
\label{tab:sur_analysis}
\centering
\begin{tabular}{lcc}
\toprule
Outcome & Coefficient & SE \\
\midrule
URM Speakers & 0.0896 & (0.0666) \\
Non-URM Speakers & -0.5423 & (0.4575) \\
\midrule
Sum of Effects & -0.4527 & --- \\
\midrule
\multicolumn{3}{l}{\textit{Wald Test: H0: Treatment effect on URM + Treatment effect on Non-URM = 0}} \\
\bottomrule
\end{tabular}
\parbox{\linewidth}{\footnotesize Note: SUR estimation with simple controls allows for correlation between equation errors. The Wald test examines whether the treatment effect represents a pure substitution (increasing URM speakers while decreasing non-URM speakers by the same amount).}
\end{table}

\newpage

# Demographic Subgroup Analysis

## Black Speakers

\begin{table}[H]
\caption{Effect on Black Speakers}
\label{tab:black}
\centering
\scriptsize
\begin{tabularx}{\textwidth}{l*{6}{>{\centering\arraybackslash}X}}
\toprule
 & \% Black & \% Black & Count Black & Count Black & Any Black & Any Black \\
 &  (1) & (2) & (3) & (4) & (5) & (6)  \\
\midrule
Treatment  &  0.561$^{+}$ & 0.527$^{+}$ & 0.068$^{}$ & 0.063$^{}$ & 0.042$^{+}$ & 0.042$^{+}$  \\
 &  (0.313) & (0.298) & (0.042) & (0.040) & (0.023) & (0.022)  \\
Constant  &  2.874$^{***}$ & 0.576$^{}$ & 0.459$^{***}$ & 0.093$^{}$ & 0.295$^{***}$ & 0.065$^{}$  \\
 &  (0.830) & (1.298) & (0.113) & (0.163) & (0.066) & (0.104)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,656 & 1,656 & 1,656 & 1,656 & 1,656 & 1,656  \\
Adjusted $R^2$ &  0.028 & 0.035 & 0.048 & 0.059 & 0.042 & 0.051  \\
\bottomrule
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize \vspace{2pt}Clustered standard errors at department level in parentheses.}}\\
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize $^{+}p<0.1$; $^{*}p<0.05$; $^{**}p<0.01$; $^{***}p<0.001$\vspace{2pt}}}\\
\end{tabularx}
\end{table}

## Hispanic Speakers

\begin{table}[H]
\caption{Effect on Hispanic Speakers}
\label{tab:hispanic}
\centering
\scriptsize
\begin{tabularx}{\textwidth}{l*{6}{>{\centering\arraybackslash}X}}
\toprule
 & \% Hispanic & \% Hispanic & Count Hispanic & Count Hispanic & Any Hispanic & Any Hispanic \\
 &  (1) & (2) & (3) & (4) & (5) & (6)  \\
\midrule
Treatment  &  0.111$^{}$ & 0.138$^{}$ & 0.021$^{}$ & 0.005$^{}$ & -0.008$^{}$ & -0.010$^{}$  \\
 &  (0.468) & (0.476) & (0.052) & (0.052) & (0.025) & (0.025)  \\
Constant  &  5.437$^{***}$ & 3.657$^{*}$ & 0.766$^{***}$ & 0.239$^{}$ & 0.504$^{***}$ & 0.289$^{**}$  \\
 &  (1.458) & (1.766) & (0.146) & (0.217) & (0.065) & (0.101)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,656 & 1,656 & 1,656 & 1,656 & 1,656 & 1,656  \\
Adjusted $R^2$ &  0.005 & 0.004 & 0.013 & 0.019 & 0.019 & 0.023  \\
\bottomrule
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize \vspace{2pt}Clustered standard errors at department level in parentheses.}}\\
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize $^{+}p<0.1$; $^{*}p<0.05$; $^{**}p<0.01$; $^{***}p<0.001$\vspace{2pt}}}\\
\end{tabularx}
\end{table}

## Female Speakers

\begin{table}[H]
\caption{Effect on Female Speakers}
\label{tab:female}
\centering
\scriptsize
\begin{tabularx}{\textwidth}{l*{6}{>{\centering\arraybackslash}X}}
\toprule
 & \% Female & \% Female & Count Female & Count Female & Any Female & Any Female \\
 &  (1) & (2) & (3) & (4) & (5) & (6)  \\
\midrule
Treatment  &  0.087$^{}$ & -0.241$^{}$ & -0.061$^{}$ & -0.130$^{}$ & -0.007$^{}$ & -0.010$^{}$  \\
 &  (0.823) & (0.823) & (0.129) & (0.124) & (0.021) & (0.021)  \\
Constant  &  22.166$^{***}$ & 16.604$^{***}$ & 3.631$^{***}$ & 2.386$^{***}$ & 0.884$^{***}$ & 0.716$^{***}$  \\
 &  (2.010) & (3.826) & (0.342) & (0.575) & (0.061) & (0.090)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,656 & 1,656 & 1,656 & 1,656 & 1,656 & 1,656  \\
Adjusted $R^2$ &  0.050 & 0.056 & 0.087 & 0.106 & 0.017 & 0.028  \\
\bottomrule
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize \vspace{2pt}Clustered standard errors at department level in parentheses.}}\\
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize $^{+}p<0.1$; $^{*}p<0.05$; $^{**}p<0.01$; $^{***}p<0.001$\vspace{2pt}}}\\
\end{tabularx}
\end{table}

## URM Female

\begin{table}[H]
\caption{Effect on URM Female Speakers}
\label{tab:urm_female}
\centering
\scriptsize
\begin{tabularx}{\textwidth}{l*{6}{>{\centering\arraybackslash}X}}
\toprule
 & \% URM Female & \% URM Female & Count URM Female & Count URM Female & Any URM Female & Any URM Female \\
 &  (1) & (2) & (3) & (4) & (5) & (6)  \\
\midrule
Treatment  &  -0.056$^{}$ & -0.104$^{}$ & 0.017$^{}$ & 0.007$^{}$ & 0.011$^{}$ & 0.002$^{}$  \\
 &  (0.174) & (0.188) & (0.019) & (0.019) & (0.017) & (0.017)  \\
Constant  &  1.883$^{**}$ & 0.135$^{}$ & 0.220$^{***}$ & -0.034$^{}$ & 0.190$^{***}$ & -0.043$^{}$  \\
 &  (0.611) & (0.602) & (0.062) & (0.088) & (0.052) & (0.074)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,656 & 1,656 & 1,656 & 1,656 & 1,656 & 1,656  \\
Adjusted $R^2$ &  0.015 & 0.020 & 0.043 & 0.061 & 0.046 & 0.064  \\
\bottomrule
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize \vspace{2pt}Clustered standard errors at department level in parentheses.}}\\
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize $^{+}p<0.1$; $^{*}p<0.05$; $^{**}p<0.01$; $^{***}p<0.001$\vspace{2pt}}}\\
\end{tabularx}
\end{table}

## Black Female

\begin{table}[H]
\caption{Effect on Black Female Speakers}
\label{tab:black_female}
\centering
\scriptsize
\begin{tabularx}{\textwidth}{l*{6}{>{\centering\arraybackslash}X}}
\toprule
 & \% Black Female & \% Black Female & Count Black Female & Count Black Female & Any Black Female & Any Black Female \\
 &  (1) & (2) & (3) & (4) & (5) & (6)  \\
\midrule
Treatment  &  0.098$^{}$ & 0.101$^{}$ & 0.003$^{}$ & 0.002$^{}$ & 0.005$^{}$ & 0.004$^{}$  \\
 &  (0.073) & (0.074) & (0.010) & (0.009) & (0.009) & (0.009)  \\
Constant  &  0.584$^{***}$ & 0.065$^{}$ & 0.079$^{**}$ & 0.014$^{}$ & 0.066$^{**}$ & 0.012$^{}$  \\
 &  (0.176) & (0.285) & (0.025) & (0.042) & (0.022) & (0.036)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,656 & 1,656 & 1,656 & 1,656 & 1,656 & 1,656  \\
Adjusted $R^2$ &  0.032 & 0.037 & 0.023 & 0.029 & 0.018 & 0.024  \\
\bottomrule
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize \vspace{2pt}Clustered standard errors at department level in parentheses.}}\\
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize $^{+}p<0.1$; $^{*}p<0.05$; $^{**}p<0.01$; $^{***}p<0.001$\vspace{2pt}}}\\
\end{tabularx}
\end{table}

## Black Male

\begin{table}[H]
\caption{Effect on Black Male Speakers}
\label{tab:black_male}
\centering
\scriptsize
\begin{tabularx}{\textwidth}{l*{6}{>{\centering\arraybackslash}X}}
\toprule
 & \% Black Male & \% Black Male & Count Black Male & Count Black Male & Any Black Male & Any Black Male \\
 &  (1) & (2) & (3) & (4) & (5) & (6)  \\
\midrule
Treatment  &  0.463$^{+}$ & 0.426$^{+}$ & 0.065$^{+}$ & 0.061$^{+}$ & 0.048$^{*}$ & 0.047$^{*}$  \\
 &  (0.267) & (0.252) & (0.036) & (0.034) & (0.023) & (0.022)  \\
Constant  &  2.290$^{**}$ & 0.511$^{}$ & 0.375$^{***}$ & 0.075$^{}$ & 0.284$^{***}$ & 0.049$^{}$  \\
 &  (0.730) & (1.171) & (0.098) & (0.137) & (0.066) & (0.102)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,656 & 1,656 & 1,656 & 1,656 & 1,656 & 1,656  \\
Adjusted $R^2$ &  0.020 & 0.025 & 0.044 & 0.052 & 0.041 & 0.050  \\
\bottomrule
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize \vspace{2pt}Clustered standard errors at department level in parentheses.}}\\
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize $^{+}p<0.1$; $^{*}p<0.05$; $^{**}p<0.01$; $^{***}p<0.001$\vspace{2pt}}}\\
\end{tabularx}
\end{table}

## Hispanic Female

\begin{table}[H]
\caption{Effect on Hispanic Female Speakers}
\label{tab:hispanic_female}
\centering
\scriptsize
\begin{tabularx}{\textwidth}{l*{6}{>{\centering\arraybackslash}X}}
\toprule
 & \% Hispanic Female & \% Hispanic Female & Count Hispanic Female & Count Hispanic Female & Any Hispanic Female & Any Hispanic Female \\
 &  (1) & (2) & (3) & (4) & (5) & (6)  \\
\midrule
Treatment  &  -0.158$^{}$ & -0.210$^{}$ & 0.004$^{}$ & -0.005$^{}$ & 0.002$^{}$ & -0.006$^{}$  \\
 &  (0.162) & (0.180) & (0.013) & (0.013) & (0.012) & (0.012)  \\
Constant  &  1.274$^{*}$ & 0.044$^{}$ & 0.067$^{}$ & -0.062$^{}$ & 0.062$^{+}$ & -0.062$^{}$  \\
 &  (0.587) & (0.506) & (0.044) & (0.065) & (0.035) & (0.055)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,656 & 1,656 & 1,656 & 1,656 & 1,656 & 1,656  \\
Adjusted $R^2$ &  0.001 & 0.004 & 0.006 & 0.021 & 0.006 & 0.021  \\
\bottomrule
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize \vspace{2pt}Clustered standard errors at department level in parentheses.}}\\
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize $^{+}p<0.1$; $^{*}p<0.05$; $^{**}p<0.01$; $^{***}p<0.001$\vspace{2pt}}}\\
\end{tabularx}
\end{table}

## Hispanic Male

\begin{table}[H]
\caption{Effect on Hispanic Male Speakers}
\label{tab:hispanic_male}
\centering
\scriptsize
\begin{tabularx}{\textwidth}{l*{6}{>{\centering\arraybackslash}X}}
\toprule
 & \% Hispanic Male & \% Hispanic Male & Count Hispanic Male & Count Hispanic Male & Any Hispanic Male & Any Hispanic Male \\
 &  (1) & (2) & (3) & (4) & (5) & (6)  \\
\midrule
Treatment  &  0.269$^{}$ & 0.348$^{}$ & 0.016$^{}$ & 0.009$^{}$ & -0.008$^{}$ & -0.009$^{}$  \\
 &  (0.395) & (0.394) & (0.047) & (0.046) & (0.025) & (0.025)  \\
Constant  &  4.164$^{**}$ & 3.613$^{*}$ & 0.698$^{***}$ & 0.303$^{}$ & 0.501$^{***}$ & 0.295$^{**}$  \\
 &  (1.272) & (1.540) & (0.125) & (0.187) & (0.064) & (0.101)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,656 & 1,656 & 1,656 & 1,656 & 1,656 & 1,656  \\
Adjusted $R^2$ &  0.008 & 0.007 & 0.013 & 0.018 & 0.020 & 0.023  \\
\bottomrule
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize \vspace{2pt}Clustered standard errors at department level in parentheses.}}\\
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize $^{+}p<0.1$; $^{*}p<0.05$; $^{**}p<0.01$; $^{***}p<0.001$\vspace{2pt}}}\\
\end{tabularx}
\end{table}

\newpage

# Discipline Subgroup Analysis


\subsubsection{Chemistry (N=271)}

\begin{table}[H]
\caption{Chemistry : Effect on URM Speaker Representation}
\label{tab:discipline_chemistry_urm}
\centering
\scriptsize
\begin{tabularx}{\textwidth}{l*{6}{>{\centering\arraybackslash}X}}
\toprule
 & \% URM & \% URM & Count URM & Count URM & Any URM & Any URM \\
 &  (1) & (2) & (3) & (4) & (5) & (6)  \\
\midrule
Treatment  &  0.180$^{}$ & -0.657$^{}$ & -0.159$^{}$ & -0.220$^{}$ & 0.028$^{}$ & 0.011$^{}$  \\
 &  (1.198) & (1.210) & (0.171) & (0.177) & (0.052) & (0.058)  \\
Constant  &  5.747$^{*}$ & -0.097$^{}$ & 0.851$^{*}$ & -0.489$^{}$ & 0.146$^{}$ & -0.214$^{}$  \\
 &  (2.675) & (5.225) & (0.418) & (0.705) & (0.119) & (0.249)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  271 & 271 & 271 & 271 & 271 & 271  \\
Adjusted $R^2$ &  -0.025 & -0.016 & 0.109 & 0.111 & 0.097 & 0.098  \\
\bottomrule
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize \vspace{2pt}Clustered standard errors at department level in parentheses.}}\\
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize $^{+}p<0.1$; $^{*}p<0.05$; $^{**}p<0.01$; $^{***}p<0.001$\vspace{2pt}}}\\
\end{tabularx}
\end{table}
\begin{table}[H]
\caption{Chemistry : Effect on Black Speaker Representation}
\label{tab:discipline_chemistry_black}
\centering
\scriptsize
\begin{tabularx}{\textwidth}{l*{6}{>{\centering\arraybackslash}X}}
\toprule
 & \% Black & \% Black & Count Black & Count Black & Any Black & Any Black \\
 &  (1) & (2) & (3) & (4) & (5) & (6)  \\
\midrule
Treatment  &  0.421$^{}$ & 0.052$^{}$ & -0.036$^{}$ & -0.034$^{}$ & 0.065$^{}$ & 0.033$^{}$  \\
 &  (1.082) & (0.923) & (0.126) & (0.112) & (0.067) & (0.068)  \\
Constant  &  2.569$^{}$ & -8.271$^{*}$ & 0.386$^{}$ & -1.290$^{*}$ & 0.148$^{}$ & -0.735$^{*}$  \\
 &  (2.588) & (3.954) & (0.248) & (0.510) & (0.157) & (0.305)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  271 & 271 & 271 & 271 & 271 & 271  \\
Adjusted $R^2$ &  -0.031 & -0.001 & 0.053 & 0.096 & 0.064 & 0.118  \\
\bottomrule
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize \vspace{2pt}Clustered standard errors at department level in parentheses.}}\\
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize $^{+}p<0.1$; $^{*}p<0.05$; $^{**}p<0.01$; $^{***}p<0.001$\vspace{2pt}}}\\
\end{tabularx}
\end{table}
\begin{table}[H]
\caption{Chemistry : Effect on Hispanic Speaker Representation}
\label{tab:discipline_chemistry_hispanic}
\centering
\scriptsize
\begin{tabularx}{\textwidth}{l*{6}{>{\centering\arraybackslash}X}}
\toprule
 & \% Hispanic & \% Hispanic & Count Hispanic & Count Hispanic & Any Hispanic & Any Hispanic \\
 &  (1) & (2) & (3) & (4) & (5) & (6)  \\
\midrule
Treatment  &  -0.173$^{}$ & -0.645$^{}$ & -0.135$^{}$ & -0.203$^{}$ & -0.083$^{}$ & -0.104$^{}$  \\
 &  (1.016) & (1.034) & (0.123) & (0.142) & (0.062) & (0.063)  \\
Constant  &  2.343$^{}$ & 6.315$^{}$ & 0.433$^{}$ & 0.606$^{}$ & 0.147$^{}$ & 0.256$^{}$  \\
 &  (1.857) & (3.844) & (0.367) & (0.519) & (0.154) & (0.268)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  271 & 271 & 271 & 271 & 271 & 271  \\
Adjusted $R^2$ &  -0.019 & -0.017 & 0.053 & 0.072 & 0.035 & 0.049  \\
\bottomrule
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize \vspace{2pt}Clustered standard errors at department level in parentheses.}}\\
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize $^{+}p<0.1$; $^{*}p<0.05$; $^{**}p<0.01$; $^{***}p<0.001$\vspace{2pt}}}\\
\end{tabularx}
\end{table}

\subsubsection{Mathematics (N=811)}

\begin{table}[H]
\caption{Mathematics : Effect on URM Speaker Representation}
\label{tab:discipline_mathematics_urm}
\centering
\scriptsize
\begin{tabularx}{\textwidth}{l*{6}{>{\centering\arraybackslash}X}}
\toprule
 & \% URM & \% URM & Count URM & Count URM & Any URM & Any URM \\
 &  (1) & (2) & (3) & (4) & (5) & (6)  \\
\midrule
Treatment  &  1.153$^{}$ & 1.498$^{+}$ & 0.148$^{}$ & 0.155$^{}$ & 0.023$^{}$ & 0.014$^{}$  \\
 &  (0.711) & (0.853) & (0.097) & (0.116) & (0.032) & (0.031)  \\
Constant  &  5.745$^{***}$ & 3.771$^{}$ & 0.948$^{***}$ & 0.122$^{}$ & 0.524$^{***}$ & 0.178$^{}$  \\
 &  (1.291) & (4.418) & (0.149) & (0.584) & (0.058) & (0.176)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  811 & 811 & 811 & 811 & 811 & 811  \\
Adjusted $R^2$ &  0.004 & 0.002 & -0.000 & -0.000 & -0.006 & 0.004  \\
\bottomrule
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize \vspace{2pt}Clustered standard errors at department level in parentheses.}}\\
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize $^{+}p<0.1$; $^{*}p<0.05$; $^{**}p<0.01$; $^{***}p<0.001$\vspace{2pt}}}\\
\end{tabularx}
\end{table}
\begin{table}[H]
\caption{Mathematics : Effect on Black Speaker Representation}
\label{tab:discipline_mathematics_black}
\centering
\scriptsize
\begin{tabularx}{\textwidth}{l*{6}{>{\centering\arraybackslash}X}}
\toprule
 & \% Black & \% Black & Count Black & Count Black & Any Black & Any Black \\
 &  (1) & (2) & (3) & (4) & (5) & (6)  \\
\midrule
Treatment  &  0.269$^{}$ & 0.508$^{}$ & 0.066$^{}$ & 0.100$^{+}$ & 0.009$^{}$ & 0.014$^{}$  \\
 &  (0.373) & (0.435) & (0.051) & (0.058) & (0.030) & (0.028)  \\
Constant  &  0.459$^{}$ & 0.902$^{}$ & 0.182$^{*}$ & 0.372$^{}$ & 0.146$^{**}$ & 0.061$^{}$  \\
 &  (0.492) & (2.365) & (0.071) & (0.270) & (0.051) & (0.154)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  811 & 811 & 811 & 811 & 811 & 811  \\
Adjusted $R^2$ &  0.024 & 0.036 & 0.011 & 0.025 & 0.008 & 0.026  \\
\bottomrule
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize \vspace{2pt}Clustered standard errors at department level in parentheses.}}\\
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize $^{+}p<0.1$; $^{*}p<0.05$; $^{**}p<0.01$; $^{***}p<0.001$\vspace{2pt}}}\\
\end{tabularx}
\end{table}
\begin{table}[H]
\caption{Mathematics : Effect on Hispanic Speaker Representation}
\label{tab:discipline_mathematics_hispanic}
\centering
\scriptsize
\begin{tabularx}{\textwidth}{l*{6}{>{\centering\arraybackslash}X}}
\toprule
 & \% Hispanic & \% Hispanic & Count Hispanic & Count Hispanic & Any Hispanic & Any Hispanic \\
 &  (1) & (2) & (3) & (4) & (5) & (6)  \\
\midrule
Treatment  &  0.903$^{}$ & 0.995$^{}$ & 0.086$^{}$ & 0.056$^{}$ & 0.042$^{}$ & 0.038$^{}$  \\
 &  (0.637) & (0.709) & (0.078) & (0.082) & (0.033) & (0.035)  \\
Constant  &  5.210$^{***}$ & 2.721$^{}$ & 0.747$^{***}$ & -0.286$^{}$ & 0.459$^{***}$ & 0.217$^{}$  \\
 &  (1.249) & (3.331) & (0.133) & (0.463) & (0.065) & (0.195)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  811 & 811 & 811 & 811 & 811 & 811  \\
Adjusted $R^2$ &  -0.005 & -0.006 & -0.003 & 0.001 & -0.002 & -0.001  \\
\bottomrule
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize \vspace{2pt}Clustered standard errors at department level in parentheses.}}\\
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize $^{+}p<0.1$; $^{*}p<0.05$; $^{**}p<0.01$; $^{***}p<0.001$\vspace{2pt}}}\\
\end{tabularx}
\end{table}

\subsubsection{Physics (N=350)}

\begin{table}[H]
\caption{Physics : Effect on URM Speaker Representation}
\label{tab:discipline_physics_urm}
\centering
\scriptsize
\begin{tabularx}{\textwidth}{l*{6}{>{\centering\arraybackslash}X}}
\toprule
 & \% URM & \% URM & Count URM & Count URM & Any URM & Any URM \\
 &  (1) & (2) & (3) & (4) & (5) & (6)  \\
\midrule
Treatment  &  0.116$^{}$ & 0.223$^{}$ & 0.206$^{}$ & 0.227$^{}$ & -0.013$^{}$ & 0.001$^{}$  \\
 &  (1.279) & (1.194) & (0.140) & (0.141) & (0.061) & (0.057)  \\
Constant  &  14.461$^{***}$ & 14.002$^{}$ & 1.405$^{***}$ & 2.788$^{*}$ & 0.540$^{***}$ & 1.036$^{+}$  \\
 &  (2.251) & (13.765) & (0.160) & (1.361) & (0.061) & (0.601)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  350 & 350 & 350 & 350 & 350 & 350  \\
Adjusted $R^2$ &  -0.002 & -0.012 & -0.002 & 0.006 & 0.003 & 0.032  \\
\bottomrule
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize \vspace{2pt}Clustered standard errors at department level in parentheses.}}\\
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize $^{+}p<0.1$; $^{*}p<0.05$; $^{**}p<0.01$; $^{***}p<0.001$\vspace{2pt}}}\\
\end{tabularx}
\end{table}
\begin{table}[H]
\caption{Physics : Effect on Black Speaker Representation}
\label{tab:discipline_physics_black}
\centering
\scriptsize
\begin{tabularx}{\textwidth}{l*{6}{>{\centering\arraybackslash}X}}
\toprule
 & \% Black & \% Black & Count Black & Count Black & Any Black & Any Black \\
 &  (1) & (2) & (3) & (4) & (5) & (6)  \\
\midrule
Treatment  &  1.251$^{*}$ & 1.307$^{*}$ & 0.162$^{*}$ & 0.165$^{*}$ & 0.117$^{*}$ & 0.120$^{*}$  \\
 &  (0.625) & (0.636) & (0.068) & (0.069) & (0.050) & (0.051)  \\
Constant  &  0.605$^{}$ & 1.075$^{}$ & 0.067$^{}$ & 0.445$^{}$ & 0.042$^{}$ & 0.279$^{}$  \\
 &  (0.688) & (4.079) & (0.085) & (0.577) & (0.058) & (0.393)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  350 & 350 & 350 & 350 & 350 & 350  \\
Adjusted $R^2$ &  0.006 & 0.002 & 0.019 & 0.011 & 0.005 & 0.011  \\
\bottomrule
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize \vspace{2pt}Clustered standard errors at department level in parentheses.}}\\
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize $^{+}p<0.1$; $^{*}p<0.05$; $^{**}p<0.01$; $^{***}p<0.001$\vspace{2pt}}}\\
\end{tabularx}
\end{table}
\begin{table}[H]
\caption{Physics : Effect on Hispanic Speaker Representation}
\label{tab:discipline_physics_hispanic}
\centering
\scriptsize
\begin{tabularx}{\textwidth}{l*{6}{>{\centering\arraybackslash}X}}
\toprule
 & \% Hispanic & \% Hispanic & Count Hispanic & Count Hispanic & Any Hispanic & Any Hispanic \\
 &  (1) & (2) & (3) & (4) & (5) & (6)  \\
\midrule
Treatment  &  -1.135$^{}$ & -1.084$^{}$ & 0.043$^{}$ & 0.061$^{}$ & -0.052$^{}$ & -0.042$^{}$  \\
 &  (1.265) & (1.224) & (0.130) & (0.132) & (0.065) & (0.064)  \\
Constant  &  13.855$^{***}$ & 12.926$^{}$ & 1.338$^{***}$ & 2.343$^{*}$ & 0.534$^{***}$ & 0.951$^{}$  \\
 &  (2.284) & (12.986) & (0.144) & (1.171) & (0.072) & (0.597)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  350 & 350 & 350 & 350 & 350 & 350  \\
Adjusted $R^2$ &  -0.005 & -0.016 & -0.013 & 0.006 & -0.000 & 0.002  \\
\bottomrule
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize \vspace{2pt}Clustered standard errors at department level in parentheses.}}\\
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize $^{+}p<0.1$; $^{*}p<0.05$; $^{**}p<0.01$; $^{***}p<0.001$\vspace{2pt}}}\\
\end{tabularx}
\end{table}

\subsubsection{Computer Science (N=142)}

\begin{table}[H]
\caption{Computer Science : Effect on URM Speaker Representation}
\label{tab:discipline_computer_science_urm}
\centering
\scriptsize
\begin{tabularx}{\textwidth}{l*{6}{>{\centering\arraybackslash}X}}
\toprule
 & \% URM & \% URM & Count URM & Count URM & Any URM & Any URM \\
 &  (1) & (2) & (3) & (4) & (5) & (6)  \\
\midrule
Treatment  &  2.285$^{+}$ & 2.529$^{}$ & 0.124$^{}$ & 0.052$^{}$ & 0.108$^{}$ & 0.114$^{}$  \\
 &  (1.377) & (1.763) & (0.153) & (0.202) & (0.095) & (0.088)  \\
Constant  &  8.029$^{***}$ & 7.913$^{}$ & 1.463$^{***}$ & 3.396$^{*}$ & 0.807$^{***}$ & 2.639$^{***}$  \\
 &  (1.496) & (13.562) & (0.274) & (1.449) & (0.178) & (0.702)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  142 & 142 & 142 & 142 & 142 & 142  \\
Adjusted $R^2$ &  0.078 & 0.105 & 0.121 & 0.098 & 0.104 & 0.127  \\
\bottomrule
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize \vspace{2pt}Clustered standard errors at department level in parentheses.}}\\
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize $^{+}p<0.1$; $^{*}p<0.05$; $^{**}p<0.01$; $^{***}p<0.001$\vspace{2pt}}}\\
\end{tabularx}
\end{table}
\begin{table}[H]
\caption{Computer Science : Effect on Black Speaker Representation}
\label{tab:discipline_computer_science_black}
\centering
\scriptsize
\begin{tabularx}{\textwidth}{l*{6}{>{\centering\arraybackslash}X}}
\toprule
 & \% Black & \% Black & Count Black & Count Black & Any Black & Any Black \\
 &  (1) & (2) & (3) & (4) & (5) & (6)  \\
\midrule
Treatment  &  0.332$^{}$ & -0.138$^{}$ & -0.041$^{}$ & -0.065$^{}$ & -0.015$^{}$ & -0.049$^{}$  \\
 &  (0.671) & (0.645) & (0.067) & (0.068) & (0.056) & (0.062)  \\
Constant  &  3.892$^{**}$ & -0.450$^{}$ & 0.629$^{**}$ & 1.496$^{}$ & 0.487$^{**}$ & 0.944$^{}$  \\
 &  (1.485) & (8.588) & (0.226) & (0.933) & (0.158) & (0.696)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  142 & 142 & 142 & 142 & 142 & 142  \\
Adjusted $R^2$ &  -0.018 & -0.048 & 0.026 & 0.018 & 0.029 & 0.015  \\
\bottomrule
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize \vspace{2pt}Clustered standard errors at department level in parentheses.}}\\
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize $^{+}p<0.1$; $^{*}p<0.05$; $^{**}p<0.01$; $^{***}p<0.001$\vspace{2pt}}}\\
\end{tabularx}
\end{table}
\begin{table}[H]
\caption{Computer Science : Effect on Hispanic Speaker Representation}
\label{tab:discipline_computer_science_hispanic}
\centering
\scriptsize
\begin{tabularx}{\textwidth}{l*{6}{>{\centering\arraybackslash}X}}
\toprule
 & \% Hispanic & \% Hispanic & Count Hispanic & Count Hispanic & Any Hispanic & Any Hispanic \\
 &  (1) & (2) & (3) & (4) & (5) & (6)  \\
\midrule
Treatment  &  1.953$^{}$ & 2.667$^{}$ & 0.165$^{}$ & 0.117$^{}$ & 0.144$^{}$ & 0.156$^{+}$  \\
 &  (1.426) & (1.699) & (0.141) & (0.174) & (0.098) & (0.083)  \\
Constant  &  4.138$^{*}$ & 8.363$^{}$ & 0.834$^{***}$ & 1.899$^{+}$ & 0.628$^{**}$ & 2.352$^{***}$  \\
 &  (1.791) & (10.246) & (0.244) & (1.009) & (0.207) & (0.662)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  142 & 142 & 142 & 142 & 142 & 142  \\
Adjusted $R^2$ &  0.076 & 0.143 & 0.075 & 0.065 & 0.092 & 0.141  \\
\bottomrule
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize \vspace{2pt}Clustered standard errors at department level in parentheses.}}\\
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize $^{+}p<0.1$; $^{*}p<0.05$; $^{**}p<0.01$; $^{***}p<0.001$\vspace{2pt}}}\\
\end{tabularx}
\end{table}

\subsubsection{Mechanical Engineering (N=82)}

\begin{table}[H]
\caption{Mechanical Engineering : Effect on URM Speaker Representation}
\label{tab:discipline_mechanical_engineering_urm}
\centering
\scriptsize
\begin{tabularx}{\textwidth}{l*{6}{>{\centering\arraybackslash}X}}
\toprule
 & \% URM & \% URM & Count URM & Count URM & Any URM & Any URM \\
 &  (1) & (2) & (3) & (4) & (5) & (6)  \\
\midrule
Treatment  &  3.049$^{}$ & 2.865$^{}$ & 0.715$^{*}$ & 0.849$^{*}$ & 0.037$^{}$ & 0.043$^{}$  \\
 &  (1.991) & (1.895) & (0.344) & (0.368) & (0.111) & (0.127)  \\
Constant  &  14.737$^{*}$ & 5.298$^{}$ & 2.044$^{*}$ & 2.239$^{}$ & 0.722$^{**}$ & 0.566$^{}$  \\
 &  (5.904) & (9.694) & (0.930) & (2.340) & (0.267) & (0.491)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  82 & 82 & 82 & 82 & 82 & 82  \\
Adjusted $R^2$ &  0.006 & 0.007 & -0.006 & 0.083 & 0.016 & 0.034  \\
\bottomrule
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize \vspace{2pt}Clustered standard errors at department level in parentheses.}}\\
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize $^{+}p<0.1$; $^{*}p<0.05$; $^{**}p<0.01$; $^{***}p<0.001$\vspace{2pt}}}\\
\end{tabularx}
\end{table}
\begin{table}[H]
\caption{Mechanical Engineering : Effect on Black Speaker Representation}
\label{tab:discipline_mechanical_engineering_black}
\centering
\scriptsize
\begin{tabularx}{\textwidth}{l*{6}{>{\centering\arraybackslash}X}}
\toprule
 & \% Black & \% Black & Count Black & Count Black & Any Black & Any Black \\
 &  (1) & (2) & (3) & (4) & (5) & (6)  \\
\midrule
Treatment  &  3.048$^{**}$ & 2.333$^{*}$ & 0.643$^{*}$ & 0.575$^{**}$ & 0.291$^{**}$ & 0.286$^{**}$  \\
 &  (1.148) & (0.916) & (0.254) & (0.208) & (0.100) & (0.097)  \\
Constant  &  7.745$^{**}$ & 8.148$^{}$ & 0.744$^{**}$ & 0.196$^{}$ & 0.657$^{**}$ & 0.963$^{*}$  \\
 &  (2.544) & (5.230) & (0.244) & (1.971) & (0.197) & (0.400)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  82 & 82 & 82 & 82 & 82 & 82  \\
Adjusted $R^2$ &  0.073 & 0.106 & 0.052 & 0.110 & 0.070 & 0.139  \\
\bottomrule
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize \vspace{2pt}Clustered standard errors at department level in parentheses.}}\\
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize $^{+}p<0.1$; $^{*}p<0.05$; $^{**}p<0.01$; $^{***}p<0.001$\vspace{2pt}}}\\
\end{tabularx}
\end{table}
\begin{table}[H]
\caption{Mechanical Engineering : Effect on Hispanic Speaker Representation}
\label{tab:discipline_mechanical_engineering_hispanic}
\centering
\scriptsize
\begin{tabularx}{\textwidth}{l*{6}{>{\centering\arraybackslash}X}}
\toprule
 & \% Hispanic & \% Hispanic & Count Hispanic & Count Hispanic & Any Hispanic & Any Hispanic \\
 &  (1) & (2) & (3) & (4) & (5) & (6)  \\
\midrule
Treatment  &  0.001$^{}$ & 0.532$^{}$ & 0.072$^{}$ & 0.274$^{}$ & -0.050$^{}$ & -0.016$^{}$  \\
 &  (1.872) & (1.855) & (0.227) & (0.244) & (0.122) & (0.130)  \\
Constant  &  6.992$^{}$ & -2.849$^{}$ & 1.300$^{}$ & 2.043$^{}$ & 0.495$^{+}$ & 0.059$^{}$  \\
 &  (4.310) & (9.815) & (0.839) & (1.318) & (0.274) & (0.552)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  82 & 82 & 82 & 82 & 82 & 82  \\
Adjusted $R^2$ &  -0.072 & -0.098 & -0.027 & 0.022 & -0.018 & -0.012  \\
\bottomrule
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize \vspace{2pt}Clustered standard errors at department level in parentheses.}}\\
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize $^{+}p<0.1$; $^{*}p<0.05$; $^{**}p<0.01$; $^{***}p<0.001$\vspace{2pt}}}\\
\end{tabularx}
\end{table}

\newpage

# Semester-Specific Analysis

## Fall Semester

\begin{table}[H]
\caption{Fall: Effect on URM Speakers}
\label{tab:fall_urm}
\centering
\scriptsize
\begin{tabularx}{\textwidth}{l*{6}{>{\centering\arraybackslash}X}}
\toprule
 & \% URM & \% URM & Count URM & Count URM & Any URM & Any URM \\
 &  (1) & (2) & (3) & (4) & (5) & (6)  \\
\midrule
Treatment  &  1.178$^{+}$ & 1.063$^{}$ & 0.103$^{*}$ & 0.079$^{+}$ & 0.045$^{+}$ & 0.035$^{}$  \\
 &  (0.705) & (0.686) & (0.047) & (0.046) & (0.025) & (0.025)  \\
Constant  &  5.830$^{*}$ & -2.421$^{}$ & 0.517$^{***}$ & -0.214$^{}$ & 0.352$^{***}$ & -0.016$^{}$  \\
 &  (2.451) & (2.956) & (0.145) & (0.198) & (0.070) & (0.102)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,448 & 1,448 & 1,448 & 1,448 & 1,448 & 1,448  \\
Adjusted $R^2$ &  0.018 & 0.026 & 0.026 & 0.041 & 0.032 & 0.042  \\
\bottomrule
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize \vspace{2pt}Clustered standard errors at department level in parentheses.}}\\
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize $^{+}p<0.1$; $^{*}p<0.05$; $^{**}p<0.01$; $^{***}p<0.001$\vspace{2pt}}}\\
\end{tabularx}
\end{table}
\begin{table}[H]
\caption{Fall: Effect on Black Speakers}
\label{tab:fall_black}
\centering
\scriptsize
\begin{tabularx}{\textwidth}{l*{6}{>{\centering\arraybackslash}X}}
\toprule
 & \% Black & \% Black & Count Black & Count Black & Any Black & Any Black \\
 &  (1) & (2) & (3) & (4) & (5) & (6)  \\
\midrule
Treatment  &  0.406$^{}$ & 0.371$^{}$ & 0.048$^{*}$ & 0.045$^{*}$ & 0.037$^{*}$ & 0.034$^{*}$  \\
 &  (0.336) & (0.334) & (0.021) & (0.021) & (0.017) & (0.017)  \\
Constant  &  2.704$^{**}$ & -1.560$^{}$ & 0.207$^{***}$ & -0.059$^{}$ & 0.155$^{***}$ & -0.059$^{}$  \\
 &  (0.983) & (1.371) & (0.060) & (0.090) & (0.046) & (0.076)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,448 & 1,448 & 1,448 & 1,448 & 1,448 & 1,448  \\
Adjusted $R^2$ &  0.024 & 0.038 & 0.037 & 0.048 & 0.035 & 0.043  \\
\bottomrule
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize \vspace{2pt}Clustered standard errors at department level in parentheses.}}\\
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize $^{+}p<0.1$; $^{*}p<0.05$; $^{**}p<0.01$; $^{***}p<0.001$\vspace{2pt}}}\\
\end{tabularx}
\end{table}
\begin{table}[H]
\caption{Fall: Effect on Hispanic Speakers}
\label{tab:fall_hispanic}
\centering
\scriptsize
\begin{tabularx}{\textwidth}{l*{6}{>{\centering\arraybackslash}X}}
\toprule
 & \% Hispanic & \% Hispanic & Count Hispanic & Count Hispanic & Any Hispanic & Any Hispanic \\
 &  (1) & (2) & (3) & (4) & (5) & (6)  \\
\midrule
Treatment  &  0.754$^{}$ & 0.666$^{}$ & 0.054$^{}$ & 0.032$^{}$ & 0.028$^{}$ & 0.018$^{}$  \\
 &  (0.648) & (0.650) & (0.040) & (0.040) & (0.025) & (0.025)  \\
Constant  &  2.983$^{}$ & -1.013$^{}$ & 0.297$^{*}$ & -0.170$^{}$ & 0.225$^{**}$ & -0.018$^{}$  \\
 &  (2.370) & (2.900) & (0.134) & (0.181) & (0.074) & (0.106)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,448 & 1,448 & 1,448 & 1,448 & 1,448 & 1,448  \\
Adjusted $R^2$ &  0.012 & 0.011 & 0.021 & 0.030 & 0.023 & 0.027  \\
\bottomrule
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize \vspace{2pt}Clustered standard errors at department level in parentheses.}}\\
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize $^{+}p<0.1$; $^{*}p<0.05$; $^{**}p<0.01$; $^{***}p<0.001$\vspace{2pt}}}\\
\end{tabularx}
\end{table}

## Spring Semester

\begin{table}[H]
\caption{Spring: Effect on URM Speakers}
\label{tab:spring_urm}
\centering
\scriptsize
\begin{tabularx}{\textwidth}{l*{6}{>{\centering\arraybackslash}X}}
\toprule
 & \% URM & \% URM & Count URM & Count URM & Any URM & Any URM \\
 &  (1) & (2) & (3) & (4) & (5) & (6)  \\
\midrule
Treatment  &  0.278$^{}$ & 0.429$^{}$ & -0.018$^{}$ & -0.014$^{}$ & -0.027$^{}$ & -0.023$^{}$  \\
 &  (0.769) & (0.771) & (0.058) & (0.058) & (0.027) & (0.027)  \\
Constant  &  9.229$^{***}$ & 9.567$^{**}$ & 1.113$^{***}$ & 0.952$^{***}$ & 0.603$^{***}$ & 0.495$^{***}$  \\
 &  (1.907) & (2.954) & (0.166) & (0.251) & (0.063) & (0.105)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,397 & 1,397 & 1,397 & 1,397 & 1,397 & 1,397  \\
Adjusted $R^2$ &  0.001 & 0.002 & 0.020 & 0.017 & 0.024 & 0.026  \\
\bottomrule
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize \vspace{2pt}Clustered standard errors at department level in parentheses.}}\\
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize $^{+}p<0.1$; $^{*}p<0.05$; $^{**}p<0.01$; $^{***}p<0.001$\vspace{2pt}}}\\
\end{tabularx}
\end{table}
\begin{table}[H]
\caption{Spring: Effect on Black Speakers}
\label{tab:spring_black}
\centering
\scriptsize
\begin{tabularx}{\textwidth}{l*{6}{>{\centering\arraybackslash}X}}
\toprule
 & \% Black & \% Black & Count Black & Count Black & Any Black & Any Black \\
 &  (1) & (2) & (3) & (4) & (5) & (6)  \\
\midrule
Treatment  &  0.679$^{}$ & 0.657$^{}$ & 0.024$^{}$ & 0.023$^{}$ & 0.012$^{}$ & 0.013$^{}$  \\
 &  (0.465) & (0.448) & (0.037) & (0.036) & (0.023) & (0.022)  \\
Constant  &  2.412$^{*}$ & 1.184$^{}$ & 0.370$^{***}$ & 0.263$^{+}$ & 0.264$^{***}$ & 0.172$^{+}$  \\
 &  (1.074) & (1.688) & (0.099) & (0.147) & (0.064) & (0.102)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,397 & 1,397 & 1,397 & 1,397 & 1,397 & 1,397  \\
Adjusted $R^2$ &  0.010 & 0.011 & 0.031 & 0.036 & 0.024 & 0.027  \\
\bottomrule
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize \vspace{2pt}Clustered standard errors at department level in parentheses.}}\\
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize $^{+}p<0.1$; $^{*}p<0.05$; $^{**}p<0.01$; $^{***}p<0.001$\vspace{2pt}}}\\
\end{tabularx}
\end{table}
\begin{table}[H]
\caption{Spring: Effect on Hispanic Speakers}
\label{tab:spring_hispanic}
\centering
\scriptsize
\begin{tabularx}{\textwidth}{l*{6}{>{\centering\arraybackslash}X}}
\toprule
 & \% Hispanic & \% Hispanic & Count Hispanic & Count Hispanic & Any Hispanic & Any Hispanic \\
 &  (1) & (2) & (3) & (4) & (5) & (6)  \\
\midrule
Treatment  &  -0.379$^{}$ & -0.208$^{}$ & -0.041$^{}$ & -0.036$^{}$ & -0.035$^{}$ & -0.031$^{}$  \\
 &  (0.647) & (0.659) & (0.042) & (0.042) & (0.026) & (0.026)  \\
Constant  &  6.599$^{***}$ & 8.224$^{**}$ & 0.725$^{***}$ & 0.674$^{***}$ & 0.482$^{***}$ & 0.400$^{***}$  \\
 &  (1.670) & (2.690) & (0.127) & (0.193) & (0.066) & (0.100)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,397 & 1,397 & 1,397 & 1,397 & 1,397 & 1,397  \\
Adjusted $R^2$ &  -0.005 & -0.003 & 0.009 & 0.009 & 0.019 & 0.021  \\
\bottomrule
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize \vspace{2pt}Clustered standard errors at department level in parentheses.}}\\
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize $^{+}p<0.1$; $^{*}p<0.05$; $^{**}p<0.01$; $^{***}p<0.001$\vspace{2pt}}}\\
\end{tabularx}
\end{table}

\newpage

# Heterogeneity Analysis

## Moderation by Department Ranking

\begin{table}[H]
\caption{Effect by Department Rank}
\label{tab:mod_ranking}
\centering
\scriptsize
\begin{tabularx}{\textwidth}{l*{6}{>{\centering\arraybackslash}X}}
\toprule
 & \% URM & \% URM & Count URM & Count URM & Any URM & Any URM \\
 &  (1) & (2) & (3) & (4) & (5) & (6)  \\
\midrule
Treatment  &  0.616$^{}$ & 0.649$^{}$ & 0.091$^{}$ & 0.066$^{}$ & 0.011$^{}$ & 0.006$^{}$  \\
 &  (0.532) & (0.532) & (0.069) & (0.067) & (0.025) & (0.023)  \\
Constant  &  9.582$^{***}$ & 5.889$^{**}$ & 1.189$^{***}$ & 0.422$^{+}$ & 0.573$^{***}$ & 0.287$^{**}$  \\
 &  (1.618) & (1.828) & (0.186) & (0.244) & (0.069) & (0.094)  \\
Dept Ranking (centered)  &  0.015$^{}$ & 0.028$^{*}$ & -0.003$^{*}$ & -0.001$^{}$ & -0.001$^{*}$ & -0.001$^{}$  \\
 &  (0.013) & (0.014) & (0.001) & (0.002) & (0.001) & (0.001)  \\
Treatment $\times$ Dept Ranking (centered)  &  0.006$^{}$ & 0.003$^{}$ & 0.004$^{+}$ & 0.004$^{*}$ & 0.001$^{}$ & 0.001$^{}$  \\
 &  (0.017) & (0.017) & (0.002) & (0.002) & (0.001) & (0.001)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,656 & 1,656 & 1,656 & 1,656 & 1,656 & 1,656  \\
Adjusted $R^2$ &  0.011 & 0.015 & 0.028 & 0.037 & 0.035 & 0.047  \\
\bottomrule
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize \vspace{2pt}Clustered standard errors at department level in parentheses.}}\\
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize $^{+}p<0.1$; $^{*}p<0.05$; $^{**}p<0.01$; $^{***}p<0.001$\vspace{2pt}}}\\
\end{tabularx}
\end{table}

\newpage

## Moderation by Total Faculty Size

\begin{table}[H]
\caption{Effect by Faculty Size}
\label{tab:mod_faculty_size}
\centering
\scriptsize
\begin{tabularx}{\textwidth}{l*{6}{>{\centering\arraybackslash}X}}
\toprule
 & \% URM & \% URM & Count URM & Count URM & Any URM & Any URM \\
 &  (1) & (2) & (3) & (4) & (5) & (6)  \\
\midrule
Treatment  &  0.804$^{}$ & 0.653$^{}$ & 0.072$^{}$ & 0.065$^{}$ & 0.004$^{}$ & 0.007$^{}$  \\
 &  (0.555) & (0.535) & (0.072) & (0.068) & (0.025) & (0.024)  \\
Constant  &  8.520$^{***}$ & 3.367$^{}$ & 1.268$^{***}$ & 0.354$^{}$ & 0.628$^{***}$ & 0.269$^{**}$  \\
 &  (1.545) & (2.054) & (0.184) & (0.290) & (0.065) & (0.102)  \\
Total Faculty (centered)  &  -0.023$^{}$ & -0.027$^{}$ & 0.003$^{}$ & 0.001$^{}$ & 0.001$^{}$ & -0.001$^{}$  \\
 &  (0.023) & (0.023) & (0.003) & (0.003) & (0.001) & (0.001)  \\
Treatment $\times$ Total Faculty (centered)  &  0.009$^{}$ & 0.001$^{}$ & -0.002$^{}$ & -0.003$^{}$ & 0.000$^{}$ & -0.000$^{}$  \\
 &  (0.027) & (0.027) & (0.003) & (0.003) & (0.001) & (0.001)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,656 & 1,656 & 1,656 & 1,656 & 1,656 & 1,656  \\
Adjusted $R^2$ &  0.010 & 0.015 & 0.026 & 0.034 & 0.031 & 0.046  \\
\bottomrule
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize \vspace{2pt}Clustered standard errors at department level in parentheses.}}\\
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize $^{+}p<0.1$; $^{*}p<0.05$; $^{**}p<0.01$; $^{***}p<0.001$\vspace{2pt}}}\\
\end{tabularx}
\end{table}

\newpage

## Moderation by URM Faculty in Peer Departments

\begin{table}[H]
\caption{Effect by Peer URM Faculty}
\label{tab:mod_peer_urm}
\centering
\scriptsize
\begin{tabularx}{\textwidth}{l*{6}{>{\centering\arraybackslash}X}}
\toprule
 & \% URM & \% URM & Count URM & Count URM & Any URM & Any URM \\
 &  (1) & (2) & (3) & (4) & (5) & (6)  \\
\midrule
Treatment  &  0.663$^{}$ & 0.637$^{}$ & 0.094$^{}$ & 0.069$^{}$ & 0.011$^{}$ & 0.007$^{}$  \\
 &  (0.533) & (0.533) & (0.068) & (0.068) & (0.024) & (0.023)  \\
Constant  &  8.350$^{***}$ & 8.073$^{***}$ & 1.205$^{***}$ & 0.965$^{***}$ & 0.615$^{***}$ & 0.514$^{***}$  \\
 &  (1.505) & (1.534) & (0.173) & (0.205) & (0.060) & (0.078)  \\
Peer URM Faculty (centered)  &  0.077$^{}$ & 0.141$^{*}$ & 0.017$^{**}$ & 0.019$^{**}$ & 0.007$^{**}$ & 0.007$^{**}$  \\
 &  (0.055) & (0.056) & (0.006) & (0.006) & (0.002) & (0.002)  \\
Treatment $\times$ Peer URM Faculty (centered)  &  -0.075$^{}$ & -0.055$^{}$ & -0.003$^{}$ & -0.002$^{}$ & -0.001$^{}$ & -0.001$^{}$  \\
 &  (0.075) & (0.074) & (0.008) & (0.008) & (0.003) & (0.003)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,656 & 1,656 & 1,656 & 1,656 & 1,656 & 1,656  \\
Adjusted $R^2$ &  0.011 & 0.015 & 0.032 & 0.034 & 0.041 & 0.046  \\
\bottomrule
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize \vspace{2pt}Clustered standard errors at department level in parentheses.}}\\
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize $^{+}p<0.1$; $^{*}p<0.05$; $^{**}p<0.01$; $^{***}p<0.001$\vspace{2pt}}}\\
\end{tabularx}
\end{table}


\clearpage
\section{Summary of All Significant Results}

\begin{table}[H]
\caption{All Significant Results (p < 0.1) from All Analyses (Excluding Constant Term)}
\label{tab:all_significant_results}
\centering
{\scriptsize % Start group for scriptsize and tabcolsep
\setlength{\tabcolsep}{2pt} % Reduce column separation further
\begin{tabular}{p{3.2cm} p{2.3cm} p{2.3cm} l r r r r l}
\toprule
Analysis & Outcome & Variable & Model & Coef. & SE & t-stat & p-value & Sig. \\
\midrule
\multicolumn{9}{l}{\textbf{Discipline Analysis}} \\
\midrule
Computer Science & \% URM & Treatment & Simple & 2.2852 & 1.3775 & 1.659 & 0.0996 & + \\
Computer Science & Any Hispanic & Treatment & Extended & 0.1563 & 0.0832 & 1.880 & 0.0626 & + \\
Mathematics & \% URM & Treatment & Extended & 1.4978 & 0.8526 & 1.757 & 0.0793 & + \\
Mathematics & Count Black & Treatment & Extended & 0.1004 & 0.0580 & 1.731 & 0.0838 & + \\
Mechanical Engineering & \% Black & Treatment & Simple & 3.0477 & 1.1484 & 2.654 & 0.0100 & ** \\
Mechanical Engineering & Any Black & Treatment & Extended & 0.2857 & 0.0972 & 2.940 & 0.0047 & ** \\
Mechanical Engineering & Count Black & Treatment & Extended & 0.5753 & 0.2079 & 2.767 & 0.0076 & ** \\
Mechanical Engineering & Count URM & Treatment & Extended & 0.8489 & 0.3682 & 2.306 & 0.0248 & * \\
Physics & \% Black & Treatment & Extended & 1.3070 & 0.6361 & 2.055 & 0.0407 & * \\
Physics & Any Black & Treatment & Extended & 0.1201 & 0.0507 & 2.371 & 0.0183 & * \\
Physics & Count Black & Treatment & Extended & 0.1655 & 0.0686 & 2.413 & 0.0164 & * \\
\addlinespace[0.5em]
\multicolumn{9}{l}{\textbf{Identity Analysis}} \\
\midrule
Demographic Subgroup & \% Black & Treatment & Simple & 0.5612 & 0.3127 & 1.794 & 0.0729 & + \\
Demographic Subgroup & \% Black Male & Treatment & Simple & 0.4635 & 0.2665 & 1.739 & 0.0823 & + \\
Demographic Subgroup & Any Black & Treatment & Extended & 0.0415 & 0.0224 & 1.851 & 0.0643 & + \\
Demographic Subgroup & Any Black Male & Treatment & Extended & 0.0472 & 0.0221 & 2.134 & 0.0330 & * \\
Demographic Subgroup & Count Black Male & Treatment & Simple & 0.0647 & 0.0357 & 1.811 & 0.0703 & + \\
\addlinespace[0.5em]
\multicolumn{9}{l}{\textbf{Moderation Analysis}} \\
\midrule
Department Rank & Count URM & Treatment $\times$ Dept Ranking & Extended & 0.0039 & 0.0019 & 2.038 & 0.0417 & * \\
\addlinespace[0.5em]
\multicolumn{9}{l}{\textbf{Semester Analysis}} \\
\midrule
Fall Semester & \% URM & Treatment & Simple & 1.1775 & 0.7049 & 1.671 & 0.0950 & + \\
Fall Semester & Any Black & Treatment & Simple & 0.0366 & 0.0171 & 2.139 & 0.0326 & * \\
Fall Semester & Any URM & Treatment & Simple & 0.0448 & 0.0254 & 1.765 & 0.0778 & + \\
Fall Semester & Count Black & Treatment & Simple & 0.0478 & 0.0214 & 2.235 & 0.0256 & * \\
Fall Semester & Count URM & Treatment & Simple & 0.1031 & 0.0468 & 2.202 & 0.0278 & * \\
\bottomrule
\end{tabular}
} % End group for scriptsize and tabcolsep
\parbox{\linewidth}{\footnotesize Note: Significance levels: + p<0.1; * p<0.05; ** p<0.01; *** p<0.001. SE = Clustered standard errors at department level. Constant terms are excluded from this summary.}
\end{table}
