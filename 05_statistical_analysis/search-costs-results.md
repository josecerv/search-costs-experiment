---
title: "Search Costs Field Experiment"
date: "2025-06-20"
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
Number of seminars & 1654 \\
Number of unique departments & 527 \\
Total speakers across all seminars & 23219 \\
Mean speakers per seminar & 14.04 \\
SD speakers per seminar & 9.90 \\
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
URM & 7.40 & 11.09 & 1.00 & 1.28 & 54.0 \\
Black & 2.22 & 5.91 & 0.32 & 0.69 & 23.3 \\
Hispanic & 5.16 & 9.52 & 0.68 & 1.01 & 42.6 \\
Female & 16.91 & 16.10 & 2.40 & 2.47 & 76.2 \\
\bottomrule
\end{tabular}
\parbox{\linewidth}{\footnotesize Note: N =  1654  seminars. Percentages calculated among speakers with demographic data available. 'Pct. Any' indicates the percentage of seminars that have at least one speaker from that demographic group.}
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
Total faculty per department & 34.1 & 18.1 \\
\% URM faculty & 4.09 & 4.41 \\
\% Women faculty & 20.40 & 7.59 \\
\bottomrule
\end{tabular}
\parbox{\linewidth}{\footnotesize Note: N =  527  unique departments. Department faculty demographics based on 2024 coding.}
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
Chemistry & 270 & 122 & 14.5 & 10.9 \\
Computer Science & 142 & 82 & 13.2 & 10.3 \\
Mathematics & 812 & 134 & 13.3 & 9.1 \\
Mechanical Engineering & 81 & 65 & 13.0 & 10.2 \\
Physics & 349 & 124 & 15.9 & 10.4 \\
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
Chemistry & 270 & 8.88 & 10.48 & 1.27 & 64.4 \\
Computer Science & 142 & 4.48 & 8.21 & 0.54 & 36.6 \\
Mathematics & 812 & 6.99 & 10.67 & 0.93 & 49.8 \\
Mechanical Engineering & 81 & 8.20 & 9.17 & 1.12 & 61.7 \\
Physics & 349 & 8.22 & 13.45 & 1.12 & 61.0 \\
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
Chemistry & 4.24 & 39.6 & 4.53 & 45.2 & 23.52 & 86.7 \\
Computer Science & 1.55 & 17.6 & 2.93 & 24.6 & 19.21 & 78.2 \\
Mathematics & 1.76 & 19.5 & 5.21 & 40.5 & 13.94 & 70.7 \\
Mechanical Engineering & 2.95 & 28.4 & 5.25 & 46.9 & 19.87 & 77.8 \\
Physics & 1.83 & 20.9 & 6.40 & 51.9 & 17.10 & 79.9 \\
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
Chemistry & 122 & 28.6 & 11.9 & 4.76 & 4.47 & 24.40 & 7.18 \\
Computer Science & 82 & 43.5 & 25.0 & 2.79 & 3.27 & 20.12 & 7.28 \\
Mathematics & 134 & 33.9 & 16.2 & 3.63 & 3.54 & 19.82 & 7.67 \\
Mechanical Engineering & 65 & 36.4 & 19.1 & 5.57 & 5.48 & 19.70 & 7.61 \\
Physics & 124 & 32.1 & 16.5 & 4.02 & 4.91 & 17.62 & 6.54 \\
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
Fall (1448) & 7.08 & 0.53 & 36.3 & 1.72 & 11.7 & 5.34 & 28.9 \\
Spring (1388) & 7.49 & 0.64 & 41.4 & 2.65 & 18.4 & 4.82 & 29.3 \\
\midrule
 & \multicolumn{3}{c}{Female} & \multicolumn{2}{c}{Total Speakers} & & \\
Semester & Mean \% & Mean Count & Pct. Any & Mean & SD & & \\
\midrule
Fall & 16.14 & 1.27 & 62.0 & 7.75 & 5.50 & & \\
Spring & 17.64 & 1.53 & 65.0 & 8.65 & 6.86 & & \\
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
Treatment  &  0.788$^{}$ & 0.759$^{}$ & 0.104$^{}$ & 0.082$^{}$ & 0.021$^{}$ & 0.015$^{}$  \\
 &  (0.522) & (0.514) & (0.066) & (0.064) & (0.025) & (0.023)  \\
Constant  &  7.770$^{***}$ & 3.403$^{}$ & 1.098$^{***}$ & 0.197$^{}$ & 0.562$^{***}$ & 0.208$^{+}$  \\
 &  (1.658) & (2.098) & (0.168) & (0.273) & (0.069) & (0.116)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,654 & 1,654 & 1,654 & 1,654 & 1,654 & 1,654  \\
Adjusted $R^2$ &  0.011 & 0.017 & 0.030 & 0.039 & 0.029 & 0.042  \\
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
Treatment  &  -0.472$^{}$ & -0.438$^{}$ & 0.104$^{}$ & 0.082$^{}$ & -0.576$^{}$ & -0.520$^{}$  \\
 &  (0.545) & (0.544) & (0.066) & (0.064) & (0.518) & (0.518)  \\
Constant  &  17.123$^{***}$ & 13.824$^{***}$ & 1.098$^{***}$ & 0.197$^{}$ & 16.025$^{***}$ & 13.626$^{***}$  \\
 &  (1.256) & (2.405) & (0.168) & (0.273) & (1.174) & (2.250)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,654 & 1,654 & 1,654 & 1,654 & 1,654 & 1,654  \\
Adjusted $R^2$ &  0.032 & 0.056 & 0.030 & 0.039 & 0.031 & 0.056  \\
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
URM Speakers & 0.1042 & (0.0630) \\
Non-URM Speakers & -0.5763 & (0.4599) \\
\midrule
Sum of Effects & -0.4721 & --- \\
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
Treatment  &  0.670$^{*}$ & 0.661$^{*}$ & 0.084$^{*}$ & 0.084$^{*}$ & 0.056$^{*}$ & 0.056$^{*}$  \\
 &  (0.306) & (0.290) & (0.040) & (0.038) & (0.023) & (0.023)  \\
Constant  &  2.709$^{***}$ & 0.977$^{}$ & 0.434$^{***}$ & 0.118$^{}$ & 0.293$^{***}$ & 0.065$^{}$  \\
 &  (0.790) & (1.300) & (0.103) & (0.168) & (0.061) & (0.105)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,654 & 1,654 & 1,654 & 1,654 & 1,654 & 1,654  \\
Adjusted $R^2$ &  0.026 & 0.031 & 0.048 & 0.056 & 0.035 & 0.044  \\
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
Treatment  &  0.132$^{}$ & 0.104$^{}$ & 0.020$^{}$ & -0.004$^{}$ & -0.014$^{}$ & -0.024$^{}$  \\
 &  (0.456) & (0.470) & (0.048) & (0.048) & (0.025) & (0.025)  \\
Constant  &  4.849$^{**}$ & 2.208$^{}$ & 0.638$^{***}$ & 0.043$^{}$ & 0.415$^{***}$ & 0.151$^{}$  \\
 &  (1.517) & (1.867) & (0.136) & (0.208) & (0.070) & (0.107)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,654 & 1,654 & 1,654 & 1,654 & 1,654 & 1,654  \\
Adjusted $R^2$ &  0.006 & 0.006 & 0.015 & 0.021 & 0.021 & 0.025  \\
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
Treatment  &  0.266$^{}$ & -0.240$^{}$ & -0.062$^{}$ & -0.127$^{}$ & 0.005$^{}$ & 0.001$^{}$  \\
 &  (0.829) & (0.819) & (0.127) & (0.127) & (0.022) & (0.022)  \\
Constant  &  21.961$^{***}$ & 13.684$^{***}$ & 3.656$^{***}$ & 2.260$^{***}$ & 0.875$^{***}$ & 0.708$^{***}$  \\
 &  (2.069) & (3.902) & (0.338) & (0.593) & (0.061) & (0.100)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,654 & 1,654 & 1,654 & 1,654 & 1,654 & 1,654  \\
Adjusted $R^2$ &  0.051 & 0.059 & 0.084 & 0.099 & 0.017 & 0.025  \\
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
Treatment  &  0.022$^{}$ & -0.040$^{}$ & 0.020$^{}$ & 0.013$^{}$ & 0.013$^{}$ & 0.007$^{}$  \\
 &  (0.171) & (0.183) & (0.019) & (0.019) & (0.017) & (0.017)  \\
Constant  &  1.772$^{**}$ & -0.024$^{}$ & 0.199$^{***}$ & 0.004$^{}$ & 0.169$^{***}$ & -0.007$^{}$  \\
 &  (0.603) & (0.578) & (0.060) & (0.091) & (0.049) & (0.078)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,654 & 1,654 & 1,654 & 1,654 & 1,654 & 1,654  \\
Adjusted $R^2$ &  0.013 & 0.019 & 0.037 & 0.046 & 0.037 & 0.045  \\
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
Treatment  &  0.134$^{*}$ & 0.144$^{*}$ & 0.011$^{}$ & 0.012$^{}$ & 0.013$^{}$ & 0.014$^{+}$  \\
 &  (0.068) & (0.070) & (0.009) & (0.009) & (0.008) & (0.008)  \\
Constant  &  0.471$^{**}$ & 0.056$^{}$ & 0.054$^{*}$ & 0.008$^{}$ & 0.042$^{*}$ & 0.008$^{}$  \\
 &  (0.149) & (0.268) & (0.024) & (0.042) & (0.020) & (0.036)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,654 & 1,654 & 1,654 & 1,654 & 1,654 & 1,654  \\
Adjusted $R^2$ &  0.032 & 0.037 & 0.020 & 0.024 & 0.017 & 0.021  \\
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
Treatment  &  0.536$^{*}$ & 0.516$^{*}$ & 0.074$^{*}$ & 0.073$^{*}$ & 0.059$^{**}$ & 0.059$^{**}$  \\
 &  (0.263) & (0.247) & (0.034) & (0.033) & (0.023) & (0.022)  \\
Constant  &  2.238$^{**}$ & 0.922$^{}$ & 0.372$^{***}$ & 0.106$^{}$ & 0.284$^{***}$ & 0.049$^{}$  \\
 &  (0.709) & (1.166) & (0.092) & (0.144) & (0.061) & (0.103)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,654 & 1,654 & 1,654 & 1,654 & 1,654 & 1,654  \\
Adjusted $R^2$ &  0.019 & 0.022 & 0.041 & 0.048 & 0.035 & 0.043  \\
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
Treatment  &  -0.117$^{}$ & -0.191$^{}$ & 0.006$^{}$ & -0.000$^{}$ & 0.003$^{}$ & -0.003$^{}$  \\
 &  (0.160) & (0.175) & (0.013) & (0.013) & (0.012) & (0.012)  \\
Constant  &  1.276$^{*}$ & -0.123$^{}$ & 0.061$^{}$ & -0.052$^{}$ & 0.055$^{}$ & -0.055$^{}$  \\
 &  (0.588) & (0.487) & (0.044) & (0.066) & (0.035) & (0.057)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,654 & 1,654 & 1,654 & 1,654 & 1,654 & 1,654  \\
Adjusted $R^2$ &  0.001 & 0.004 & 0.006 & 0.013 & 0.005 & 0.011  \\
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
Treatment  &  0.248$^{}$ & 0.295$^{}$ & 0.013$^{}$ & -0.004$^{}$ & -0.015$^{}$ & -0.024$^{}$  \\
 &  (0.389) & (0.398) & (0.044) & (0.043) & (0.025) & (0.025)  \\
Constant  &  3.574$^{**}$ & 2.331$^{}$ & 0.571$^{***}$ & 0.093$^{}$ & 0.412$^{***}$ & 0.165$^{}$  \\
 &  (1.334) & (1.636) & (0.113) & (0.178) & (0.070) & (0.107)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,654 & 1,654 & 1,654 & 1,654 & 1,654 & 1,654  \\
Adjusted $R^2$ &  0.008 & 0.007 & 0.015 & 0.021 & 0.022 & 0.026  \\
\bottomrule
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize \vspace{2pt}Clustered standard errors at department level in parentheses.}}\\
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize $^{+}p<0.1$; $^{*}p<0.05$; $^{**}p<0.01$; $^{***}p<0.001$\vspace{2pt}}}\\
\end{tabularx}
\end{table}

\newpage

# Discipline Subgroup Analysis


\subsubsection{Chemistry (N=270)}

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
Treatment  &  0.643$^{}$ & -0.106$^{}$ & -0.089$^{}$ & -0.157$^{}$ & 0.027$^{}$ & 0.005$^{}$  \\
 &  (1.177) & (1.169) & (0.165) & (0.166) & (0.052) & (0.057)  \\
Constant  &  6.081$^{*}$ & -2.012$^{}$ & 0.908$^{*}$ & -0.764$^{}$ & 0.197$^{}$ & -0.304$^{}$  \\
 &  (2.655) & (5.785) & (0.408) & (0.777) & (0.130) & (0.266)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  270 & 270 & 270 & 270 & 270 & 270  \\
Adjusted $R^2$ &  -0.022 & -0.018 & 0.103 & 0.110 & 0.111 & 0.119  \\
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
Treatment  &  0.744$^{}$ & 0.405$^{}$ & 0.021$^{}$ & 0.024$^{}$ & 0.090$^{}$ & 0.062$^{}$  \\
 &  (1.057) & (0.848) & (0.121) & (0.100) & (0.065) & (0.059)  \\
Constant  &  2.245$^{}$ & -8.846$^{*}$ & 0.314$^{}$ & -1.603$^{**}$ & 0.120$^{}$ & -0.963$^{**}$  \\
 &  (2.564) & (3.920) & (0.246) & (0.535) & (0.155) & (0.295)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  270 & 270 & 270 & 270 & 270 & 270  \\
Adjusted $R^2$ &  -0.033 & -0.014 & 0.045 & 0.084 & 0.045 & 0.098  \\
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
Treatment  &  -0.035$^{}$ & -0.470$^{}$ & -0.123$^{}$ & -0.202$^{}$ & -0.089$^{}$ & -0.125$^{+}$  \\
 &  (0.976) & (1.009) & (0.116) & (0.127) & (0.062) & (0.064)  \\
Constant  &  3.004$^{+}$ & 4.627$^{}$ & 0.562$^{}$ & 0.579$^{}$ & 0.236$^{}$ & 0.245$^{}$  \\
 &  (1.766) & (4.893) & (0.358) & (0.546) & (0.159) & (0.303)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  270 & 270 & 270 & 270 & 270 & 270  \\
Adjusted $R^2$ &  -0.022 & -0.022 & 0.049 & 0.074 & 0.038 & 0.057  \\
\bottomrule
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize \vspace{2pt}Clustered standard errors at department level in parentheses.}}\\
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize $^{+}p<0.1$; $^{*}p<0.05$; $^{**}p<0.01$; $^{***}p<0.001$\vspace{2pt}}}\\
\end{tabularx}
\end{table}

\subsubsection{Mathematics (N=812)}

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
Treatment  &  1.096$^{}$ & 1.398$^{+}$ & 0.183$^{+}$ & 0.189$^{+}$ & 0.025$^{}$ & 0.020$^{}$  \\
 &  (0.728) & (0.798) & (0.093) & (0.101) & (0.034) & (0.033)  \\
Constant  &  5.536$^{***}$ & 4.759$^{}$ & 0.786$^{***}$ & 0.035$^{}$ & 0.470$^{***}$ & 0.174$^{}$  \\
 &  (1.420) & (4.201) & (0.131) & (0.519) & (0.063) & (0.187)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  812 & 812 & 812 & 812 & 812 & 812  \\
Adjusted $R^2$ &  0.001 & -0.001 & 0.001 & 0.000 & -0.008 & 0.001  \\
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
Treatment  &  0.221$^{}$ & 0.523$^{}$ & 0.081$^{}$ & 0.120$^{*}$ & 0.023$^{}$ & 0.035$^{}$  \\
 &  (0.386) & (0.421) & (0.050) & (0.054) & (0.029) & (0.027)  \\
Constant  &  0.826$^{}$ & 1.703$^{}$ & 0.198$^{**}$ & 0.346$^{}$ & 0.173$^{***}$ & 0.066$^{}$  \\
 &  (0.513) & (2.402) & (0.072) & (0.263) & (0.052) & (0.151)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  812 & 812 & 812 & 812 & 812 & 812  \\
Adjusted $R^2$ &  0.011 & 0.021 & 0.010 & 0.024 & 0.005 & 0.020  \\
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
Treatment  &  0.894$^{}$ & 0.879$^{}$ & 0.107$^{}$ & 0.070$^{}$ & 0.031$^{}$ & 0.017$^{}$  \\
 &  (0.632) & (0.681) & (0.071) & (0.069) & (0.033) & (0.036)  \\
Constant  &  4.634$^{***}$ & 2.904$^{}$ & 0.570$^{***}$ & -0.348$^{}$ & 0.374$^{***}$ & 0.154$^{}$  \\
 &  (1.291) & (3.230) & (0.102) & (0.378) & (0.070) & (0.185)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  812 & 812 & 812 & 812 & 812 & 812  \\
Adjusted $R^2$ &  -0.004 & -0.003 & -0.000 & 0.004 & -0.001 & -0.001  \\
\bottomrule
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize \vspace{2pt}Clustered standard errors at department level in parentheses.}}\\
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize $^{+}p<0.1$; $^{*}p<0.05$; $^{**}p<0.01$; $^{***}p<0.001$\vspace{2pt}}}\\
\end{tabularx}
\end{table}

\subsubsection{Physics (N=349)}

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
Treatment  &  0.257$^{}$ & 0.137$^{}$ & 0.164$^{}$ & 0.140$^{}$ & -0.001$^{}$ & -0.000$^{}$  \\
 &  (1.190) & (1.150) & (0.130) & (0.128) & (0.058) & (0.051)  \\
Constant  &  13.454$^{***}$ & 7.788$^{}$ & 1.251$^{***}$ & 1.652$^{}$ & 0.407$^{***}$ & 0.922$^{+}$  \\
 &  (2.392) & (13.711) & (0.169) & (1.433) & (0.073) & (0.555)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  349 & 349 & 349 & 349 & 349 & 349  \\
Adjusted $R^2$ &  0.004 & -0.002 & 0.005 & 0.008 & 0.004 & 0.030  \\
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
Treatment  &  1.488$^{*}$ & 1.612$^{**}$ & 0.176$^{*}$ & 0.184$^{**}$ & 0.124$^{*}$ & 0.129$^{*}$  \\
 &  (0.605) & (0.615) & (0.068) & (0.070) & (0.048) & (0.050)  \\
Constant  &  -0.215$^{}$ & -0.025$^{}$ & 0.032$^{}$ & 0.246$^{}$ & 0.001$^{}$ & 0.029$^{}$  \\
 &  (0.409) & (4.614) & (0.082) & (0.648) & (0.052) & (0.444)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  349 & 349 & 349 & 349 & 349 & 349  \\
Adjusted $R^2$ &  0.001 & -0.003 & 0.020 & 0.009 & 0.012 & 0.014  \\
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
Treatment  &  -1.230$^{}$ & -1.475$^{}$ & -0.012$^{}$ & -0.043$^{}$ & -0.063$^{}$ & -0.066$^{}$  \\
 &  (1.178) & (1.174) & (0.113) & (0.115) & (0.063) & (0.058)  \\
Constant  &  13.669$^{***}$ & 7.813$^{}$ & 1.219$^{***}$ & 1.406$^{}$ & 0.435$^{***}$ & 0.827$^{}$  \\
 &  (2.391) & (12.631) & (0.152) & (1.181) & (0.080) & (0.571)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  349 & 349 & 349 & 349 & 349 & 349  \\
Adjusted $R^2$ &  -0.001 & -0.006 & -0.007 & 0.007 & 0.001 & 0.010  \\
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
Treatment  &  2.148$^{}$ & 2.645$^{}$ & 0.073$^{}$ & 0.063$^{}$ & 0.110$^{}$ & 0.109$^{}$  \\
 &  (1.370) & (1.775) & (0.162) & (0.212) & (0.091) & (0.094)  \\
Constant  &  7.104$^{***}$ & 16.416$^{}$ & 1.378$^{***}$ & 4.200$^{**}$ & 0.882$^{***}$ & 2.540$^{***}$  \\
 &  (1.952) & (13.370) & (0.329) & (1.453) & (0.186) & (0.674)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  142 & 142 & 142 & 142 & 142 & 142  \\
Adjusted $R^2$ &  0.031 & 0.076 & 0.067 & 0.058 & 0.081 & 0.100  \\
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
Treatment  &  0.203$^{}$ & -0.178$^{}$ & -0.057$^{}$ & -0.065$^{}$ & -0.018$^{}$ & -0.042$^{}$  \\
 &  (0.698) & (0.713) & (0.064) & (0.072) & (0.055) & (0.067)  \\
Constant  &  4.152$^{**}$ & 3.617$^{}$ & 0.703$^{***}$ & 2.104$^{*}$ & 0.603$^{***}$ & 1.437$^{*}$  \\
 &  (1.454) & (9.859) & (0.207) & (0.917) & (0.155) & (0.696)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  142 & 142 & 142 & 142 & 142 & 142  \\
Adjusted $R^2$ &  -0.041 & -0.076 & 0.042 & 0.027 & 0.051 & 0.026  \\
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
Treatment  &  1.945$^{}$ & 2.823$^{}$ & 0.131$^{}$ & 0.128$^{}$ & 0.136$^{}$ & 0.156$^{+}$  \\
 &  (1.458) & (1.754) & (0.145) & (0.182) & (0.096) & (0.089)  \\
Constant  &  2.952$^{}$ & 12.798$^{}$ & 0.675$^{*}$ & 2.097$^{+}$ & 0.589$^{**}$ & 2.245$^{**}$  \\
 &  (2.209) & (11.268) & (0.305) & (1.089) & (0.224) & (0.704)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  142 & 142 & 142 & 142 & 142 & 142  \\
Adjusted $R^2$ &  0.039 & 0.101 & 0.029 & 0.018 & 0.066 & 0.088  \\
\bottomrule
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize \vspace{2pt}Clustered standard errors at department level in parentheses.}}\\
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize $^{+}p<0.1$; $^{*}p<0.05$; $^{**}p<0.01$; $^{***}p<0.001$\vspace{2pt}}}\\
\end{tabularx}
\end{table}

\subsubsection{Mechanical Engineering (N=81)}

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
Treatment  &  3.859$^{+}$ & 2.959$^{}$ & 0.665$^{*}$ & 0.731$^{+}$ & 0.113$^{}$ & 0.107$^{}$  \\
 &  (2.026) & (2.002) & (0.300) & (0.370) & (0.116) & (0.130)  \\
Constant  &  17.140$^{**}$ & 0.793$^{}$ & 2.618$^{**}$ & 1.814$^{}$ & 0.792$^{**}$ & 0.316$^{}$  \\
 &  (5.984) & (11.347) & (0.963) & (2.267) & (0.279) & (0.597)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  81 & 81 & 81 & 81 & 81 & 81  \\
Adjusted $R^2$ &  0.039 & 0.055 & 0.033 & 0.133 & -0.002 & -0.009  \\
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
Treatment  &  3.942$^{***}$ & 2.942$^{**}$ & 0.646$^{***}$ & 0.551$^{*}$ & 0.346$^{***}$ & 0.310$^{**}$  \\
 &  (0.999) & (0.937) & (0.185) & (0.210) & (0.090) & (0.097)  \\
Constant  &  8.540$^{**}$ & 6.694$^{}$ & 0.966$^{***}$ & 0.498$^{}$ & 0.818$^{***}$ & 0.679$^{}$  \\
 &  (2.526) & (5.016) & (0.149) & (1.711) & (0.174) & (0.466)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  81 & 81 & 81 & 81 & 81 & 81  \\
Adjusted $R^2$ &  0.153 & 0.170 & 0.129 & 0.185 & 0.157 & 0.196  \\
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
Treatment  &  -0.083$^{}$ & 0.017$^{}$ & 0.019$^{}$ & 0.181$^{}$ & -0.034$^{}$ & 0.006$^{}$  \\
 &  (1.897) & (1.900) & (0.227) & (0.244) & (0.122) & (0.132)  \\
Constant  &  8.600$^{+}$ & -5.901$^{}$ & 1.652$^{+}$ & 1.316$^{}$ & 0.585$^{*}$ & 0.036$^{}$  \\
 &  (4.526) & (11.026) & (0.926) & (1.569) & (0.291) & (0.645)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  81 & 81 & 81 & 81 & 81 & 81  \\
Adjusted $R^2$ &  -0.053 & -0.041 & 0.025 & 0.067 & -0.015 & 0.001  \\
\bottomrule
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize \vspace{2pt}Clustered standard errors at department level in parentheses.}}\\
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize $^{+}p<0.1$; $^{*}p<0.05$; $^{**}p<0.01$; $^{***}p<0.001$\vspace{2pt}}}\\
\end{tabularx}
\end{table}

## Testing for Significant Moderation Across Disciplines

\textbf{F-test for Treatment × Discipline Interactions (Black Speakers):}
F-statistic: 3.583 
p-value: 0.0065 
Degrees of freedom: 4 

The treatment effect on Black speaker representation varies significantly across disciplines (p < 0.05).
This indicates that the diversity intervention has heterogeneous effects depending on the academic field.

\textbf{F-test for Treatment × Discipline Interactions (URM Speakers):}
F-statistic: 0.63 
p-value: 0.6413 
Degrees of freedom: 4 

\textbf{F-test for Treatment × Discipline Interactions (% Black Speakers):}
F-statistic: 2.466 
p-value: 0.0432 
Degrees of freedom: 4 

\textbf{F-test for Treatment × Discipline Interactions (Total Black Speakers):}
F-statistic: 4.132 
p-value: 0.0025 
Degrees of freedom: 4 

\textbf{Individual Interaction Effects (Black Speakers):}
                                      Estimate Std. Error t value Pr(>|t|)
treatment:disc_mathematics             -0.0567     0.0605 -0.9369   0.3490
treatment:disc_physics                  0.0242     0.0685  0.3538   0.7236
treatment:disc_computer_science        -0.1065     0.0879 -1.2117   0.2258
treatment:disc_mechanical_engineering   0.2798     0.1059  2.6421   0.0083

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
Treatment  &  0.944$^{}$ & 0.853$^{}$ & 0.078$^{+}$ & 0.049$^{}$ & 0.033$^{}$ & 0.020$^{}$  \\
 &  (0.694) & (0.687) & (0.046) & (0.044) & (0.025) & (0.025)  \\
Constant  &  6.369$^{**}$ & -2.473$^{}$ & 0.544$^{***}$ & -0.276$^{}$ & 0.366$^{***}$ & -0.058$^{}$  \\
 &  (2.448) & (3.058) & (0.145) & (0.212) & (0.070) & (0.111)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,448 & 1,448 & 1,448 & 1,448 & 1,448 & 1,448  \\
Adjusted $R^2$ &  0.017 & 0.026 & 0.023 & 0.040 & 0.023 & 0.035  \\
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
Treatment  &  0.472$^{}$ & 0.432$^{}$ & 0.053$^{*}$ & 0.050$^{*}$ & 0.043$^{**}$ & 0.042$^{*}$  \\
 &  (0.331) & (0.332) & (0.021) & (0.021) & (0.017) & (0.017)  \\
Constant  &  2.819$^{**}$ & -1.717$^{}$ & 0.224$^{***}$ & -0.075$^{}$ & 0.172$^{***}$ & -0.067$^{}$  \\
 &  (0.985) & (1.425) & (0.061) & (0.097) & (0.046) & (0.080)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,448 & 1,448 & 1,448 & 1,448 & 1,448 & 1,448  \\
Adjusted $R^2$ &  0.023 & 0.037 & 0.033 & 0.046 & 0.028 & 0.041  \\
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
Treatment  &  0.455$^{}$ & 0.390$^{}$ & 0.024$^{}$ & -0.003$^{}$ & 0.011$^{}$ & -0.004$^{}$  \\
 &  (0.636) & (0.659) & (0.038) & (0.038) & (0.024) & (0.025)  \\
Constant  &  3.408$^{}$ & -0.999$^{}$ & 0.307$^{*}$ & -0.224$^{}$ & 0.238$^{**}$ & -0.063$^{}$  \\
 &  (2.362) & (2.932) & (0.134) & (0.188) & (0.073) & (0.109)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,448 & 1,448 & 1,448 & 1,448 & 1,448 & 1,448  \\
Adjusted $R^2$ &  0.011 & 0.010 & 0.020 & 0.029 & 0.022 & 0.028  \\
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
Treatment  &  0.771$^{}$ & 0.905$^{}$ & 0.030$^{}$ & 0.037$^{}$ & -0.004$^{}$ & -0.001$^{}$  \\
 &  (0.753) & (0.798) & (0.055) & (0.056) & (0.028) & (0.028)  \\
Constant  &  6.932$^{***}$ & 7.323$^{*}$ & 0.876$^{***}$ & 0.794$^{***}$ & 0.498$^{***}$ & 0.403$^{***}$  \\
 &  (1.697) & (2.897) & (0.141) & (0.241) & (0.071) & (0.121)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,388 & 1,388 & 1,388 & 1,388 & 1,388 & 1,388  \\
Adjusted $R^2$ &  0.007 & 0.007 & 0.025 & 0.022 & 0.027 & 0.029  \\
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
Treatment  &  0.891$^{+}$ & 0.926$^{*}$ & 0.038$^{}$ & 0.042$^{}$ & 0.028$^{}$ & 0.031$^{}$  \\
 &  (0.456) & (0.430) & (0.035) & (0.034) & (0.023) & (0.023)  \\
Constant  &  1.923$^{+}$ & 1.818$^{}$ & 0.322$^{***}$ & 0.319$^{*}$ & 0.237$^{***}$ & 0.190$^{+}$  \\
 &  (1.023) & (1.704) & (0.088) & (0.148) & (0.059) & (0.102)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,388 & 1,388 & 1,388 & 1,388 & 1,388 & 1,388  \\
Adjusted $R^2$ &  0.012 & 0.012 & 0.031 & 0.034 & 0.022 & 0.022  \\
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
Treatment  &  -0.099$^{}$ & -0.007$^{}$ & -0.007$^{}$ & -0.005$^{}$ & -0.027$^{}$ & -0.026$^{}$  \\
 &  (0.641) & (0.703) & (0.040) & (0.040) & (0.026) & (0.027)  \\
Constant  &  4.786$^{***}$ & 5.278$^{*}$ & 0.536$^{***}$ & 0.453$^{**}$ & 0.373$^{***}$ & 0.310$^{**}$  \\
 &  (1.364) & (2.477) & (0.096) & (0.170) & (0.065) & (0.103)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,388 & 1,388 & 1,388 & 1,388 & 1,388 & 1,388  \\
Adjusted $R^2$ &  -0.002 & -0.003 & 0.008 & 0.009 & 0.015 & 0.017  \\
\bottomrule
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize \vspace{2pt}Clustered standard errors at department level in parentheses.}}\\
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize $^{+}p<0.1$; $^{*}p<0.05$; $^{**}p<0.01$; $^{***}p<0.001$\vspace{2pt}}}\\
\end{tabularx}
\end{table}

\newpage

# Heterogeneity Analysis

## Moderation by Department Ranking

\subsection{ URM  Speakers}

\begin{table}[H]
\caption{Effect on URM Speakers: Moderation by Department Ranking}
\label{tab:mod_urm_dept_ranking}
\centering
\scriptsize
\begin{tabularx}{\textwidth}{l*{6}{>{\centering\arraybackslash}X}}
\toprule
 & \% URM & \% URM & Count URM & Count URM & Any URM & Any URM \\
 &  (1) & (2) & (3) & (4) & (5) & (6)  \\
\midrule
Treatment  &  0.744$^{}$ & 0.748$^{}$ & 0.104$^{}$ & 0.075$^{}$ & 0.023$^{}$ & 0.013$^{}$  \\
 &  (0.514) & (0.511) & (0.065) & (0.063) & (0.025) & (0.023)  \\
Constant  &  8.970$^{***}$ & 4.961$^{*}$ & 1.057$^{***}$ & 0.251$^{}$ & 0.506$^{***}$ & 0.193$^{+}$  \\
 &  (1.666) & (1.961) & (0.176) & (0.249) & (0.074) & (0.110)  \\
Department Ranking  &  0.016$^{}$ & 0.029$^{*}$ & -0.003$^{*}$ & -0.001$^{}$ & -0.002$^{**}$ & -0.001$^{}$  \\
 &  (0.013) & (0.013) & (0.001) & (0.001) & (0.001) & (0.001)  \\
Treatment $\times$ Department Ranking  &  0.009$^{}$ & 0.007$^{}$ & 0.005$^{*}$ & 0.005$^{**}$ & 0.001$^{}$ & 0.001$^{+}$  \\
 &  (0.016) & (0.016) & (0.002) & (0.002) & (0.001) & (0.001)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,654 & 1,654 & 1,654 & 1,654 & 1,654 & 1,654  \\
Adjusted $R^2$ &  0.013 & 0.017 & 0.034 & 0.043 & 0.033 & 0.043  \\
\bottomrule
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize \vspace{2pt}Clustered standard errors at department level in parentheses.}}\\
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize $^{+}p<0.1$; $^{*}p<0.05$; $^{**}p<0.01$; $^{***}p<0.001$\vspace{2pt}}}\\
\end{tabularx}
\end{table}

\subsection{ BLACK  Speakers}

\begin{table}[H]
\caption{Effect on Black Speakers: Moderation by Department Ranking}
\label{tab:mod_black_dept_ranking}
\centering
\scriptsize
\begin{tabularx}{\textwidth}{l*{6}{>{\centering\arraybackslash}X}}
\toprule
 & \% Black & \% Black & Count Black & Count Black & Any Black & Any Black \\
 &  (1) & (2) & (3) & (4) & (5) & (6)  \\
\midrule
Treatment  &  0.653$^{*}$ & 0.656$^{*}$ & 0.082$^{*}$ & 0.081$^{*}$ & 0.057$^{*}$ & 0.055$^{*}$  \\
 &  (0.305) & (0.288) & (0.039) & (0.037) & (0.023) & (0.023)  \\
Constant  &  3.180$^{***}$ & 1.559$^{}$ & 0.486$^{***}$ & 0.182$^{}$ & 0.266$^{***}$ & 0.063$^{}$  \\
 &  (0.839) & (1.166) & (0.115) & (0.152) & (0.066) & (0.098)  \\
Department Ranking  &  0.006$^{}$ & 0.011$^{}$ & -0.000$^{}$ & 0.001$^{}$ & -0.001$^{*}$ & -0.000$^{}$  \\
 &  (0.007) & (0.008) & (0.001) & (0.001) & (0.000) & (0.001)  \\
Treatment $\times$ Department Ranking  &  0.004$^{}$ & 0.003$^{}$ & 0.002$^{*}$ & 0.002$^{*}$ & 0.001$^{}$ & 0.001$^{}$  \\
 &  (0.009) & (0.009) & (0.001) & (0.001) & (0.001) & (0.001)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,654 & 1,654 & 1,654 & 1,654 & 1,654 & 1,654  \\
Adjusted $R^2$ &  0.027 & 0.031 & 0.052 & 0.059 & 0.037 & 0.045  \\
\bottomrule
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize \vspace{2pt}Clustered standard errors at department level in parentheses.}}\\
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize $^{+}p<0.1$; $^{*}p<0.05$; $^{**}p<0.01$; $^{***}p<0.001$\vspace{2pt}}}\\
\end{tabularx}
\end{table}

\subsection{ HISPANIC  Speakers}

\begin{table}[H]
\caption{Effect on Hispanic Speakers: Moderation by Department Ranking}
\label{tab:mod_hispanic_dept_ranking}
\centering
\scriptsize
\begin{tabularx}{\textwidth}{l*{6}{>{\centering\arraybackslash}X}}
\toprule
 & \% Hispanic & \% Hispanic & Count Hispanic & Count Hispanic & Any Hispanic & Any Hispanic \\
 &  (1) & (2) & (3) & (4) & (5) & (6)  \\
\midrule
Treatment  &  0.107$^{}$ & 0.097$^{}$ & 0.023$^{}$ & -0.007$^{}$ & -0.013$^{}$ & -0.025$^{}$  \\
 &  (0.453) & (0.468) & (0.049) & (0.048) & (0.025) & (0.025)  \\
Constant  &  5.514$^{***}$ & 3.119$^{+}$ & 0.536$^{***}$ & 0.025$^{}$ & 0.377$^{***}$ & 0.146$^{}$  \\
 &  (1.548) & (1.796) & (0.145) & (0.198) & (0.074) & (0.101)  \\
Department Ranking  &  0.009$^{}$ & 0.017$^{}$ & -0.003$^{**}$ & -0.001$^{}$ & -0.001$^{+}$ & -0.000$^{}$  \\
 &  (0.011) & (0.011) & (0.001) & (0.001) & (0.001) & (0.001)  \\
Treatment $\times$ Department Ranking  &  0.004$^{}$ & 0.005$^{}$ & 0.002$^{+}$ & 0.003$^{*}$ & 0.001$^{}$ & 0.001$^{}$  \\
 &  (0.013) & (0.013) & (0.001) & (0.001) & (0.001) & (0.001)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,654 & 1,654 & 1,654 & 1,654 & 1,654 & 1,654  \\
Adjusted $R^2$ &  0.006 & 0.006 & 0.018 & 0.023 & 0.022 & 0.026  \\
\bottomrule
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize \vspace{2pt}Clustered standard errors at department level in parentheses.}}\\
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize $^{+}p<0.1$; $^{*}p<0.05$; $^{**}p<0.01$; $^{***}p<0.001$\vspace{2pt}}}\\
\end{tabularx}
\end{table}

\newpage

## Moderation by Total Faculty Size

\subsection{ URM  Speakers}

\begin{table}[H]
\caption{Effect on URM Speakers: Moderation by Total Faculty}
\label{tab:mod_urm_total_faculty}
\centering
\scriptsize
\begin{tabularx}{\textwidth}{l*{6}{>{\centering\arraybackslash}X}}
\toprule
 & \% URM & \% URM & Count URM & Count URM & Any URM & Any URM \\
 &  (1) & (2) & (3) & (4) & (5) & (6)  \\
\midrule
Treatment  &  1.000$^{+}$ & 0.784$^{}$ & 0.087$^{}$ & 0.079$^{}$ & 0.015$^{}$ & 0.016$^{}$  \\
 &  (0.529) & (0.509) & (0.068) & (0.064) & (0.025) & (0.023)  \\
Constant  &  7.684$^{***}$ & 2.308$^{}$ & 1.086$^{***}$ & 0.209$^{}$ & 0.542$^{***}$ & 0.187$^{+}$  \\
 &  (1.562) & (2.044) & (0.176) & (0.281) & (0.070) & (0.112)  \\
Total Faculty  &  -0.043$^{}$ & -0.036$^{}$ & 0.003$^{}$ & 0.001$^{}$ & 0.000$^{}$ & -0.001$^{}$  \\
 &  (0.026) & (0.026) & (0.003) & (0.003) & (0.001) & (0.001)  \\
Treatment $\times$ Total Faculty  &  0.031$^{}$ & 0.018$^{}$ & -0.001$^{}$ & -0.002$^{}$ & 0.001$^{}$ & 0.001$^{}$  \\
 &  (0.029) & (0.028) & (0.003) & (0.003) & (0.001) & (0.001)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,654 & 1,654 & 1,654 & 1,654 & 1,654 & 1,654  \\
Adjusted $R^2$ &  0.012 & 0.017 & 0.030 & 0.038 & 0.029 & 0.041  \\
\bottomrule
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize \vspace{2pt}Clustered standard errors at department level in parentheses.}}\\
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize $^{+}p<0.1$; $^{*}p<0.05$; $^{**}p<0.01$; $^{***}p<0.001$\vspace{2pt}}}\\
\end{tabularx}
\end{table}

\subsection{ BLACK  Speakers}

\begin{table}[H]
\caption{Effect on Black Speakers: Moderation by Total Faculty}
\label{tab:mod_black_total_faculty}
\centering
\scriptsize
\begin{tabularx}{\textwidth}{l*{6}{>{\centering\arraybackslash}X}}
\toprule
 & \% Black & \% Black & Count Black & Count Black & Any Black & Any Black \\
 &  (1) & (2) & (3) & (4) & (5) & (6)  \\
\midrule
Treatment  &  0.768$^{*}$ & 0.655$^{*}$ & 0.092$^{*}$ & 0.080$^{*}$ & 0.056$^{*}$ & 0.054$^{*}$  \\
 &  (0.308) & (0.287) & (0.041) & (0.037) & (0.023) & (0.023)  \\
Constant  &  2.805$^{***}$ & 0.336$^{}$ & 0.469$^{***}$ & 0.046$^{}$ & 0.309$^{***}$ & 0.027$^{}$  \\
 &  (0.796) & (1.326) & (0.103) & (0.171) & (0.065) & (0.105)  \\
Total Faculty  &  -0.015$^{}$ & -0.014$^{}$ & -0.000$^{}$ & -0.000$^{}$ & 0.001$^{}$ & -0.000$^{}$  \\
 &  (0.011) & (0.010) & (0.001) & (0.002) & (0.001) & (0.001)  \\
Treatment $\times$ Total Faculty  &  0.003$^{}$ & -0.004$^{}$ & -0.002$^{}$ & -0.003$^{+}$ & -0.001$^{}$ & -0.002$^{}$  \\
 &  (0.015) & (0.014) & (0.002) & (0.002) & (0.001) & (0.001)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,654 & 1,654 & 1,654 & 1,654 & 1,654 & 1,654  \\
Adjusted $R^2$ &  0.027 & 0.031 & 0.048 & 0.057 & 0.035 & 0.045  \\
\bottomrule
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize \vspace{2pt}Clustered standard errors at department level in parentheses.}}\\
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize $^{+}p<0.1$; $^{*}p<0.05$; $^{**}p<0.01$; $^{***}p<0.001$\vspace{2pt}}}\\
\end{tabularx}
\end{table}

\subsection{ HISPANIC  Speakers}

\begin{table}[H]
\caption{Effect on Hispanic Speakers: Moderation by Total Faculty}
\label{tab:mod_hispanic_total_faculty}
\centering
\scriptsize
\begin{tabularx}{\textwidth}{l*{6}{>{\centering\arraybackslash}X}}
\toprule
 & \% Hispanic & \% Hispanic & Count Hispanic & Count Hispanic & Any Hispanic & Any Hispanic \\
 &  (1) & (2) & (3) & (4) & (5) & (6)  \\
\midrule
Treatment  &  0.237$^{}$ & 0.133$^{}$ & -0.007$^{}$ & -0.002$^{}$ & -0.024$^{}$ & -0.022$^{}$  \\
 &  (0.467) & (0.466) & (0.048) & (0.048) & (0.025) & (0.025)  \\
Constant  &  4.673$^{**}$ & 1.795$^{}$ & 0.590$^{***}$ & 0.133$^{}$ & 0.381$^{***}$ & 0.183$^{+}$  \\
 &  (1.490) & (1.763) & (0.149) & (0.203) & (0.071) & (0.107)  \\
Total Faculty  &  -0.026$^{}$ & -0.020$^{}$ & 0.003$^{}$ & 0.002$^{}$ & 0.001$^{}$ & 0.000$^{}$  \\
 &  (0.025) & (0.026) & (0.002) & (0.002) & (0.001) & (0.001)  \\
Treatment $\times$ Total Faculty  &  0.026$^{}$ & 0.021$^{}$ & 0.001$^{}$ & 0.001$^{}$ & 0.002$^{}$ & 0.002$^{}$  \\
 &  (0.027) & (0.026) & (0.003) & (0.003) & (0.001) & (0.001)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,654 & 1,654 & 1,654 & 1,654 & 1,654 & 1,654  \\
Adjusted $R^2$ &  0.005 & 0.006 & 0.018 & 0.021 & 0.024 & 0.025  \\
\bottomrule
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize \vspace{2pt}Clustered standard errors at department level in parentheses.}}\\
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize $^{+}p<0.1$; $^{*}p<0.05$; $^{**}p<0.01$; $^{***}p<0.001$\vspace{2pt}}}\\
\end{tabularx}
\end{table}

\newpage

## Moderation by URM Faculty in Peer Departments

\subsection{ URM  Speakers}

\begin{table}[H]
\caption{Effect on URM Speakers: Moderation by Peer URM Faculty}
\label{tab:mod_urm_total_urm_peer_faculty}
\centering
\scriptsize
\begin{tabularx}{\textwidth}{l*{6}{>{\centering\arraybackslash}X}}
\toprule
 & \% URM & \% URM & Count URM & Count URM & Any URM & Any URM \\
 &  (1) & (2) & (3) & (4) & (5) & (6)  \\
\midrule
Treatment  &  0.791$^{}$ & 0.734$^{}$ & 0.108$^{+}$ & 0.080$^{}$ & 0.023$^{}$ & 0.014$^{}$  \\
 &  (0.518) & (0.515) & (0.064) & (0.063) & (0.024) & (0.023)  \\
Constant  &  7.619$^{***}$ & 6.997$^{***}$ & 1.052$^{***}$ & 0.784$^{***}$ & 0.542$^{***}$ & 0.410$^{***}$  \\
 &  (1.589) & (1.814) & (0.163) & (0.221) & (0.066) & (0.098)  \\
Peer URM Faculty  &  0.068$^{}$ & 0.141$^{**}$ & 0.017$^{**}$ & 0.021$^{***}$ & 0.007$^{**}$ & 0.007$^{**}$  \\
 &  (0.054) & (0.054) & (0.005) & (0.006) & (0.002) & (0.002)  \\
Treatment $\times$ Peer URM Faculty  &  -0.067$^{}$ & -0.055$^{}$ & -0.005$^{}$ & -0.006$^{}$ & -0.001$^{}$ & -0.001$^{}$  \\
 &  (0.072) & (0.071) & (0.008) & (0.008) & (0.003) & (0.003)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,654 & 1,654 & 1,654 & 1,654 & 1,654 & 1,654  \\
Adjusted $R^2$ &  0.011 & 0.017 & 0.037 & 0.038 & 0.037 & 0.041  \\
\bottomrule
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize \vspace{2pt}Clustered standard errors at department level in parentheses.}}\\
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize $^{+}p<0.1$; $^{*}p<0.05$; $^{**}p<0.01$; $^{***}p<0.001$\vspace{2pt}}}\\
\end{tabularx}
\end{table}

\subsection{ BLACK  Speakers}

\begin{table}[H]
\caption{Effect on Black Speakers: Moderation by Peer URM Faculty}
\label{tab:mod_black_total_urm_peer_faculty}
\centering
\scriptsize
\begin{tabularx}{\textwidth}{l*{6}{>{\centering\arraybackslash}X}}
\toprule
 & \% Black & \% Black & Count Black & Count Black & Any Black & Any Black \\
 &  (1) & (2) & (3) & (4) & (5) & (6)  \\
\midrule
Treatment  &  0.673$^{*}$ & 0.662$^{*}$ & 0.085$^{*}$ & 0.084$^{*}$ & 0.058$^{*}$ & 0.058$^{*}$  \\
 &  (0.303) & (0.288) & (0.039) & (0.037) & (0.023) & (0.023)  \\
Constant  &  2.675$^{***}$ & 2.386$^{*}$ & 0.425$^{***}$ & 0.368$^{*}$ & 0.283$^{***}$ & 0.233$^{**}$  \\
 &  (0.783) & (1.005) & (0.103) & (0.144) & (0.062) & (0.086)  \\
Peer URM Faculty  &  0.013$^{}$ & 0.040$^{}$ & 0.003$^{}$ & 0.007$^{}$ & 0.003$^{}$ & 0.003$^{}$  \\
 &  (0.023) & (0.029) & (0.003) & (0.004) & (0.002) & (0.002)  \\
Treatment $\times$ Peer URM Faculty  &  -0.004$^{}$ & 0.004$^{}$ & 0.000$^{}$ & 0.001$^{}$ & 0.002$^{}$ & 0.003$^{}$  \\
 &  (0.037) & (0.037) & (0.005) & (0.005) & (0.003) & (0.003)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,654 & 1,654 & 1,654 & 1,654 & 1,654 & 1,654  \\
Adjusted $R^2$ &  0.025 & 0.031 & 0.048 & 0.056 & 0.040 & 0.044  \\
\bottomrule
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize \vspace{2pt}Clustered standard errors at department level in parentheses.}}\\
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize $^{+}p<0.1$; $^{*}p<0.05$; $^{**}p<0.01$; $^{***}p<0.001$\vspace{2pt}}}\\
\end{tabularx}
\end{table}

\subsection{ HISPANIC  Speakers}

\begin{table}[H]
\caption{Effect on Hispanic Speakers: Moderation by Peer URM Faculty}
\label{tab:mod_hispanic_total_urm_peer_faculty}
\centering
\scriptsize
\begin{tabularx}{\textwidth}{l*{6}{>{\centering\arraybackslash}X}}
\toprule
 & \% Hispanic & \% Hispanic & Count Hispanic & Count Hispanic & Any Hispanic & Any Hispanic \\
 &  (1) & (2) & (3) & (4) & (5) & (6)  \\
\midrule
Treatment  &  0.133$^{}$ & 0.077$^{}$ & 0.023$^{}$ & -0.007$^{}$ & -0.013$^{}$ & -0.024$^{}$  \\
 &  (0.454) & (0.472) & (0.047) & (0.048) & (0.025) & (0.025)  \\
Constant  &  4.728$^{**}$ & 4.309$^{*}$ & 0.601$^{***}$ & 0.370$^{*}$ & 0.402$^{***}$ & 0.285$^{**}$  \\
 &  (1.446) & (1.700) & (0.130) & (0.182) & (0.069) & (0.087)  \\
Peer URM Faculty  &  0.057$^{}$ & 0.099$^{+}$ & 0.014$^{***}$ & 0.014$^{**}$ & 0.005$^{*}$ & 0.005$^{+}$  \\
 &  (0.049) & (0.051) & (0.004) & (0.005) & (0.002) & (0.003)  \\
Treatment $\times$ Peer URM Faculty  &  -0.064$^{}$ & -0.060$^{}$ & -0.005$^{}$ & -0.007$^{}$ & -0.000$^{}$ & -0.001$^{}$  \\
 &  (0.063) & (0.063) & (0.006) & (0.006) & (0.003) & (0.003)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,654 & 1,654 & 1,654 & 1,654 & 1,654 & 1,654  \\
Adjusted $R^2$ &  0.006 & 0.006 & 0.022 & 0.021 & 0.024 & 0.025  \\
\bottomrule
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize \vspace{2pt}Clustered standard errors at department level in parentheses.}}\\
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize $^{+}p<0.1$; $^{*}p<0.05$; $^{**}p<0.01$; $^{***}p<0.001$\vspace{2pt}}}\\
\end{tabularx}
\end{table}

\newpage

## Moderation by % Female Email Recipients

\subsection{ URM  Speakers}

\begin{table}[H]
\caption{Effect on URM Speakers: Moderation by \% Female Recipients}
\label{tab:mod_urm_pct_female_recipients}
\centering
\scriptsize
\begin{tabularx}{\textwidth}{l*{6}{>{\centering\arraybackslash}X}}
\toprule
 & \% URM & \% URM & Count URM & Count URM & Any URM & Any URM \\
 &  (1) & (2) & (3) & (4) & (5) & (6)  \\
\midrule
Treatment  &  0.003$^{}$ & 0.027$^{}$ & 0.039$^{}$ & 0.018$^{}$ & -0.010$^{}$ & -0.013$^{}$  \\
 &  (0.671) & (0.659) & (0.084) & (0.082) & (0.031) & (0.030)  \\
Constant  &  8.203$^{***}$ & 3.905$^{+}$ & 1.161$^{***}$ & 0.254$^{}$ & 0.594$^{***}$ & 0.234$^{*}$  \\
 &  (1.687) & (2.071) & (0.177) & (0.277) & (0.070) & (0.116)  \\
\% Female Recipients  &  -1.219$^{}$ & -1.227$^{}$ & -0.213$^{}$ & -0.219$^{}$ & -0.114$^{+}$ & -0.102$^{}$  \\
 &  (1.322) & (1.326) & (0.159) & (0.161) & (0.065) & (0.064)  \\
Treatment $\times$ \% Female Recipients  &  4.030$^{*}$ & 3.735$^{+}$ & 0.310$^{}$ & 0.298$^{}$ & 0.142$^{+}$ & 0.126$^{}$  \\
 &  (1.933) & (1.926) & (0.227) & (0.224) & (0.086) & (0.084)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,654 & 1,654 & 1,654 & 1,654 & 1,654 & 1,654  \\
Adjusted $R^2$ &  0.012 & 0.018 & 0.030 & 0.039 & 0.030 & 0.042  \\
\bottomrule
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize \vspace{2pt}Clustered standard errors at department level in parentheses.}}\\
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize $^{+}p<0.1$; $^{*}p<0.05$; $^{**}p<0.01$; $^{***}p<0.001$\vspace{2pt}}}\\
\end{tabularx}
\end{table}

\subsection{ BLACK  Speakers}

\begin{table}[H]
\caption{Effect on Black Speakers: Moderation by \% Female Recipients}
\label{tab:mod_black_pct_female_recipients}
\centering
\scriptsize
\begin{tabularx}{\textwidth}{l*{6}{>{\centering\arraybackslash}X}}
\toprule
 & \% Black & \% Black & Count Black & Count Black & Any Black & Any Black \\
 &  (1) & (2) & (3) & (4) & (5) & (6)  \\
\midrule
Treatment  &  0.355$^{}$ & 0.407$^{}$ & 0.077$^{}$ & 0.085$^{+}$ & 0.043$^{}$ & 0.048$^{+}$  \\
 &  (0.387) & (0.384) & (0.050) & (0.049) & (0.029) & (0.029)  \\
Constant  &  2.811$^{**}$ & 1.100$^{}$ & 0.450$^{***}$ & 0.121$^{}$ & 0.298$^{***}$ & 0.069$^{}$  \\
 &  (0.856) & (1.304) & (0.111) & (0.169) & (0.064) & (0.106)  \\
\% Female Recipients  &  -0.187$^{}$ & 0.028$^{}$ & -0.062$^{}$ & -0.032$^{}$ & -0.010$^{}$ & 0.006$^{}$  \\
 &  (0.847) & (0.844) & (0.099) & (0.101) & (0.060) & (0.061)  \\
Treatment $\times$ \% Female Recipients  &  1.691$^{}$ & 1.419$^{}$ & 0.024$^{}$ & -0.014$^{}$ & 0.071$^{}$ & 0.049$^{}$  \\
 &  (1.388) & (1.379) & (0.133) & (0.132) & (0.086) & (0.084)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,654 & 1,654 & 1,654 & 1,654 & 1,654 & 1,654  \\
Adjusted $R^2$ &  0.027 & 0.032 & 0.047 & 0.055 & 0.035 & 0.043  \\
\bottomrule
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize \vspace{2pt}Clustered standard errors at department level in parentheses.}}\\
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize $^{+}p<0.1$; $^{*}p<0.05$; $^{**}p<0.01$; $^{***}p<0.001$\vspace{2pt}}}\\
\end{tabularx}
\end{table}

\subsection{ HISPANIC  Speakers}

\begin{table}[H]
\caption{Effect on Hispanic Speakers: Moderation by \% Female Recipients}
\label{tab:mod_hispanic_pct_female_recipients}
\centering
\scriptsize
\begin{tabularx}{\textwidth}{l*{6}{>{\centering\arraybackslash}X}}
\toprule
 & \% Hispanic & \% Hispanic & Count Hispanic & Count Hispanic & Any Hispanic & Any Hispanic \\
 &  (1) & (2) & (3) & (4) & (5) & (6)  \\
\midrule
Treatment  &  -0.328$^{}$ & -0.364$^{}$ & -0.039$^{}$ & -0.069$^{}$ & -0.022$^{}$ & -0.035$^{}$  \\
 &  (0.598) & (0.605) & (0.063) & (0.062) & (0.032) & (0.033)  \\
Constant  &  5.156$^{***}$ & 2.574$^{}$ & 0.683$^{***}$ & 0.096$^{}$ & 0.434$^{***}$ & 0.165$^{}$  \\
 &  (1.556) & (1.850) & (0.144) & (0.212) & (0.073) & (0.108)  \\
\% Female Recipients  &  -0.942$^{}$ & -1.183$^{}$ & -0.142$^{}$ & -0.182$^{}$ & -0.072$^{}$ & -0.083$^{}$  \\
 &  (1.074) & (1.108) & (0.122) & (0.123) & (0.066) & (0.068)  \\
Treatment $\times$ \% Female Recipients  &  2.305$^{}$ & 2.278$^{}$ & 0.290$^{}$ & 0.314$^{+}$ & 0.029$^{}$ & 0.037$^{}$  \\
 &  (1.721) & (1.714) & (0.185) & (0.184) & (0.091) & (0.093)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,654 & 1,654 & 1,654 & 1,654 & 1,654 & 1,654  \\
Adjusted $R^2$ &  0.005 & 0.006 & 0.015 & 0.022 & 0.021 & 0.025  \\
\bottomrule
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize \vspace{2pt}Clustered standard errors at department level in parentheses.}}\\
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize $^{+}p<0.1$; $^{*}p<0.05$; $^{**}p<0.01$; $^{***}p<0.001$\vspace{2pt}}}\\
\end{tabularx}
\end{table}

\newpage

## Moderation by % URM Email Recipients

\subsection{ URM  Speakers}

\begin{table}[H]
\caption{Effect on URM Speakers: Moderation by \% URM Recipients}
\label{tab:mod_urm_pct_urm_recipients}
\centering
\scriptsize
\begin{tabularx}{\textwidth}{l*{6}{>{\centering\arraybackslash}X}}
\toprule
 & \% URM & \% URM & Count URM & Count URM & Any URM & Any URM \\
 &  (1) & (2) & (3) & (4) & (5) & (6)  \\
\midrule
Treatment  &  0.274$^{}$ & 0.305$^{}$ & 0.103$^{}$ & 0.084$^{}$ & 0.022$^{}$ & 0.017$^{}$  \\
 &  (0.565) & (0.562) & (0.074) & (0.072) & (0.028) & (0.026)  \\
Constant  &  8.006$^{***}$ & 3.617$^{+}$ & 1.099$^{***}$ & 0.195$^{}$ & 0.560$^{***}$ & 0.204$^{+}$  \\
 &  (1.661) & (2.074) & (0.171) & (0.279) & (0.070) & (0.119)  \\
\% URM Recipients  &  0.464$^{}$ & 0.788$^{}$ & -0.005$^{}$ & 0.010$^{}$ & 0.021$^{}$ & 0.043$^{}$  \\
 &  (2.109) & (2.045) & (0.226) & (0.225) & (0.101) & (0.100)  \\
Treatment $\times$ \% URM Recipients  &  7.348$^{*}$ & 6.527$^{+}$ & 0.016$^{}$ & -0.022$^{}$ & -0.009$^{}$ & -0.029$^{}$  \\
 &  (3.596) & (3.550) & (0.348) & (0.343) & (0.142) & (0.136)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,654 & 1,654 & 1,654 & 1,654 & 1,654 & 1,654  \\
Adjusted $R^2$ &  0.016 & 0.021 & 0.029 & 0.037 & 0.028 & 0.041  \\
\bottomrule
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize \vspace{2pt}Clustered standard errors at department level in parentheses.}}\\
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize $^{+}p<0.1$; $^{*}p<0.05$; $^{**}p<0.01$; $^{***}p<0.001$\vspace{2pt}}}\\
\end{tabularx}
\end{table}

\subsection{ BLACK  Speakers}

\begin{table}[H]
\caption{Effect on Black Speakers: Moderation by \% URM Recipients}
\label{tab:mod_black_pct_urm_recipients}
\centering
\scriptsize
\begin{tabularx}{\textwidth}{l*{6}{>{\centering\arraybackslash}X}}
\toprule
 & \% Black & \% Black & Count Black & Count Black & Any Black & Any Black \\
 &  (1) & (2) & (3) & (4) & (5) & (6)  \\
\midrule
Treatment  &  0.267$^{}$ & 0.270$^{}$ & 0.066$^{}$ & 0.068$^{}$ & 0.044$^{+}$ & 0.045$^{+}$  \\
 &  (0.317) & (0.307) & (0.043) & (0.042) & (0.025) & (0.025)  \\
Constant  &  2.971$^{***}$ & 1.293$^{}$ & 0.453$^{***}$ & 0.140$^{}$ & 0.306$^{***}$ & 0.081$^{}$  \\
 &  (0.795) & (1.289) & (0.103) & (0.170) & (0.060) & (0.105)  \\
\% URM Recipients  &  -1.068$^{}$ & -1.061$^{}$ & -0.185$^{}$ & -0.164$^{}$ & -0.121$^{}$ & -0.116$^{}$  \\
 &  (1.102) & (1.081) & (0.125) & (0.122) & (0.082) & (0.077)  \\
Treatment $\times$ \% URM Recipients  &  5.572$^{*}$ & 5.315$^{*}$ & 0.242$^{}$ & 0.191$^{}$ & 0.155$^{}$ & 0.142$^{}$  \\
 &  (2.645) & (2.669) & (0.213) & (0.207) & (0.133) & (0.124)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,654 & 1,654 & 1,654 & 1,654 & 1,654 & 1,654  \\
Adjusted $R^2$ &  0.033 & 0.037 & 0.048 & 0.056 & 0.036 & 0.044  \\
\bottomrule
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize \vspace{2pt}Clustered standard errors at department level in parentheses.}}\\
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize $^{+}p<0.1$; $^{*}p<0.05$; $^{**}p<0.01$; $^{***}p<0.001$\vspace{2pt}}}\\
\end{tabularx}
\end{table}

\subsection{ HISPANIC  Speakers}

\begin{table}[H]
\caption{Effect on Hispanic Speakers: Moderation by \% URM Recipients}
\label{tab:mod_hispanic_pct_urm_recipients}
\centering
\scriptsize
\begin{tabularx}{\textwidth}{l*{6}{>{\centering\arraybackslash}X}}
\toprule
 & \% Hispanic & \% Hispanic & Count Hispanic & Count Hispanic & Any Hispanic & Any Hispanic \\
 &  (1) & (2) & (3) & (4) & (5) & (6)  \\
\midrule
Treatment  &  0.016$^{}$ & 0.032$^{}$ & 0.036$^{}$ & 0.012$^{}$ & -0.011$^{}$ & -0.020$^{}$  \\
 &  (0.511) & (0.525) & (0.055) & (0.054) & (0.028) & (0.028)  \\
Constant  &  4.826$^{**}$ & 2.116$^{}$ & 0.621$^{***}$ & 0.022$^{}$ & 0.411$^{***}$ & 0.143$^{}$  \\
 &  (1.545) & (1.893) & (0.137) & (0.210) & (0.072) & (0.109)  \\
\% URM Recipients  &  1.506$^{}$ & 1.789$^{}$ & 0.167$^{}$ & 0.156$^{}$ & 0.059$^{}$ & 0.077$^{}$  \\
 &  (1.772) & (1.755) & (0.171) & (0.176) & (0.092) & (0.095)  \\
Treatment $\times$ \% URM Recipients  &  1.841$^{}$ & 1.321$^{}$ & -0.204$^{}$ & -0.186$^{}$ & -0.028$^{}$ & -0.037$^{}$  \\
 &  (3.163) & (3.115) & (0.253) & (0.256) & (0.144) & (0.144)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,654 & 1,654 & 1,654 & 1,654 & 1,654 & 1,654  \\
Adjusted $R^2$ &  0.006 & 0.007 & 0.014 & 0.020 & 0.020 & 0.025  \\
\bottomrule
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize \vspace{2pt}Clustered standard errors at department level in parentheses.}}\\
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize $^{+}p<0.1$; $^{*}p<0.05$; $^{**}p<0.01$; $^{***}p<0.001$\vspace{2pt}}}\\
\end{tabularx}
\end{table}

\newpage

## Moderation by % URM Faculty in Department

\subsection{ URM  Speakers}

\begin{table}[H]
\caption{Effect on URM Speakers: Moderation by \% URM Faculty}
\label{tab:mod_urm_frac_urm_faculty}
\centering
\scriptsize
\begin{tabularx}{\textwidth}{l*{6}{>{\centering\arraybackslash}X}}
\toprule
 & \% URM & \% URM & Count URM & Count URM & Any URM & Any URM \\
 &  (1) & (2) & (3) & (4) & (5) & (6)  \\
\midrule
Treatment  &  -0.299$^{}$ & -0.143$^{}$ & -0.018$^{}$ & -0.033$^{}$ & 0.012$^{}$ & 0.004$^{}$  \\
 &  (0.748) & (0.745) & (0.094) & (0.093) & (0.035) & (0.033)  \\
Constant  &  7.795$^{***}$ & 3.756$^{+}$ & 1.104$^{***}$ & 0.243$^{}$ & 0.563$^{***}$ & 0.213$^{+}$  \\
 &  (1.683) & (2.080) & (0.172) & (0.272) & (0.070) & (0.117)  \\
\% URM Faculty  &  -5.202$^{}$ & -3.999$^{}$ & -0.698$^{}$ & -0.887$^{}$ & -0.096$^{}$ & -0.272$^{}$  \\
 &  (10.019) & (9.951) & (1.219) & (1.159) & (0.554) & (0.515)  \\
Treatment $\times$ \% URM Faculty  &  28.196$^{+}$ & 24.989$^{}$ & 3.186$^{}$ & 3.209$^{+}$ & 0.241$^{}$ & 0.302$^{}$  \\
 &  (15.711) & (15.532) & (1.966) & (1.942) & (0.671) & (0.656)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,654 & 1,654 & 1,654 & 1,654 & 1,654 & 1,654  \\
Adjusted $R^2$ &  0.013 & 0.018 & 0.032 & 0.040 & 0.028 & 0.041  \\
\bottomrule
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize \vspace{2pt}Clustered standard errors at department level in parentheses.}}\\
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize $^{+}p<0.1$; $^{*}p<0.05$; $^{**}p<0.01$; $^{***}p<0.001$\vspace{2pt}}}\\
\end{tabularx}
\end{table}

\subsection{ BLACK  Speakers}

\begin{table}[H]
\caption{Effect on Black Speakers: Moderation by \% URM Faculty}
\label{tab:mod_black_frac_urm_faculty}
\centering
\scriptsize
\begin{tabularx}{\textwidth}{l*{6}{>{\centering\arraybackslash}X}}
\toprule
 & \% Black & \% Black & Count Black & Count Black & Any Black & Any Black \\
 &  (1) & (2) & (3) & (4) & (5) & (6)  \\
\midrule
Treatment  &  0.024$^{}$ & 0.087$^{}$ & -0.001$^{}$ & 0.005$^{}$ & 0.020$^{}$ & 0.021$^{}$  \\
 &  (0.366) & (0.366) & (0.051) & (0.051) & (0.031) & (0.031)  \\
Constant  &  2.681$^{***}$ & 1.201$^{}$ & 0.439$^{***}$ & 0.149$^{}$ & 0.293$^{***}$ & 0.079$^{}$  \\
 &  (0.813) & (1.315) & (0.107) & (0.166) & (0.063) & (0.105)  \\
\% URM Faculty  &  -1.036$^{}$ & -1.005$^{}$ & -0.579$^{}$ & -0.618$^{}$ & -0.139$^{}$ & -0.254$^{}$  \\
 &  (4.661) & (4.668) & (0.633) & (0.618) & (0.424) & (0.402)  \\
Treatment $\times$ \% URM Faculty  &  16.486$^{*}$ & 15.893$^{+}$ & 2.240$^{*}$ & 2.193$^{*}$ & 0.928$^{}$ & 0.972$^{+}$  \\
 &  (8.372) & (8.323) & (1.089) & (1.030) & (0.586) & (0.567)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,654 & 1,654 & 1,654 & 1,654 & 1,654 & 1,654  \\
Adjusted $R^2$ &  0.030 & 0.033 & 0.051 & 0.059 & 0.037 & 0.045  \\
\bottomrule
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize \vspace{2pt}Clustered standard errors at department level in parentheses.}}\\
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize $^{+}p<0.1$; $^{*}p<0.05$; $^{**}p<0.01$; $^{***}p<0.001$\vspace{2pt}}}\\
\end{tabularx}
\end{table}

\subsection{ HISPANIC  Speakers}

\begin{table}[H]
\caption{Effect on Hispanic Speakers: Moderation by \% URM Faculty}
\label{tab:mod_hispanic_frac_urm_faculty}
\centering
\scriptsize
\begin{tabularx}{\textwidth}{l*{6}{>{\centering\arraybackslash}X}}
\toprule
 & \% Hispanic & \% Hispanic & Count Hispanic & Count Hispanic & Any Hispanic & Any Hispanic \\
 &  (1) & (2) & (3) & (4) & (5) & (6)  \\
\midrule
Treatment  &  -0.331$^{}$ & -0.243$^{}$ & -0.025$^{}$ & -0.047$^{}$ & 0.009$^{}$ & -0.003$^{}$  \\
 &  (0.731) & (0.734) & (0.080) & (0.080) & (0.037) & (0.036)  \\
Constant  &  4.899$^{**}$ & 2.344$^{}$ & 0.639$^{***}$ & 0.060$^{}$ & 0.416$^{***}$ & 0.142$^{}$  \\
 &  (1.541) & (1.861) & (0.139) & (0.210) & (0.070) & (0.108)  \\
\% URM Faculty  &  -4.116$^{}$ & -3.027$^{}$ & -0.207$^{}$ & -0.369$^{}$ & 0.051$^{}$ & -0.026$^{}$  \\
 &  (8.713) & (8.539) & (0.972) & (0.932) & (0.520) & (0.501)  \\
Treatment $\times$ \% URM Faculty  &  12.279$^{}$ & 9.633$^{}$ & 1.155$^{}$ & 1.211$^{}$ & -0.583$^{}$ & -0.592$^{}$  \\
 &  (15.100) & (14.969) & (1.710) & (1.741) & (0.673) & (0.666)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,654 & 1,654 & 1,654 & 1,654 & 1,654 & 1,654  \\
Adjusted $R^2$ &  0.005 & 0.006 & 0.014 & 0.021 & 0.020 & 0.025  \\
\bottomrule
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize \vspace{2pt}Clustered standard errors at department level in parentheses.}}\\
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize $^{+}p<0.1$; $^{*}p<0.05$; $^{**}p<0.01$; $^{***}p<0.001$\vspace{2pt}}}\\
\end{tabularx}
\end{table}

\newpage

## Moderation by % Women Faculty in Department

\subsection{ URM  Speakers}

\begin{table}[H]
\caption{Effect on URM Speakers: Moderation by \% Women Faculty}
\label{tab:mod_urm_frac_women_faculty}
\centering
\scriptsize
\begin{tabularx}{\textwidth}{l*{6}{>{\centering\arraybackslash}X}}
\toprule
 & \% URM & \% URM & Count URM & Count URM & Any URM & Any URM \\
 &  (1) & (2) & (3) & (4) & (5) & (6)  \\
\midrule
Treatment  &  1.587$^{}$ & 1.959$^{}$ & 0.173$^{}$ & 0.134$^{}$ & 0.097$^{}$ & 0.073$^{}$  \\
 &  (1.526) & (1.493) & (0.199) & (0.198) & (0.074) & (0.070)  \\
Constant  &  6.036$^{**}$ & 3.089$^{}$ & 0.966$^{***}$ & 0.184$^{}$ & 0.481$^{***}$ & 0.193$^{}$  \\
 &  (1.943) & (2.143) & (0.218) & (0.277) & (0.086) & (0.119)  \\
\% Women Faculty  &  8.483$^{+}$ & 8.753$^{+}$ & 0.655$^{}$ & 0.669$^{}$ & 0.428$^{}$ & 0.466$^{+}$  \\
 &  (5.034) & (4.962) & (0.727) & (0.711) & (0.284) & (0.268)  \\
Treatment $\times$ \% Women Faculty  &  -4.628$^{}$ & -6.091$^{}$ & -0.392$^{}$ & -0.261$^{}$ & -0.409$^{}$ & -0.297$^{}$  \\
 &  (7.405) & (7.145) & (1.011) & (0.983) & (0.358) & (0.339)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,654 & 1,654 & 1,654 & 1,654 & 1,654 & 1,654  \\
Adjusted $R^2$ &  0.012 & 0.017 & 0.030 & 0.038 & 0.030 & 0.042  \\
\bottomrule
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize \vspace{2pt}Clustered standard errors at department level in parentheses.}}\\
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize $^{+}p<0.1$; $^{*}p<0.05$; $^{**}p<0.01$; $^{***}p<0.001$\vspace{2pt}}}\\
\end{tabularx}
\end{table}

\subsection{ BLACK  Speakers}

\begin{table}[H]
\caption{Effect on Black Speakers: Moderation by \% Women Faculty}
\label{tab:mod_black_frac_women_faculty}
\centering
\scriptsize
\begin{tabularx}{\textwidth}{l*{6}{>{\centering\arraybackslash}X}}
\toprule
 & \% Black & \% Black & Count Black & Count Black & Any Black & Any Black \\
 &  (1) & (2) & (3) & (4) & (5) & (6)  \\
\midrule
Treatment  &  0.206$^{}$ & 0.420$^{}$ & 0.047$^{}$ & 0.055$^{}$ & 0.037$^{}$ & 0.040$^{}$  \\
 &  (0.785) & (0.749) & (0.112) & (0.108) & (0.068) & (0.067)  \\
Constant  &  2.338$^{**}$ & 1.040$^{}$ & 0.380$^{**}$ & 0.125$^{}$ & 0.259$^{***}$ & 0.070$^{}$  \\
 &  (0.884) & (1.331) & (0.121) & (0.168) & (0.075) & (0.107)  \\
\% Women Faculty  &  1.259$^{}$ & 1.612$^{}$ & 0.207$^{}$ & 0.259$^{}$ & 0.133$^{}$ & 0.182$^{}$  \\
 &  (2.759) & (2.613) & (0.383) & (0.354) & (0.250) & (0.233)  \\
Treatment $\times$ \% Women Faculty  &  2.164$^{}$ & 1.219$^{}$ & 0.167$^{}$ & 0.148$^{}$ & 0.085$^{}$ & 0.085$^{}$  \\
 &  (4.344) & (3.972) & (0.614) & (0.568) & (0.343) & (0.331)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,654 & 1,654 & 1,654 & 1,654 & 1,654 & 1,654  \\
Adjusted $R^2$ &  0.026 & 0.031 & 0.047 & 0.056 & 0.035 & 0.043  \\
\bottomrule
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize \vspace{2pt}Clustered standard errors at department level in parentheses.}}\\
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize $^{+}p<0.1$; $^{*}p<0.05$; $^{**}p<0.01$; $^{***}p<0.001$\vspace{2pt}}}\\
\end{tabularx}
\end{table}

\subsection{ HISPANIC  Speakers}

\begin{table}[H]
\caption{Effect on Hispanic Speakers: Moderation by \% Women Faculty}
\label{tab:mod_hispanic_frac_women_faculty}
\centering
\scriptsize
\begin{tabularx}{\textwidth}{l*{6}{>{\centering\arraybackslash}X}}
\toprule
 & \% Hispanic & \% Hispanic & Count Hispanic & Count Hispanic & Any Hispanic & Any Hispanic \\
 &  (1) & (2) & (3) & (4) & (5) & (6)  \\
\midrule
Treatment  &  1.342$^{}$ & 1.509$^{}$ & 0.122$^{}$ & 0.075$^{}$ & 0.091$^{}$ & 0.056$^{}$  \\
 &  (1.348) & (1.354) & (0.147) & (0.148) & (0.073) & (0.074)  \\
Constant  &  3.436$^{+}$ & 1.841$^{}$ & 0.545$^{**}$ & 0.022$^{}$ & 0.343$^{***}$ & 0.130$^{}$  \\
 &  (1.773) & (1.913) & (0.172) & (0.217) & (0.082) & (0.109)  \\
\% Women Faculty  &  7.406$^{+}$ & 7.322$^{+}$ & 0.509$^{}$ & 0.469$^{}$ & 0.417$^{}$ & 0.398$^{}$  \\
 &  (4.220) & (4.195) & (0.535) & (0.547) & (0.257) & (0.263)  \\
Treatment $\times$ \% Women Faculty  &  -6.550$^{}$ & -7.132$^{}$ & -0.546$^{}$ & -0.398$^{}$ & -0.547$^{}$ & -0.404$^{}$  \\
 &  (6.205) & (6.161) & (0.698) & (0.697) & (0.339) & (0.343)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,654 & 1,654 & 1,654 & 1,654 & 1,654 & 1,654  \\
Adjusted $R^2$ &  0.006 & 0.006 & 0.014 & 0.021 & 0.022 & 0.025  \\
\bottomrule
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize \vspace{2pt}Clustered standard errors at department level in parentheses.}}\\
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize $^{+}p<0.1$; $^{*}p<0.05$; $^{**}p<0.01$; $^{***}p<0.001$\vspace{2pt}}}\\
\end{tabularx}
\end{table}

\newpage

## Moderation by % URM Faculty in Department - Black Speakers Only

**Note**: Our dataset contains combined URM faculty percentages (Black, Latino, and Native American) but not Black-specific faculty percentages. This analysis examines whether the treatment effect on Black speaker representation is moderated by the overall URM faculty percentage in the department. While not a perfect measure, departments with higher URM faculty percentages likely have higher Black faculty representation as well.

\begin{table}[H]
\caption{Effect on Black Speakers: Moderation by \% URM Faculty}
\label{tab:mod_black_frac_urm_faculty}
\centering
\scriptsize
\begin{tabularx}{\textwidth}{l*{6}{>{\centering\arraybackslash}X}}
\toprule
 & \% Black & \% Black & Count Black & Count Black & Any Black & Any Black \\
 &  (1) & (2) & (3) & (4) & (5) & (6)  \\
\midrule
Treatment  &  0.024$^{}$ & 0.087$^{}$ & -0.001$^{}$ & 0.005$^{}$ & 0.020$^{}$ & 0.021$^{}$  \\
 &  (0.366) & (0.366) & (0.051) & (0.051) & (0.031) & (0.031)  \\
Constant  &  2.681$^{***}$ & 1.201$^{}$ & 0.439$^{***}$ & 0.149$^{}$ & 0.293$^{***}$ & 0.079$^{}$  \\
 &  (0.813) & (1.315) & (0.107) & (0.166) & (0.063) & (0.105)  \\
\% URM Faculty  &  -1.036$^{}$ & -1.005$^{}$ & -0.579$^{}$ & -0.618$^{}$ & -0.139$^{}$ & -0.254$^{}$  \\
 &  (4.661) & (4.668) & (0.633) & (0.618) & (0.424) & (0.402)  \\
Treatment $\times$ \% URM Faculty  &  16.486$^{*}$ & 15.893$^{+}$ & 2.240$^{*}$ & 2.193$^{*}$ & 0.928$^{}$ & 0.972$^{+}$  \\
 &  (8.372) & (8.323) & (1.089) & (1.030) & (0.586) & (0.567)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,654 & 1,654 & 1,654 & 1,654 & 1,654 & 1,654  \\
Adjusted $R^2$ &  0.030 & 0.033 & 0.051 & 0.059 & 0.037 & 0.045  \\
\bottomrule
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize \vspace{2pt}Clustered standard errors at department level in parentheses.}}\\
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize $^{+}p<0.1$; $^{*}p<0.05$; $^{**}p<0.01$; $^{***}p<0.001$\vspace{2pt}}}\\
\end{tabularx}
\end{table}

\newpage

## Moderation by Number of Distinct Seminars

\subsection{ URM  Speakers}

\begin{table}[H]
\caption{Effect on URM Speakers: Moderation by Number of Seminars}
\label{tab:mod_urm_num_distinct_seminars}
\centering
\scriptsize
\begin{tabularx}{\textwidth}{l*{6}{>{\centering\arraybackslash}X}}
\toprule
 & \% URM & \% URM & Count URM & Count URM & Any URM & Any URM \\
 &  (1) & (2) & (3) & (4) & (5) & (6)  \\
\midrule
Treatment  &  0.760$^{}$ & 0.661$^{}$ & 0.102$^{}$ & 0.068$^{}$ & 0.021$^{}$ & 0.010$^{}$  \\
 &  (0.516) & (0.514) & (0.066) & (0.064) & (0.025) & (0.024)  \\
Constant  &  11.157$^{***}$ & 5.432$^{*}$ & 1.040$^{***}$ & 0.273$^{}$ & 0.435$^{***}$ & 0.167$^{}$  \\
 &  (2.735) & (2.715) & (0.286) & (0.322) & (0.121) & (0.162)  \\
Number of Seminars  &  -0.235$^{}$ & -0.157$^{}$ & 0.012$^{}$ & -0.000$^{}$ & 0.013$^{}$ & 0.007$^{}$  \\
 &  (0.189) & (0.177) & (0.022) & (0.021) & (0.009) & (0.010)  \\
Treatment $\times$ Number of Seminars  &  -0.087$^{}$ & -0.102$^{}$ & -0.010$^{}$ & -0.020$^{+}$ & -0.003$^{}$ & -0.008$^{+}$  \\
 &  (0.085) & (0.089) & (0.010) & (0.011) & (0.004) & (0.005)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,654 & 1,654 & 1,654 & 1,654 & 1,654 & 1,654  \\
Adjusted $R^2$ &  0.012 & 0.017 & 0.029 & 0.039 & 0.029 & 0.042  \\
\bottomrule
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize \vspace{2pt}Clustered standard errors at department level in parentheses.}}\\
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize $^{+}p<0.1$; $^{*}p<0.05$; $^{**}p<0.01$; $^{***}p<0.001$\vspace{2pt}}}\\
\end{tabularx}
\end{table}

\subsection{ BLACK  Speakers}

\begin{table}[H]
\caption{Effect on Black Speakers: Moderation by Number of Seminars}
\label{tab:mod_black_num_distinct_seminars}
\centering
\scriptsize
\begin{tabularx}{\textwidth}{l*{6}{>{\centering\arraybackslash}X}}
\toprule
 & \% Black & \% Black & Count Black & Count Black & Any Black & Any Black \\
 &  (1) & (2) & (3) & (4) & (5) & (6)  \\
\midrule
Treatment  &  0.661$^{*}$ & 0.651$^{*}$ & 0.083$^{*}$ & 0.083$^{*}$ & 0.056$^{*}$ & 0.054$^{*}$  \\
 &  (0.301) & (0.283) & (0.038) & (0.037) & (0.022) & (0.022)  \\
Constant  &  1.094$^{}$ & -1.157$^{}$ & 0.079$^{}$ & -0.314$^{}$ & 0.029$^{}$ & -0.188$^{}$  \\
 &  (1.258) & (1.744) & (0.147) & (0.192) & (0.097) & (0.119)  \\
Number of Seminars  &  0.191$^{*}$ & 0.227$^{*}$ & 0.039$^{***}$ & 0.046$^{***}$ & 0.029$^{***}$ & 0.028$^{***}$  \\
 &  (0.087) & (0.097) & (0.010) & (0.011) & (0.007) & (0.007)  \\
Treatment $\times$ Number of Seminars  &  -0.070$^{+}$ & -0.070$^{}$ & -0.011$^{*}$ & -0.013$^{*}$ & -0.008$^{*}$ & -0.010$^{**}$  \\
 &  (0.041) & (0.043) & (0.005) & (0.006) & (0.004) & (0.004)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,654 & 1,654 & 1,654 & 1,654 & 1,654 & 1,654  \\
Adjusted $R^2$ &  0.027 & 0.033 & 0.053 & 0.063 & 0.043 & 0.051  \\
\bottomrule
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize \vspace{2pt}Clustered standard errors at department level in parentheses.}}\\
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize $^{+}p<0.1$; $^{*}p<0.05$; $^{**}p<0.01$; $^{***}p<0.001$\vspace{2pt}}}\\
\end{tabularx}
\end{table}

\subsection{ HISPANIC  Speakers}

\begin{table}[H]
\caption{Effect on Hispanic Speakers: Moderation by Number of Seminars}
\label{tab:mod_hispanic_num_distinct_seminars}
\centering
\scriptsize
\begin{tabularx}{\textwidth}{l*{6}{>{\centering\arraybackslash}X}}
\toprule
 & \% Hispanic & \% Hispanic & Count Hispanic & Count Hispanic & Any Hispanic & Any Hispanic \\
 &  (1) & (2) & (3) & (4) & (5) & (6)  \\
\midrule
Treatment  &  0.113$^{}$ & 0.013$^{}$ & 0.019$^{}$ & -0.016$^{}$ & -0.014$^{}$ & -0.028$^{}$  \\
 &  (0.445) & (0.471) & (0.048) & (0.047) & (0.025) & (0.026)  \\
Constant  &  9.947$^{***}$ & 6.552$^{*}$ & 0.954$^{***}$ & 0.584$^{*}$ & 0.471$^{***}$ & 0.282$^{*}$  \\
 &  (2.339) & (2.609) & (0.200) & (0.241) & (0.106) & (0.139)  \\
Number of Seminars  &  -0.436$^{**}$ & -0.401$^{*}$ & -0.030$^{+}$ & -0.049$^{**}$ & -0.006$^{}$ & -0.012$^{}$  \\
 &  (0.157) & (0.165) & (0.016) & (0.016) & (0.008) & (0.009)  \\
Treatment $\times$ Number of Seminars  &  -0.015$^{}$ & -0.031$^{}$ & 0.003$^{}$ & -0.006$^{}$ & 0.002$^{}$ & -0.002$^{}$  \\
 &  (0.075) & (0.079) & (0.009) & (0.008) & (0.004) & (0.005)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,654 & 1,654 & 1,654 & 1,654 & 1,654 & 1,654  \\
Adjusted $R^2$ &  0.009 & 0.008 & 0.015 & 0.025 & 0.020 & 0.025  \\
\bottomrule
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize \vspace{2pt}Clustered standard errors at department level in parentheses.}}\\
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize $^{+}p<0.1$; $^{*}p<0.05$; $^{**}p<0.01$; $^{***}p<0.001$\vspace{2pt}}}\\
\end{tabularx}
\end{table}

\newpage

## Junior vs Senior Speaker Analysis

### Analysis: Treatment effects on representation by speaker career stage

This analysis examines whether the treatment differentially affects the representation of junior versus senior speakers.
We define:
- **Junior speakers**: Those below the median years since PhD completion
- **Senior speakers**: Those above the median years since PhD completion

We analyze treatment effects on three types of outcomes for each demographic group (URM, Black, Hispanic):
1. **Percentage**: What percentage of speakers from a demographic group are junior (or senior)?
2. **Count**: How many speakers from a demographic group are junior (or senior)?
3. **Binary**: Does the seminar have any junior (or senior) speakers from this demographic group?

\subsection{Seniority Data Coverage}

Total seminars analyzed: 1654\\[0.3em]
Seminars with junior speakers: 1518 (91.8\%)\\[0.3em]
Seminars with senior speakers: 1535 (92.8\%)\\[0.3em]
Mean junior speakers per seminar: 5.99\\[0.3em]
Mean senior speakers per seminar: 5.88\\[0.3em]
Median years since PhD (cutoff): 12.0\\[0.5em]

\subsection{URM Speakers by Career Stage}



\begin{table}[H]
\caption{Treatment Effects on Junior and Senior URM Speakers}
\centering
\footnotesize
\begin{tabular}{lccccccc}
\toprule
 & \multicolumn{3}{c}{Junior Speakers} & \multicolumn{3}{c}{Senior Speakers} \\
Outcome & Model 1 & Model 2 & & Model 1 & Model 2 \\
\midrule
\% of speakers & 0.9850 & 0.5776 & & 0.6141 & 0.8026 \\
Count & 0.0624 & 0.0444 & & -0.0239 & -0.0211 \\
Any (0/1) & 0.0249 & 0.0135 & & -0.0116 & -0.0063 \\
\midrule
\textit{Mean (Control)} & & & & & \\
\% of speakers & 6.766 & & & 5.899 & \\
Count & 0.407 & & & 0.400 & \\
Any (0/1) & 0.299 & & & 0.284 & \\
\bottomrule
\end{tabular}
\parbox{\linewidth}{\footnotesize Note: + p$<$0.1; * p$<$0.05; ** p$<$0.01; *** p$<$0.001. Standard errors clustered at the department level. Junior speakers are defined as those below the median years since PhD; senior speakers are above the median. Model 1 includes baseline controls; Model 2 adds extended controls.}
\end{table}

\subsection{Black Speakers by Career Stage}



\begin{table}[H]
\caption{Treatment Effects on Junior and Senior Black Speakers}
\centering
\footnotesize
\begin{tabular}{lccccccc}
\toprule
 & \multicolumn{3}{c}{Junior Speakers} & \multicolumn{3}{c}{Senior Speakers} \\
Outcome & Model 1 & Model 2 & & Model 1 & Model 2 \\
\midrule
\% of speakers & 0.8051+ & 0.6486 & & 0.4364 & 0.4963 \\
Count & 0.0445* & 0.0447* & & 0.0067 & 0.0066 \\
Any (0/1) & 0.0402* & 0.0407* & & 0.0139 & 0.0143 \\
\midrule
\textit{Mean (Control)} & & & & & \\
\% of speakers & 2.013 & & & 1.275 & \\
Count & 0.110 & & & 0.110 & \\
Any (0/1) & 0.095 & & & 0.087 & \\
\bottomrule
\end{tabular}
\parbox{\linewidth}{\footnotesize Note: + p$<$0.1; * p$<$0.05; ** p$<$0.01; *** p$<$0.001. Standard errors clustered at the department level. Junior speakers are defined as those below the median years since PhD; senior speakers are above the median. Model 1 includes baseline controls; Model 2 adds extended controls.}
\end{table}

\subsection{Hispanic Speakers by Career Stage}



\begin{table}[H]
\caption{Treatment Effects on Junior and Senior Hispanic Speakers}
\centering
\footnotesize
\begin{tabular}{lccccccc}
\toprule
 & \multicolumn{3}{c}{Junior Speakers} & \multicolumn{3}{c}{Senior Speakers} \\
Outcome & Model 1 & Model 2 & & Model 1 & Model 2 \\
\midrule
\% of speakers & 0.1516 & -0.1173 & & 0.1777 & 0.3063 \\
Count & 0.0165 & -0.0036 & & -0.0306 & -0.0277 \\
Any (0/1) & -0.0079 & -0.0209 & & -0.0170 & -0.0132 \\
\midrule
\textit{Mean (Control)} & & & & & \\
\% of speakers & 4.739 & & & 4.624 & \\
Count & 0.294 & & & 0.290 & \\
Any (0/1) & 0.233 & & & 0.222 & \\
\bottomrule
\end{tabular}
\parbox{\linewidth}{\footnotesize Note: + p$<$0.1; * p$<$0.05; ** p$<$0.01; *** p$<$0.001. Standard errors clustered at the department level. Junior speakers are defined as those below the median years since PhD; senior speakers are above the median. Model 1 includes baseline controls; Model 2 adds extended controls.}
\end{table}


\clearpage
\section{Summary of All Significant Results}

\begin{landscape}
\begin{table}[H]
\caption{All Significant Results (p < 0.1) from All Analyses}
\label{tab:all_significant_results}
\centering
\footnotesize
\setlength{\tabcolsep}{4pt}
\begin{tabular}{p{3.5cm} p{2.2cm} p{3.2cm} p{1.2cm} r r r r c}
\toprule
Analysis & Outcome & Variable & Model & Coef. & SE & t-stat & p-value & Sig. \\
\midrule
\multicolumn{9}{l}{\textbf{Career Stage Analysis}} \\
\midrule
Junior/Senior Black Speakers & Junior Any (0/1) & Treatment & Simple & 0.0402 & 0.0159 & 2.521 & 0.0118 & * \\
Junior/Senior Black Speakers & Junior Count & Treatment & Simple & 0.0445 & 0.0201 & 2.212 & 0.0271 & * \\
Junior/Senior Black Speakers & Junior \\% of speakers & Treatment & Simple & 0.8051 & 0.4771 & 1.688 & 0.0917 & + \\
\addlinespace[0.5em]
\multicolumn{9}{l}{\textbf{Demographic Subgroups}} \\
\midrule
Demographic Subgroup & \% Black & Treatment & Extended & 0.6606 & 0.2903 & 2.276 & 0.0230 & * \\
Demographic Subgroup & \% Black Female & Treatment & Extended & 0.1443 & 0.0701 & 2.058 & 0.0397 & * \\
Demographic Subgroup & \% Black Male & Treatment & Extended & 0.5163 & 0.2473 & 2.088 & 0.0370 & * \\
Demographic Subgroup & Any Black & Treatment & Extended & 0.0564 & 0.0226 & 2.500 & 0.0125 & * \\
Demographic Subgroup & Any Black Female & Treatment & Extended & 0.0143 & 0.0081 & 1.771 & 0.0768 & + \\
Demographic Subgroup & Any Black Male & Treatment & Extended & 0.0592 & 0.0223 & 2.659 & 0.0079 & ** \\
Demographic Subgroup & Count Black & Treatment & Extended & 0.0839 & 0.0377 & 2.227 & 0.0261 & * \\
Demographic Subgroup & Count Black Male & Treatment & Extended & 0.0729 & 0.0326 & 2.235 & 0.0256 & * \\
\\% Female Recipients & \% URM & Treatment × \\% Female Recipients & Simple & 4.0303 & 1.9327 & 2.085 & 0.0372 & * \\
\\% Female Recipients & Any URM & Treatment × \\% Female Recipients & Simple & 0.1422 & 0.0861 & 1.651 & 0.0989 & + \\
\\% Female Recipients & Count Hispanic & Treatment × \\% Female Recipients & Extended & 0.3144 & 0.1839 & 1.709 & 0.0876 & + \\
\addlinespace[0.5em]
\multicolumn{9}{l}{\textbf{Discipline Analysis}} \\
\midrule
Chemistry & Any Hispanic & Treatment & Extended & -0.1253 & 0.0644 & -1.945 & 0.0529 & + \\
Computer Science & Any Hispanic & Treatment & Extended & 0.1556 & 0.0892 & 1.745 & 0.0836 & + \\
Mathematics & \% URM & Treatment & Extended & 1.3983 & 0.7982 & 1.752 & 0.0802 & + \\
Mathematics & Count Black & Treatment & Extended & 0.1203 & 0.0544 & 2.211 & 0.0273 & * \\
Mathematics & Count URM & Treatment & Simple & 0.1832 & 0.0935 & 1.960 & 0.0503 & + \\
Mechanical Engineering & \% Black & Treatment & Simple & 3.9420 & 0.9989 & 3.946 & 0.0002 & *** \\
Mechanical Engineering & \% URM & Treatment & Simple & 3.8590 & 2.0259 & 1.905 & 0.0613 & + \\
Mechanical Engineering & Any Black & Treatment & Simple & 0.3462 & 0.0898 & 3.855 & 0.0003 & *** \\
Mechanical Engineering & Count Black & Treatment & Simple & 0.6458 & 0.1853 & 3.486 & 0.0009 & *** \\
Mechanical Engineering & Count URM & Treatment & Simple & 0.6652 & 0.2998 & 2.219 & 0.0301 & * \\
Physics & \% Black & Treatment & Extended & 1.6116 & 0.6154 & 2.619 & 0.0092 & ** \\
Physics & Any Black & Treatment & Simple & 0.1244 & 0.0480 & 2.589 & 0.0100 & * \\
Physics & Count Black & Treatment & Extended & 0.1840 & 0.0695 & 2.646 & 0.0085 & ** \\
\addlinespace[0.5em]
\multicolumn{9}{l}{\textbf{Heterogeneity Analysis}} \\
\midrule
Department Ranking & Any URM & Treatment × Department Ranking & Extended & 0.0011 & 0.0006 & 1.764 & 0.0780 & + \\
Department Ranking & Count Black & Treatment × Department Ranking & Simple & 0.0024 & 0.0012 & 2.079 & 0.0378 & * \\
Department Ranking & Count Hispanic & Treatment × Department Ranking & Extended & 0.0026 & 0.0012 & 2.151 & 0.0316 & * \\
Department Ranking & Count URM & Treatment × Department Ranking & Extended & 0.0051 & 0.0018 & 2.828 & 0.0047 & ** \\
Number of Seminars & \% Black & Treatment × Number of Seminars & Simple & -0.0699 & 0.0413 & -1.693 & 0.0907 & + \\
Number of Seminars & Any Black & Treatment × Number of Seminars & Extended & -0.0099 & 0.0038 & -2.610 & 0.0091 & ** \\
Number of Seminars & Any URM & Treatment × Number of Seminars & Extended & -0.0081 & 0.0046 & -1.775 & 0.0761 & + \\
Number of Seminars & Count Black & Treatment × Number of Seminars & Extended & -0.0132 & 0.0058 & -2.288 & 0.0223 & * \\
Number of Seminars & Count URM & Treatment × Number of Seminars & Extended & -0.0202 & 0.0110 & -1.832 & 0.0671 & + \\
Total Faculty & Count Black & Treatment × Total Faculty & Extended & -0.0031 & 0.0018 & -1.689 & 0.0915 & + \\
\\% URM Faculty & \% Black & Treatment × \\% URM Faculty & Simple & 16.4860 & 8.3719 & 1.969 & 0.0491 & * \\
\\% URM Faculty & \% URM & Treatment × \\% URM Faculty & Simple & 28.1958 & 15.7110 & 1.795 & 0.0729 & + \\
\\% URM Faculty & Any Black & Treatment × \\% URM Faculty & Extended & 0.9718 & 0.5670 & 1.714 & 0.0867 & + \\
\\% URM Faculty & Count Black & Treatment × \\% URM Faculty & Extended & 2.1933 & 1.0297 & 2.130 & 0.0333 & * \\
\\% URM Faculty & Count URM & Treatment × \\% URM Faculty & Extended & 3.2094 & 1.9419 & 1.653 & 0.0986 & + \\
\\% URM Recipients & \% Black & Treatment × \\% URM Recipients & Simple & 5.5716 & 2.6453 & 2.106 & 0.0353 & * \\
\\% URM Recipients & \% URM & Treatment × \\% URM Recipients & Simple & 7.3478 & 3.5958 & 2.043 & 0.0412 & * \\
\addlinespace[0.5em]
\multicolumn{9}{l}{\textbf{Semester Analysis}} \\
\midrule
Fall Semester & Any Black & Treatment & Simple & 0.0434 & 0.0167 & 2.603 & 0.0093 & ** \\
Fall Semester & Count Black & Treatment & Simple & 0.0531 & 0.0209 & 2.541 & 0.0112 & * \\
Fall Semester & Count URM & Treatment & Simple & 0.0778 & 0.0456 & 1.707 & 0.0880 & + \\
Spring Semester & \% Black & Treatment & Extended & 0.9257 & 0.4298 & 2.154 & 0.0315 & * \\
\bottomrule
\end{tabular}
\parbox{\linewidth}{\footnotesize Note: Significance levels: + p<0.1; * p<0.05; ** p<0.01; *** p<0.001. SE = Clustered standard errors at department level. For moderation analyses, only significant interaction terms are shown.}
\end{table}
\end{landscape}
