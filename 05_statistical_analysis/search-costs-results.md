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
URM & 7.81 & 11.37 & 1.07 & 1.34 & 55.7 \\
Black & 2.24 & 5.90 & 0.32 & 0.67 & 23.9 \\
Hispanic & 5.55 & 9.70 & 0.75 & 1.09 & 45.2 \\
Female & 16.87 & 16.25 & 2.39 & 2.52 & 75.5 \\
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
Chemistry & 271 & 9.13 & 10.47 & 1.32 & 65.3 \\
Computer Science & 142 & 4.86 & 9.01 & 0.61 & 38.0 \\
Mathematics & 811 & 7.37 & 11.02 & 1.00 & 51.3 \\
Mechanical Engineering & 82 & 8.38 & 9.14 & 1.12 & 63.4 \\
Physics & 350 & 8.87 & 13.70 & 1.23 & 64.0 \\
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
Chemistry & 4.20 & 40.2 & 4.83 & 47.6 & 23.75 & 86.3 \\
Computer Science & 1.46 & 16.9 & 3.41 & 27.5 & 18.88 & 78.9 \\
Mathematics & 1.72 & 19.2 & 5.64 & 43.5 & 13.90 & 69.5 \\
Mechanical Engineering & 3.28 & 32.9 & 5.10 & 46.3 & 19.25 & 76.8 \\
Physics & 1.98 & 22.9 & 6.89 & 54.0 & 17.06 & 79.1 \\
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
Fall (1448) & 7.44 & 0.57 & 38.5 & 1.74 & 11.9 & 5.68 & 31.0 \\
Spring (1397) & 7.99 & 0.68 & 43.1 & 2.66 & 18.3 & 5.30 & 31.9 \\
\midrule
 & \multicolumn{3}{c}{Female} & \multicolumn{2}{c}{Total Speakers} & & \\
Semester & Mean \% & Mean Count & Pct. Any & Mean & SD & & \\
\midrule
Fall & 16.09 & 1.27 & 61.8 & 7.75 & 5.50 & & \\
Spring & 17.69 & 1.52 & 63.7 & 8.56 & 6.92 & & \\
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
Treatment  &  0.743$^{}$ & 0.734$^{}$ & 0.093$^{}$ & 0.070$^{}$ & 0.014$^{}$ & 0.011$^{}$  \\
 &  (0.535) & (0.530) & (0.069) & (0.068) & (0.025) & (0.024)  \\
Constant  &  8.189$^{***}$ & 4.213$^{*}$ & 1.252$^{***}$ & 0.354$^{}$ & 0.609$^{***}$ & 0.291$^{**}$  \\
 &  (1.622) & (2.007) & (0.180) & (0.272) & (0.069) & (0.106)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,656 & 1,656 & 1,656 & 1,656 & 1,656 & 1,656  \\
Adjusted $R^2$ &  0.011 & 0.015 & 0.026 & 0.035 & 0.031 & 0.045  \\
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
Treatment  &  -0.461$^{}$ & -0.502$^{}$ & 0.093$^{}$ & 0.070$^{}$ & -0.535$^{}$ & -0.556$^{}$  \\
 &  (0.554) & (0.542) & (0.069) & (0.068) & (0.523) & (0.511)  \\
Constant  &  16.810$^{***}$ & 12.854$^{***}$ & 1.252$^{***}$ & 0.354$^{}$ & 15.523$^{***}$ & 12.435$^{***}$  \\
 &  (1.313) & (2.276) & (0.180) & (0.272) & (1.239) & (2.133)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,656 & 1,656 & 1,656 & 1,656 & 1,656 & 1,656  \\
Adjusted $R^2$ &  0.031 & 0.058 & 0.026 & 0.035 & 0.030 & 0.057  \\
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
URM Speakers & 0.0928 & (0.0663) \\
Non-URM Speakers & -0.5352 & (0.4576) \\
\midrule
Sum of Effects & -0.4424 & --- \\
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
Treatment  &  0.587$^{+}$ & 0.554$^{+}$ & 0.067$^{+}$ & 0.062$^{}$ & 0.045$^{+}$ & 0.045$^{*}$  \\
 &  (0.308) & (0.293) & (0.040) & (0.038) & (0.023) & (0.022)  \\
Constant  &  2.605$^{**}$ & 0.303$^{}$ & 0.450$^{***}$ & 0.097$^{}$ & 0.285$^{***}$ & 0.056$^{}$  \\
 &  (0.831) & (1.286) & (0.112) & (0.161) & (0.067) & (0.104)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,656 & 1,656 & 1,656 & 1,656 & 1,656 & 1,656  \\
Adjusted $R^2$ &  0.027 & 0.034 & 0.049 & 0.058 & 0.042 & 0.051  \\
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
Treatment  &  0.175$^{}$ & 0.198$^{}$ & 0.027$^{}$ & 0.008$^{}$ & -0.007$^{}$ & -0.010$^{}$  \\
 &  (0.461) & (0.469) & (0.052) & (0.052) & (0.025) & (0.025)  \\
Constant  &  5.384$^{***}$ & 3.766$^{*}$ & 0.779$^{***}$ & 0.236$^{}$ & 0.491$^{***}$ & 0.291$^{**}$  \\
 &  (1.471) & (1.777) & (0.153) & (0.218) & (0.069) & (0.104)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,656 & 1,656 & 1,656 & 1,656 & 1,656 & 1,656  \\
Adjusted $R^2$ &  0.006 & 0.005 & 0.013 & 0.020 & 0.018 & 0.021  \\
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
Treatment  &  0.055$^{}$ & -0.251$^{}$ & -0.071$^{}$ & -0.137$^{}$ & -0.009$^{}$ & -0.012$^{}$  \\
 &  (0.828) & (0.829) & (0.129) & (0.125) & (0.021) & (0.021)  \\
Constant  &  21.840$^{***}$ & 16.463$^{***}$ & 3.595$^{***}$ & 2.394$^{***}$ & 0.854$^{***}$ & 0.693$^{***}$  \\
 &  (2.006) & (3.794) & (0.343) & (0.576) & (0.058) & (0.090)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,656 & 1,656 & 1,656 & 1,656 & 1,656 & 1,656  \\
Adjusted $R^2$ &  0.051 & 0.057 & 0.088 & 0.106 & 0.018 & 0.028  \\
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
Treatment  &  -0.052$^{}$ & -0.095$^{}$ & 0.014$^{}$ & 0.005$^{}$ & 0.011$^{}$ & 0.002$^{}$  \\
 &  (0.174) & (0.188) & (0.019) & (0.019) & (0.017) & (0.017)  \\
Constant  &  1.814$^{**}$ & 0.193$^{}$ & 0.218$^{***}$ & -0.020$^{}$ & 0.190$^{***}$ & -0.033$^{}$  \\
 &  (0.614) & (0.607) & (0.062) & (0.089) & (0.052) & (0.076)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,656 & 1,656 & 1,656 & 1,656 & 1,656 & 1,656  \\
Adjusted $R^2$ &  0.014 & 0.019 & 0.042 & 0.060 & 0.045 & 0.062  \\
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
Treatment  &  0.098$^{}$ & 0.102$^{}$ & 0.001$^{}$ & 0.001$^{}$ & 0.003$^{}$ & 0.003$^{}$  \\
 &  (0.072) & (0.073) & (0.010) & (0.010) & (0.009) & (0.009)  \\
Constant  &  0.571$^{***}$ & 0.101$^{}$ & 0.087$^{**}$ & 0.037$^{}$ & 0.074$^{**}$ & 0.035$^{}$  \\
 &  (0.173) & (0.282) & (0.027) & (0.042) & (0.024) & (0.037)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,656 & 1,656 & 1,656 & 1,656 & 1,656 & 1,656  \\
Adjusted $R^2$ &  0.030 & 0.034 & 0.025 & 0.029 & 0.020 & 0.025  \\
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
Treatment  &  0.489$^{+}$ & 0.451$^{+}$ & 0.065$^{+}$ & 0.061$^{+}$ & 0.051$^{*}$ & 0.050$^{*}$  \\
 &  (0.263) & (0.248) & (0.034) & (0.032) & (0.023) & (0.022)  \\
Constant  &  2.034$^{**}$ & 0.202$^{}$ & 0.356$^{***}$ & 0.059$^{}$ & 0.269$^{***}$ & 0.031$^{}$  \\
 &  (0.725) & (1.152) & (0.094) & (0.135) & (0.066) & (0.103)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,656 & 1,656 & 1,656 & 1,656 & 1,656 & 1,656  \\
Adjusted $R^2$ &  0.019 & 0.024 & 0.041 & 0.049 & 0.039 & 0.048  \\
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
Treatment  &  -0.152$^{}$ & -0.200$^{}$ & 0.000$^{}$ & -0.008$^{}$ & -0.001$^{}$ & -0.009$^{}$  \\
 &  (0.162) & (0.179) & (0.013) & (0.013) & (0.012) & (0.012)  \\
Constant  &  1.224$^{*}$ & 0.070$^{}$ & 0.073$^{}$ & -0.036$^{}$ & 0.068$^{+}$ & -0.035$^{}$  \\
 &  (0.589) & (0.509) & (0.045) & (0.064) & (0.036) & (0.056)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,656 & 1,656 & 1,656 & 1,656 & 1,656 & 1,656  \\
Adjusted $R^2$ &  0.001 & 0.003 & 0.004 & 0.016 & 0.004 & 0.016  \\
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
Treatment  &  0.327$^{}$ & 0.399$^{}$ & 0.025$^{}$ & 0.015$^{}$ & -0.006$^{}$ & -0.009$^{}$  \\
 &  (0.389) & (0.388) & (0.047) & (0.046) & (0.025) & (0.025)  \\
Constant  &  4.160$^{**}$ & 3.696$^{*}$ & 0.705$^{***}$ & 0.273$^{}$ & 0.484$^{***}$ & 0.283$^{**}$  \\
 &  (1.278) & (1.552) & (0.134) & (0.188) & (0.069) & (0.103)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,656 & 1,656 & 1,656 & 1,656 & 1,656 & 1,656  \\
Adjusted $R^2$ &  0.010 & 0.008 & 0.014 & 0.020 & 0.019 & 0.022  \\
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
Treatment  &  0.550$^{}$ & -0.449$^{}$ & -0.135$^{}$ & -0.205$^{}$ & 0.043$^{}$ & 0.020$^{}$  \\
 &  (1.198) & (1.224) & (0.169) & (0.176) & (0.054) & (0.059)  \\
Constant  &  4.407$^{}$ & -0.574$^{}$ & 0.789$^{+}$ & -0.527$^{}$ & 0.094$^{}$ & -0.230$^{}$  \\
 &  (2.964) & (5.429) & (0.427) & (0.708) & (0.135) & (0.264)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  271 & 271 & 271 & 271 & 271 & 271  \\
Adjusted $R^2$ &  -0.023 & -0.015 & 0.109 & 0.113 & 0.093 & 0.093  \\
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
Treatment  &  0.655$^{}$ & 0.208$^{}$ & -0.015$^{}$ & -0.016$^{}$ & 0.071$^{}$ & 0.038$^{}$  \\
 &  (1.047) & (0.914) & (0.121) & (0.111) & (0.067) & (0.068)  \\
Constant  &  1.379$^{}$ & -9.402$^{*}$ & 0.329$^{}$ & -1.328$^{**}$ & 0.105$^{}$ & -0.791$^{*}$  \\
 &  (2.636) & (3.875) & (0.247) & (0.498) & (0.162) & (0.306)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  271 & 271 & 271 & 271 & 271 & 271  \\
Adjusted $R^2$ &  -0.026 & 0.005 & 0.061 & 0.105 & 0.071 & 0.128  \\
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
Treatment  &  -0.013$^{}$ & -0.565$^{}$ & -0.127$^{}$ & -0.199$^{}$ & -0.075$^{}$ & -0.099$^{}$  \\
 &  (1.006) & (1.034) & (0.123) & (0.142) & (0.062) & (0.064)  \\
Constant  &  2.177$^{}$ & 7.127$^{+}$ & 0.424$^{}$ & 0.645$^{}$ & 0.138$^{}$ & 0.295$^{}$  \\
 &  (1.836) & (3.850) & (0.367) & (0.523) & (0.154) & (0.272)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  271 & 271 & 271 & 271 & 271 & 271  \\
Adjusted $R^2$ &  -0.020 & -0.020 & 0.048 & 0.067 & 0.025 & 0.037  \\
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
Treatment  &  1.183$^{+}$ & 1.495$^{+}$ & 0.151$^{}$ & 0.148$^{}$ & 0.024$^{}$ & 0.014$^{}$  \\
 &  (0.695) & (0.836) & (0.098) & (0.116) & (0.032) & (0.032)  \\
Constant  &  5.650$^{***}$ & 3.396$^{}$ & 0.962$^{***}$ & 0.021$^{}$ & 0.505$^{***}$ & 0.146$^{}$  \\
 &  (1.270) & (4.326) & (0.150) & (0.570) & (0.065) & (0.191)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  811 & 811 & 811 & 811 & 811 & 811  \\
Adjusted $R^2$ &  0.006 & 0.003 & 0.000 & 0.001 & -0.006 & 0.004  \\
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
Treatment  &  0.252$^{}$ & 0.496$^{}$ & 0.064$^{}$ & 0.100$^{+}$ & 0.006$^{}$ & 0.013$^{}$  \\
 &  (0.370) & (0.433) & (0.050) & (0.058) & (0.029) & (0.027)  \\
Constant  &  0.481$^{}$ & 0.972$^{}$ & 0.187$^{**}$ & 0.387$^{}$ & 0.151$^{**}$ & 0.076$^{}$  \\
 &  (0.484) & (2.345) & (0.070) & (0.267) & (0.048) & (0.148)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  811 & 811 & 811 & 811 & 811 & 811  \\
Adjusted $R^2$ &  0.025 & 0.038 & 0.013 & 0.028 & 0.010 & 0.027  \\
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
Treatment  &  0.950$^{}$ & 1.005$^{}$ & 0.091$^{}$ & 0.049$^{}$ & 0.041$^{}$ & 0.035$^{}$  \\
 &  (0.617) & (0.687) & (0.078) & (0.081) & (0.034) & (0.035)  \\
Constant  &  5.094$^{***}$ & 2.276$^{}$ & 0.756$^{***}$ & -0.401$^{}$ & 0.441$^{***}$ & 0.209$^{}$  \\
 &  (1.236) & (3.224) & (0.139) & (0.445) & (0.073) & (0.204)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  811 & 811 & 811 & 811 & 811 & 811  \\
Adjusted $R^2$ &  -0.004 & -0.005 & -0.004 & 0.002 & -0.003 & -0.002  \\
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
Treatment  &  0.195$^{}$ & 0.344$^{}$ & 0.211$^{}$ & 0.236$^{+}$ & -0.004$^{}$ & 0.010$^{}$  \\
 &  (1.281) & (1.185) & (0.142) & (0.141) & (0.061) & (0.056)  \\
Constant  &  14.623$^{***}$ & 16.403$^{}$ & 1.429$^{***}$ & 3.096$^{*}$ & 0.549$^{***}$ & 1.212$^{*}$  \\
 &  (2.277) & (13.619) & (0.160) & (1.356) & (0.063) & (0.576)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  350 & 350 & 350 & 350 & 350 & 350  \\
Adjusted $R^2$ &  0.002 & -0.007 & 0.002 & 0.009 & 0.003 & 0.033  \\
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
Treatment  &  1.260$^{*}$ & 1.333$^{*}$ & 0.167$^{*}$ & 0.174$^{*}$ & 0.130$^{**}$ & 0.134$^{**}$  \\
 &  (0.627) & (0.633) & (0.068) & (0.068) & (0.049) & (0.050)  \\
Constant  &  0.620$^{}$ & 1.842$^{}$ & 0.068$^{}$ & 0.573$^{}$ & 0.040$^{}$ & 0.322$^{}$  \\
 &  (0.687) & (4.034) & (0.084) & (0.570) & (0.058) & (0.388)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  350 & 350 & 350 & 350 & 350 & 350  \\
Adjusted $R^2$ &  0.003 & 0.001 & 0.013 & 0.009 & 0.010 & 0.021  \\
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
Treatment  &  -1.065$^{}$ & -0.989$^{}$ & 0.043$^{}$ & 0.062$^{}$ & -0.050$^{}$ & -0.039$^{}$  \\
 &  (1.256) & (1.211) & (0.129) & (0.130) & (0.065) & (0.063)  \\
Constant  &  14.003$^{***}$ & 14.560$^{}$ & 1.361$^{***}$ & 2.523$^{*}$ & 0.541$^{***}$ & 1.086$^{+}$  \\
 &  (2.319) & (12.805) & (0.146) & (1.148) & (0.074) & (0.568)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  350 & 350 & 350 & 350 & 350 & 350  \\
Adjusted $R^2$ &  -0.000 & -0.012 & -0.010 & 0.008 & 0.001 & 0.004  \\
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
Treatment  &  2.772$^{}$ & 2.771$^{}$ & 0.599$^{*}$ & 0.809$^{*}$ & 0.037$^{}$ & 0.043$^{}$  \\
 &  (1.979) & (1.876) & (0.295) & (0.349) & (0.111) & (0.127)  \\
Constant  &  14.896$^{*}$ & 7.948$^{}$ & 2.110$^{*}$ & 3.352$^{+}$ & 0.722$^{**}$ & 0.566$^{}$  \\
 &  (5.963) & (9.914) & (0.926) & (1.762) & (0.267) & (0.491)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  82 & 82 & 82 & 82 & 82 & 82  \\
Adjusted $R^2$ &  0.003 & -0.015 & -0.013 & 0.090 & 0.016 & 0.034  \\
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
Treatment  &  2.771$^{*}$ & 2.238$^{*}$ & 0.527$^{**}$ & 0.536$^{**}$ & 0.291$^{**}$ & 0.286$^{**}$  \\
 &  (1.081) & (0.878) & (0.165) & (0.173) & (0.100) & (0.097)  \\
Constant  &  7.904$^{**}$ & 10.798$^{*}$ & 0.810$^{***}$ & 1.309$^{}$ & 0.657$^{**}$ & 0.963$^{*}$  \\
 &  (2.587) & (4.389) & (0.222) & (1.135) & (0.197) & (0.400)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  82 & 82 & 82 & 82 & 82 & 82  \\
Adjusted $R^2$ &  0.065 & 0.088 & 0.079 & 0.135 & 0.070 & 0.139  \\
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
Treatment  &  1.098$^{}$ & 0.977$^{}$ & 0.098$^{*}$ & 0.073$^{}$ & 0.043$^{+}$ & 0.033$^{}$  \\
 &  (0.702) & (0.684) & (0.047) & (0.046) & (0.025) & (0.026)  \\
Constant  &  5.742$^{*}$ & -2.379$^{}$ & 0.515$^{***}$ & -0.205$^{}$ & 0.347$^{***}$ & -0.005$^{}$  \\
 &  (2.441) & (2.941) & (0.144) & (0.198) & (0.070) & (0.102)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,448 & 1,448 & 1,448 & 1,448 & 1,448 & 1,448  \\
Adjusted $R^2$ &  0.017 & 0.025 & 0.026 & 0.041 & 0.029 & 0.038  \\
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
Treatment  &  0.427$^{}$ & 0.397$^{}$ & 0.049$^{*}$ & 0.047$^{*}$ & 0.038$^{*}$ & 0.036$^{*}$  \\
 &  (0.335) & (0.334) & (0.021) & (0.021) & (0.017) & (0.017)  \\
Constant  &  2.565$^{**}$ & -1.427$^{}$ & 0.201$^{***}$ & -0.050$^{}$ & 0.149$^{***}$ & -0.051$^{}$  \\
 &  (0.976) & (1.369) & (0.060) & (0.089) & (0.045) & (0.075)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,448 & 1,448 & 1,448 & 1,448 & 1,448 & 1,448  \\
Adjusted $R^2$ &  0.021 & 0.034 & 0.036 & 0.046 & 0.033 & 0.040  \\
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
Treatment  &  0.668$^{}$ & 0.572$^{}$ & 0.049$^{}$ & 0.026$^{}$ & 0.025$^{}$ & 0.014$^{}$  \\
 &  (0.645) & (0.647) & (0.040) & (0.040) & (0.025) & (0.025)  \\
Constant  &  3.078$^{}$ & -1.066$^{}$ & 0.304$^{*}$ & -0.166$^{}$ & 0.227$^{**}$ & -0.019$^{}$  \\
 &  (2.367) & (2.893) & (0.134) & (0.181) & (0.074) & (0.106)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,448 & 1,448 & 1,448 & 1,448 & 1,448 & 1,448  \\
Adjusted $R^2$ &  0.012 & 0.011 & 0.020 & 0.030 & 0.022 & 0.027  \\
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
Treatment  &  0.426$^{}$ & 0.564$^{}$ & -0.009$^{}$ & -0.007$^{}$ & -0.020$^{}$ & -0.017$^{}$  \\
 &  (0.767) & (0.768) & (0.056) & (0.057) & (0.027) & (0.027)  \\
Constant  &  8.928$^{***}$ & 9.366$^{**}$ & 1.121$^{***}$ & 0.940$^{***}$ & 0.584$^{***}$ & 0.474$^{***}$  \\
 &  (1.960) & (3.009) & (0.157) & (0.249) & (0.068) & (0.109)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,397 & 1,397 & 1,397 & 1,397 & 1,397 & 1,397  \\
Adjusted $R^2$ &  0.001 & 0.001 & 0.019 & 0.016 & 0.023 & 0.025  \\
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
Treatment  &  0.706$^{}$ & 0.680$^{}$ & 0.021$^{}$ & 0.020$^{}$ & 0.014$^{}$ & 0.015$^{}$  \\
 &  (0.458) & (0.438) & (0.035) & (0.034) & (0.023) & (0.022)  \\
Constant  &  2.129$^{*}$ & 0.794$^{}$ & 0.366$^{***}$ & 0.256$^{+}$ & 0.255$^{***}$ & 0.155$^{}$  \\
 &  (1.070) & (1.673) & (0.097) & (0.147) & (0.066) & (0.103)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,397 & 1,397 & 1,397 & 1,397 & 1,397 & 1,397  \\
Adjusted $R^2$ &  0.009 & 0.011 & 0.031 & 0.035 & 0.024 & 0.028  \\
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
Treatment  &  -0.258$^{}$ & -0.095$^{}$ & -0.029$^{}$ & -0.027$^{}$ & -0.033$^{}$ & -0.030$^{}$  \\
 &  (0.644) & (0.654) & (0.042) & (0.042) & (0.026) & (0.026)  \\
Constant  &  6.582$^{***}$ & 8.413$^{**}$ & 0.737$^{***}$ & 0.670$^{***}$ & 0.476$^{***}$ & 0.403$^{***}$  \\
 &  (1.687) & (2.662) & (0.120) & (0.188) & (0.069) & (0.100)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,397 & 1,397 & 1,397 & 1,397 & 1,397 & 1,397  \\
Adjusted $R^2$ &  -0.006 & -0.004 & 0.008 & 0.009 & 0.018 & 0.020  \\
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
Treatment  &  0.704$^{}$ & 0.730$^{}$ & 0.095$^{}$ & 0.067$^{}$ & 0.016$^{}$ & 0.010$^{}$  \\
 &  (0.527) & (0.528) & (0.069) & (0.067) & (0.025) & (0.024)  \\
Constant  &  9.190$^{***}$ & 5.643$^{**}$ & 1.172$^{***}$ & 0.407$^{+}$ & 0.547$^{***}$ & 0.277$^{**}$  \\
 &  (1.636) & (1.876) & (0.190) & (0.245) & (0.074) & (0.099)  \\
Dept Ranking (centered)  &  0.013$^{}$ & 0.026$^{*}$ & -0.003$^{*}$ & -0.001$^{}$ & -0.001$^{*}$ & -0.001$^{}$  \\
 &  (0.013) & (0.013) & (0.001) & (0.001) & (0.001) & (0.001)  \\
Treatment $\times$ Dept Ranking (centered)  &  0.007$^{}$ & 0.004$^{}$ & 0.004$^{+}$ & 0.004$^{*}$ & 0.001$^{}$ & 0.001$^{}$  \\
 &  (0.017) & (0.016) & (0.002) & (0.002) & (0.001) & (0.001)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,656 & 1,656 & 1,656 & 1,656 & 1,656 & 1,656  \\
Adjusted $R^2$ &  0.012 & 0.015 & 0.028 & 0.037 & 0.035 & 0.045  \\
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
Treatment  &  0.878$^{}$ & 0.734$^{}$ & 0.070$^{}$ & 0.066$^{}$ & 0.008$^{}$ & 0.011$^{}$  \\
 &  (0.552) & (0.531) & (0.072) & (0.068) & (0.026) & (0.024)  \\
Constant  &  8.195$^{***}$ & 3.272$^{}$ & 1.263$^{***}$ & 0.375$^{}$ & 0.603$^{***}$ & 0.265$^{*}$  \\
 &  (1.606) & (2.096) & (0.189) & (0.290) & (0.071) & (0.109)  \\
Total Faculty (centered)  &  -0.021$^{}$ & -0.025$^{}$ & 0.004$^{}$ & 0.002$^{}$ & 0.001$^{}$ & -0.001$^{}$  \\
 &  (0.023) & (0.023) & (0.003) & (0.003) & (0.001) & (0.001)  \\
Treatment $\times$ Total Faculty (centered)  &  0.008$^{}$ & 0.000$^{}$ & -0.002$^{}$ & -0.003$^{}$ & 0.000$^{}$ & -0.000$^{}$  \\
 &  (0.027) & (0.026) & (0.003) & (0.003) & (0.001) & (0.001)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,656 & 1,656 & 1,656 & 1,656 & 1,656 & 1,656  \\
Adjusted $R^2$ &  0.011 & 0.015 & 0.026 & 0.035 & 0.031 & 0.045  \\
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
Treatment  &  0.748$^{}$ & 0.718$^{}$ & 0.098$^{}$ & 0.069$^{}$ & 0.016$^{}$ & 0.011$^{}$  \\
 &  (0.528) & (0.528) & (0.068) & (0.067) & (0.024) & (0.024)  \\
Constant  &  8.012$^{***}$ & 7.729$^{***}$ & 1.203$^{***}$ & 0.951$^{***}$ & 0.590$^{***}$ & 0.491$^{***}$  \\
 &  (1.544) & (1.578) & (0.175) & (0.207) & (0.067) & (0.082)  \\
Peer URM Faculty (centered)  &  0.081$^{}$ & 0.141$^{*}$ & 0.018$^{**}$ & 0.020$^{**}$ & 0.007$^{**}$ & 0.007$^{**}$  \\
 &  (0.054) & (0.056) & (0.005) & (0.006) & (0.002) & (0.003)  \\
Treatment $\times$ Peer URM Faculty (centered)  &  -0.083$^{}$ & -0.065$^{}$ & -0.004$^{}$ & -0.003$^{}$ & -0.001$^{}$ & -0.001$^{}$  \\
 &  (0.075) & (0.074) & (0.008) & (0.008) & (0.003) & (0.003)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,656 & 1,656 & 1,656 & 1,656 & 1,656 & 1,656  \\
Adjusted $R^2$ &  0.011 & 0.015 & 0.033 & 0.034 & 0.040 & 0.045  \\
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
Mathematics & \% URM & Treatment & Extended & 1.4949 & 0.8357 & 1.789 & 0.0740 & + \\
Mathematics & Count Black & Treatment & Extended & 0.0998 & 0.0578 & 1.726 & 0.0848 & + \\
Mechanical Engineering & \% Black & Treatment & Simple & 2.7713 & 1.0807 & 2.564 & 0.0127 & * \\
Mechanical Engineering & Any Black & Treatment & Extended & 0.2857 & 0.0972 & 2.940 & 0.0047 & ** \\
Mechanical Engineering & Count Black & Treatment & Simple & 0.5272 & 0.1654 & 3.187 & 0.0022 & ** \\
Mechanical Engineering & Count URM & Treatment & Extended & 0.8092 & 0.3492 & 2.318 & 0.0241 & * \\
Physics & \% Black & Treatment & Extended & 1.3330 & 0.6331 & 2.105 & 0.0360 & * \\
Physics & Any Black & Treatment & Extended & 0.1337 & 0.0504 & 2.652 & 0.0084 & ** \\
Physics & Count Black & Treatment & Extended & 0.1740 & 0.0679 & 2.562 & 0.0108 & * \\
Physics & Count URM & Treatment & Extended & 0.2361 & 0.1406 & 1.680 & 0.0939 & + \\
\addlinespace[0.5em]
\multicolumn{9}{l}{\textbf{Identity Analysis}} \\
\midrule
Demographic Subgroup & \% Black & Treatment & Simple & 0.5871 & 0.3084 & 1.904 & 0.0571 & + \\
Demographic Subgroup & \% Black Male & Treatment & Simple & 0.4891 & 0.2628 & 1.861 & 0.0629 & + \\
Demographic Subgroup & Any Black & Treatment & Extended & 0.0445 & 0.0224 & 1.984 & 0.0475 & * \\
Demographic Subgroup & Any Black Male & Treatment & Extended & 0.0497 & 0.0221 & 2.248 & 0.0247 & * \\
Demographic Subgroup & Count Black & Treatment & Simple & 0.0669 & 0.0400 & 1.670 & 0.0951 & + \\
Demographic Subgroup & Count Black Male & Treatment & Simple & 0.0651 & 0.0339 & 1.922 & 0.0548 & + \\
\addlinespace[0.5em]
\multicolumn{9}{l}{\textbf{Moderation Analysis}} \\
\midrule
Department Rank & Count URM & Treatment $\times$ Dept Ranking & Extended & 0.0039 & 0.0019 & 2.058 & 0.0397 & * \\
\addlinespace[0.5em]
\multicolumn{9}{l}{\textbf{Semester Analysis}} \\
\midrule
Fall Semester & Any Black & Treatment & Simple & 0.0377 & 0.0169 & 2.232 & 0.0258 & * \\
Fall Semester & Any URM & Treatment & Simple & 0.0427 & 0.0255 & 1.676 & 0.0939 & + \\
Fall Semester & Count Black & Treatment & Simple & 0.0489 & 0.0213 & 2.299 & 0.0216 & * \\
Fall Semester & Count URM & Treatment & Simple & 0.0978 & 0.0467 & 2.093 & 0.0365 & * \\
\bottomrule
\end{tabular}
} % End group for scriptsize and tabcolsep
\parbox{\linewidth}{\footnotesize Note: Significance levels: + p<0.1; * p<0.05; ** p<0.01; *** p<0.001. SE = Clustered standard errors at department level. Constant terms are excluded from this summary.}
\end{table}
