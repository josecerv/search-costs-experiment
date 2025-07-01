---
title: "Search Costs Field Experiment"
date: "2025-07-01"
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
Total speakers across all seminars & 23202 \\
Mean speakers per seminar & 14.03 \\
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
URM & 7.48 & 11.37 & 1.00 & 1.27 & 54.0 \\
Black & 2.20 & 5.90 & 0.31 & 0.68 & 23.2 \\
Hispanic & 5.25 & 9.87 & 0.68 & 1.01 & 42.7 \\
Female & 16.84 & 16.00 & 2.39 & 2.47 & 76.2 \\
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
Computer Science & 142 & 82 & 13.1 & 10.3 \\
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
Chemistry & 270 & 8.92 & 10.48 & 1.27 & 64.8 \\
Computer Science & 142 & 4.45 & 8.22 & 0.54 & 35.9 \\
Mathematics & 812 & 7.15 & 11.26 & 0.92 & 49.8 \\
Mechanical Engineering & 81 & 8.20 & 9.17 & 1.12 & 61.7 \\
Physics & 349 & 8.20 & 13.45 & 1.11 & 61.0 \\
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
Chemistry & 4.21 & 39.3 & 4.61 & 45.6 & 23.52 & 86.7 \\
Computer Science & 1.55 & 17.6 & 2.89 & 23.9 & 19.23 & 78.2 \\
Mathematics & 1.73 & 19.2 & 5.40 & 40.6 & 13.80 & 70.7 \\
Mechanical Engineering & 2.95 & 28.4 & 5.25 & 46.9 & 19.87 & 77.8 \\
Physics & 1.82 & 20.9 & 6.37 & 51.9 & 17.06 & 79.7 \\
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
Spring (1390) & 7.60 & 0.63 & 41.4 & 2.62 & 18.2 & 4.96 & 29.4 \\
\midrule
 & \multicolumn{3}{c}{Female} & \multicolumn{2}{c}{Total Speakers} & & \\
Semester & Mean \% & Mean Count & Pct. Any & Mean & SD & & \\
\midrule
Fall & 16.12 & 1.27 & 61.9 & 7.75 & 5.50 & & \\
Spring & 17.49 & 1.52 & 64.6 & 8.62 & 6.85 & & \\
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
Treatment  &  0.806$^{}$ & 0.777$^{}$ & 0.104$^{}$ & 0.083$^{}$ & 0.021$^{}$ & 0.015$^{}$  \\
 &  (0.531) & (0.519) & (0.066) & (0.064) & (0.025) & (0.023)  \\
Constant  &  7.399$^{***}$ & 3.161$^{}$ & 1.050$^{***}$ & 0.143$^{}$ & 0.553$^{***}$ & 0.194$^{+}$  \\
 &  (1.652) & (2.109) & (0.168) & (0.275) & (0.067) & (0.115)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,654 & 1,654 & 1,654 & 1,654 & 1,654 & 1,654  \\
Adjusted $R^2$ &  0.010 & 0.016 & 0.030 & 0.039 & 0.029 & 0.042  \\
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
Treatment  &  -0.448$^{}$ & -0.425$^{}$ & 0.104$^{}$ & 0.083$^{}$ & -0.552$^{}$ & -0.508$^{}$  \\
 &  (0.548) & (0.546) & (0.066) & (0.064) & (0.522) & (0.521)  \\
Constant  &  17.051$^{***}$ & 13.669$^{***}$ & 1.050$^{***}$ & 0.143$^{}$ & 16.001$^{***}$ & 13.526$^{***}$  \\
 &  (1.288) & (2.446) & (0.168) & (0.275) & (1.198) & (2.282)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,654 & 1,654 & 1,654 & 1,654 & 1,654 & 1,654  \\
Adjusted $R^2$ &  0.032 & 0.055 & 0.030 & 0.039 & 0.031 & 0.056  \\
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
URM Speakers & 0.1043 & (0.0628) \\
Non-URM Speakers & -0.5520 & (0.4601) \\
\midrule
Sum of Effects & -0.4477 & --- \\
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
Treatment  &  0.671$^{*}$ & 0.658$^{*}$ & 0.085$^{*}$ & 0.084$^{*}$ & 0.057$^{*}$ & 0.056$^{*}$  \\
 &  (0.305) & (0.289) & (0.039) & (0.038) & (0.023) & (0.022)  \\
Constant  &  2.495$^{**}$ & 0.714$^{}$ & 0.415$^{***}$ & 0.095$^{}$ & 0.274$^{***}$ & 0.042$^{}$  \\
 &  (0.758) & (1.276) & (0.100) & (0.166) & (0.059) & (0.104)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,654 & 1,654 & 1,654 & 1,654 & 1,654 & 1,654  \\
Adjusted $R^2$ &  0.027 & 0.032 & 0.048 & 0.056 & 0.036 & 0.045  \\
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
Treatment  &  0.149$^{}$ & 0.125$^{}$ & 0.019$^{}$ & -0.004$^{}$ & -0.014$^{}$ & -0.024$^{}$  \\
 &  (0.479) & (0.484) & (0.049) & (0.048) & (0.025) & (0.025)  \\
Constant  &  4.692$^{**}$ & 2.230$^{}$ & 0.610$^{***}$ & 0.012$^{}$ & 0.414$^{***}$ & 0.145$^{}$  \\
 &  (1.538) & (1.908) & (0.141) & (0.214) & (0.069) & (0.106)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,654 & 1,654 & 1,654 & 1,654 & 1,654 & 1,654  \\
Adjusted $R^2$ &  0.004 & 0.005 & 0.014 & 0.020 & 0.020 & 0.025  \\
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
Treatment  &  -0.034$^{}$ & -0.511$^{}$ & -0.070$^{}$ & -0.134$^{}$ & 0.002$^{}$ & -0.002$^{}$  \\
 &  (0.830) & (0.820) & (0.128) & (0.127) & (0.022) & (0.022)  \\
Constant  &  21.549$^{***}$ & 13.522$^{***}$ & 3.600$^{***}$ & 2.200$^{***}$ & 0.874$^{***}$ & 0.714$^{***}$  \\
 &  (2.110) & (3.859) & (0.334) & (0.588) & (0.061) & (0.099)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,654 & 1,654 & 1,654 & 1,654 & 1,654 & 1,654  \\
Adjusted $R^2$ &  0.054 & 0.061 & 0.084 & 0.099 & 0.016 & 0.024  \\
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
Treatment  &  -0.027$^{}$ & -0.084$^{}$ & 0.018$^{}$ & 0.012$^{}$ & 0.011$^{}$ & 0.006$^{}$  \\
 &  (0.175) & (0.187) & (0.018) & (0.019) & (0.016) & (0.016)  \\
Constant  &  1.647$^{**}$ & 0.002$^{}$ & 0.178$^{**}$ & -0.011$^{}$ & 0.148$^{**}$ & -0.022$^{}$  \\
 &  (0.597) & (0.577) & (0.059) & (0.090) & (0.047) & (0.075)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,654 & 1,654 & 1,654 & 1,654 & 1,654 & 1,654  \\
Adjusted $R^2$ &  0.012 & 0.017 & 0.037 & 0.046 & 0.038 & 0.045  \\
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
Treatment  &  0.137$^{*}$ & 0.147$^{*}$ & 0.011$^{}$ & 0.012$^{}$ & 0.013$^{}$ & 0.014$^{+}$  \\
 &  (0.067) & (0.070) & (0.009) & (0.009) & (0.008) & (0.008)  \\
Constant  &  0.436$^{**}$ & 0.014$^{}$ & 0.054$^{*}$ & 0.008$^{}$ & 0.042$^{*}$ & 0.008$^{}$  \\
 &  (0.145) & (0.266) & (0.024) & (0.042) & (0.020) & (0.036)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,654 & 1,654 & 1,654 & 1,654 & 1,654 & 1,654  \\
Adjusted $R^2$ &  0.032 & 0.036 & 0.020 & 0.024 & 0.017 & 0.021  \\
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
Treatment  &  0.534$^{*}$ & 0.511$^{*}$ & 0.075$^{*}$ & 0.073$^{*}$ & 0.060$^{**}$ & 0.059$^{**}$  \\
 &  (0.262) & (0.246) & (0.034) & (0.032) & (0.022) & (0.022)  \\
Constant  &  2.060$^{**}$ & 0.700$^{}$ & 0.353$^{***}$ & 0.083$^{}$ & 0.264$^{***}$ & 0.026$^{}$  \\
 &  (0.681) & (1.144) & (0.088) & (0.140) & (0.058) & (0.102)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,654 & 1,654 & 1,654 & 1,654 & 1,654 & 1,654  \\
Adjusted $R^2$ &  0.019 & 0.023 & 0.041 & 0.049 & 0.035 & 0.044  \\
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
Treatment  &  -0.169$^{}$ & -0.238$^{}$ & 0.005$^{}$ & -0.001$^{}$ & 0.002$^{}$ & -0.003$^{}$  \\
 &  (0.166) & (0.180) & (0.013) & (0.013) & (0.012) & (0.012)  \\
Constant  &  1.187$^{*}$ & -0.056$^{}$ & 0.060$^{}$ & -0.048$^{}$ & 0.054$^{}$ & -0.051$^{}$  \\
 &  (0.586) & (0.490) & (0.045) & (0.066) & (0.035) & (0.057)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,654 & 1,654 & 1,654 & 1,654 & 1,654 & 1,654  \\
Adjusted $R^2$ &  0.001 & 0.002 & 0.006 & 0.011 & 0.005 & 0.010  \\
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
Treatment  &  0.318$^{}$ & 0.363$^{}$ & 0.016$^{}$ & -0.001$^{}$ & -0.010$^{}$ & -0.020$^{}$  \\
 &  (0.410) & (0.412) & (0.044) & (0.043) & (0.025) & (0.025)  \\
Constant  &  3.505$^{**}$ & 2.286$^{}$ & 0.547$^{***}$ & 0.052$^{}$ & 0.409$^{***}$ & 0.148$^{}$  \\
 &  (1.356) & (1.677) & (0.117) & (0.184) & (0.069) & (0.107)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,654 & 1,654 & 1,654 & 1,654 & 1,654 & 1,654  \\
Adjusted $R^2$ &  0.006 & 0.007 & 0.014 & 0.021 & 0.021 & 0.026  \\
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
Treatment  &  0.543$^{}$ & -0.167$^{}$ & -0.092$^{}$ & -0.160$^{}$ & 0.021$^{}$ & 0.002$^{}$  \\
 &  (1.161) & (1.163) & (0.164) & (0.165) & (0.052) & (0.057)  \\
Constant  &  5.885$^{*}$ & -2.063$^{}$ & 0.890$^{*}$ & -0.765$^{}$ & 0.193$^{}$ & -0.307$^{}$  \\
 &  (2.654) & (5.826) & (0.406) & (0.775) & (0.131) & (0.266)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  270 & 270 & 270 & 270 & 270 & 270  \\
Adjusted $R^2$ &  -0.022 & -0.018 & 0.103 & 0.108 & 0.104 & 0.113  \\
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
Treatment  &  0.776$^{}$ & 0.413$^{}$ & 0.025$^{}$ & 0.025$^{}$ & 0.094$^{}$ & 0.063$^{}$  \\
 &  (1.054) & (0.847) & (0.121) & (0.100) & (0.065) & (0.059)  \\
Constant  &  2.137$^{}$ & -8.825$^{*}$ & 0.301$^{}$ & -1.600$^{**}$ & 0.107$^{}$ & -0.960$^{**}$  \\
 &  (2.554) & (3.937) & (0.243) & (0.533) & (0.155) & (0.296)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  270 & 270 & 270 & 270 & 270 & 270  \\
Adjusted $R^2$ &  -0.033 & -0.015 & 0.043 & 0.080 & 0.046 & 0.097  \\
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
Treatment  &  -0.168$^{}$ & -0.539$^{}$ & -0.130$^{}$ & -0.206$^{}$ & -0.096$^{}$ & -0.129$^{*}$  \\
 &  (0.972) & (1.005) & (0.115) & (0.126) & (0.062) & (0.064)  \\
Constant  &  2.915$^{}$ & 4.555$^{}$ & 0.557$^{}$ & 0.576$^{}$ & 0.232$^{}$ & 0.241$^{}$  \\
 &  (1.784) & (4.914) & (0.359) & (0.548) & (0.160) & (0.306)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  270 & 270 & 270 & 270 & 270 & 270  \\
Adjusted $R^2$ &  -0.017 & -0.018 & 0.049 & 0.073 & 0.040 & 0.057  \\
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
Treatment  &  1.141$^{}$ & 1.423$^{+}$ & 0.181$^{+}$ & 0.185$^{+}$ & 0.027$^{}$ & 0.021$^{}$  \\
 &  (0.782) & (0.815) & (0.094) & (0.101) & (0.034) & (0.032)  \\
Constant  &  5.177$^{***}$ & 4.628$^{}$ & 0.740$^{***}$ & -0.052$^{}$ & 0.456$^{***}$ & 0.156$^{}$  \\
 &  (1.374) & (4.326) & (0.125) & (0.526) & (0.061) & (0.187)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  812 & 812 & 812 & 812 & 812 & 812  \\
Adjusted $R^2$ &  -0.005 & -0.004 & 0.001 & 0.000 & -0.011 & -0.003  \\
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
Treatment  &  0.209$^{}$ & 0.510$^{}$ & 0.081$^{}$ & 0.120$^{*}$ & 0.022$^{}$ & 0.034$^{}$  \\
 &  (0.384) & (0.422) & (0.050) & (0.055) & (0.029) & (0.027)  \\
Constant  &  0.664$^{}$ & 1.430$^{}$ & 0.186$^{**}$ & 0.331$^{}$ & 0.160$^{**}$ & 0.042$^{}$  \\
 &  (0.483) & (2.383) & (0.069) & (0.262) & (0.050) & (0.150)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  812 & 812 & 812 & 812 & 812 & 812  \\
Adjusted $R^2$ &  0.012 & 0.023 & 0.011 & 0.025 & 0.006 & 0.021  \\
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
Treatment  &  0.950$^{}$ & 0.917$^{}$ & 0.104$^{}$ & 0.066$^{}$ & 0.033$^{}$ & 0.019$^{}$  \\
 &  (0.707) & (0.714) & (0.072) & (0.069) & (0.033) & (0.036)  \\
Constant  &  4.437$^{***}$ & 3.043$^{}$ & 0.536$^{***}$ & -0.420$^{}$ & 0.367$^{***}$ & 0.148$^{}$  \\
 &  (1.293) & (3.512) & (0.103) & (0.390) & (0.069) & (0.185)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  812 & 812 & 812 & 812 & 812 & 812  \\
Adjusted $R^2$ &  -0.009 & -0.005 & -0.001 & 0.003 & -0.004 & -0.003  \\
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
Treatment  &  0.352$^{}$ & 0.238$^{}$ & 0.176$^{}$ & 0.154$^{}$ & 0.002$^{}$ & 0.003$^{}$  \\
 &  (1.192) & (1.150) & (0.132) & (0.130) & (0.060) & (0.052)  \\
Constant  &  13.468$^{***}$ & 7.147$^{}$ & 1.252$^{***}$ & 1.565$^{}$ & 0.408$^{***}$ & 0.880$^{}$  \\
 &  (2.392) & (13.731) & (0.170) & (1.444) & (0.073) & (0.564)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  349 & 349 & 349 & 349 & 349 & 349  \\
Adjusted $R^2$ &  0.005 & -0.001 & 0.005 & 0.005 & 0.004 & 0.026  \\
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
Treatment  &  1.482$^{*}$ & 1.606$^{**}$ & 0.176$^{*}$ & 0.184$^{**}$ & 0.124$^{*}$ & 0.129$^{*}$  \\
 &  (0.606) & (0.615) & (0.068) & (0.070) & (0.048) & (0.050)  \\
Constant  &  -0.213$^{}$ & -0.041$^{}$ & 0.032$^{}$ & 0.246$^{}$ & 0.001$^{}$ & 0.029$^{}$  \\
 &  (0.409) & (4.611) & (0.082) & (0.648) & (0.052) & (0.444)  \\
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
Treatment  &  -1.129$^{}$ & -1.368$^{}$ & 0.000$^{}$ & -0.030$^{}$ & -0.060$^{}$ & -0.062$^{}$  \\
 &  (1.179) & (1.175) & (0.114) & (0.117) & (0.064) & (0.059)  \\
Constant  &  13.680$^{***}$ & 7.188$^{}$ & 1.221$^{***}$ & 1.319$^{}$ & 0.436$^{***}$ & 0.785$^{}$  \\
 &  (2.389) & (12.651) & (0.151) & (1.192) & (0.080) & (0.579)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  349 & 349 & 349 & 349 & 349 & 349  \\
Adjusted $R^2$ &  -0.000 & -0.006 & -0.007 & 0.004 & 0.002 & 0.007  \\
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
Treatment  &  2.222$^{}$ & 2.694$^{}$ & 0.087$^{}$ & 0.072$^{}$ & 0.124$^{}$ & 0.118$^{}$  \\
 &  (1.368) & (1.770) & (0.162) & (0.212) & (0.090) & (0.093)  \\
Constant  &  7.242$^{***}$ & 15.917$^{}$ & 1.405$^{***}$ & 4.106$^{**}$ & 0.908$^{***}$ & 2.446$^{***}$  \\
 &  (1.945) & (13.334) & (0.327) & (1.445) & (0.184) & (0.658)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  142 & 142 & 142 & 142 & 142 & 142  \\
Adjusted $R^2$ &  0.035 & 0.082 & 0.078 & 0.069 & 0.107 & 0.132  \\
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
Treatment  &  2.020$^{}$ & 2.872$^{}$ & 0.145$^{}$ & 0.137$^{}$ & 0.150$^{}$ & 0.165$^{+}$  \\
 &  (1.459) & (1.749) & (0.144) & (0.182) & (0.096) & (0.089)  \\
Constant  &  3.091$^{}$ & 12.299$^{}$ & 0.702$^{*}$ & 2.002$^{+}$ & 0.615$^{**}$ & 2.150$^{**}$  \\
 &  (2.198) & (11.220) & (0.302) & (1.068) & (0.221) & (0.690)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  142 & 142 & 142 & 142 & 142 & 142  \\
Adjusted $R^2$ &  0.045 & 0.110 & 0.044 & 0.035 & 0.102 & 0.128  \\
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
F-statistic: 3.707 
p-value: 0.0052 
Degrees of freedom: 4 

The treatment effect on Black speaker representation varies significantly across disciplines (p < 0.05).
This indicates that the diversity intervention has heterogeneous effects depending on the academic field.

\textbf{F-test for Treatment × Discipline Interactions (URM Speakers):}
F-statistic: 0.583 
p-value: 0.6753 
Degrees of freedom: 4 

\textbf{F-test for Treatment × Discipline Interactions (% Black Speakers):}
F-statistic: 2.528 
p-value: 0.039 
Degrees of freedom: 4 

\textbf{F-test for Treatment × Discipline Interactions (Total Black Speakers):}
F-statistic: 4.104 
p-value: 0.0026 
Degrees of freedom: 4 

\textbf{Individual Interaction Effects (Black Speakers):}
                                      Estimate Std. Error t value Pr(>|t|)
treatment:disc_mathematics             -0.0659     0.0603 -1.0923   0.2749
treatment:disc_physics                  0.0183     0.0683  0.2673   0.7893
treatment:disc_computer_science        -0.1134     0.0876 -1.2945   0.1957
treatment:disc_mechanical_engineering   0.2740     0.1055  2.5961   0.0095

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
Treatment  &  0.666$^{}$ & 0.811$^{}$ & 0.028$^{}$ & 0.035$^{}$ & -0.005$^{}$ & -0.002$^{}$  \\
 &  (0.768) & (0.804) & (0.055) & (0.056) & (0.028) & (0.028)  \\
Constant  &  6.394$^{***}$ & 7.010$^{*}$ & 0.808$^{***}$ & 0.715$^{**}$ & 0.483$^{***}$ & 0.379$^{**}$  \\
 &  (1.627) & (2.849) & (0.135) & (0.235) & (0.068) & (0.118)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,390 & 1,390 & 1,390 & 1,390 & 1,390 & 1,390  \\
Adjusted $R^2$ &  0.008 & 0.009 & 0.025 & 0.022 & 0.027 & 0.030  \\
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
Treatment  &  0.887$^{+}$ & 0.918$^{*}$ & 0.039$^{}$ & 0.042$^{}$ & 0.029$^{}$ & 0.031$^{}$  \\
 &  (0.454) & (0.428) & (0.035) & (0.034) & (0.023) & (0.023)  \\
Constant  &  1.614$^{+}$ & 1.420$^{}$ & 0.297$^{***}$ & 0.287$^{*}$ & 0.212$^{***}$ & 0.159$^{}$  \\
 &  (0.971) & (1.651) & (0.083) & (0.143) & (0.053) & (0.097)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,390 & 1,390 & 1,390 & 1,390 & 1,390 & 1,390  \\
Adjusted $R^2$ &  0.013 & 0.013 & 0.032 & 0.034 & 0.024 & 0.024  \\
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
Treatment  &  -0.200$^{}$ & -0.093$^{}$ & -0.010$^{}$ & -0.007$^{}$ & -0.029$^{}$ & -0.028$^{}$  \\
 &  (0.672) & (0.719) & (0.040) & (0.040) & (0.027) & (0.027)  \\
Constant  &  4.557$^{**}$ & 5.362$^{*}$ & 0.493$^{***}$ & 0.406$^{*}$ & 0.358$^{***}$ & 0.292$^{**}$  \\
 &  (1.387) & (2.532) & (0.102) & (0.173) & (0.067) & (0.105)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,390 & 1,390 & 1,390 & 1,390 & 1,390 & 1,390  \\
Adjusted $R^2$ &  -0.004 & -0.002 & 0.006 & 0.007 & 0.014 & 0.016  \\
\bottomrule
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize \vspace{2pt}Clustered standard errors at department level in parentheses.}}\\
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize $^{+}p<0.1$; $^{*}p<0.05$; $^{**}p<0.01$; $^{***}p<0.001$\vspace{2pt}}}\\
\end{tabularx}
\end{table}

\newpage

# Heterogeneity Analysis

## Moderation by Department Ranking

\begin{table}[H]
\caption{Moderation by Department Ranking: URM Speakers}
\label{tab:mod_department_ranking_urm}
\centering
\scriptsize
\begin{tabularx}{\textwidth}{l*{6}{>{\centering\arraybackslash}X}}
\toprule
 & Model 1 & Model 2 & Model 3 & Model 4 & Model 5 & Model 6 \\
 &  (1) & (2) & (3) & (4) & (5) & (6)  \\
\midrule
Treatment  &  0.757$^{}$ & 0.770$^{}$ & 0.104$^{}$ & 0.075$^{}$ & 0.022$^{}$ & 0.013$^{}$  \\
 &  (0.519) & (0.515) & (0.065) & (0.063) & (0.025) & (0.023)  \\
Constant  &  8.877$^{***}$ & 4.995$^{*}$ & 1.017$^{***}$ & 0.203$^{}$ & 0.502$^{***}$ & 0.183$^{+}$  \\
 &  (1.644) & (1.961) & (0.174) & (0.245) & (0.072) & (0.107)  \\
Department Ranking  &  0.022$^{+}$ & 0.035$^{**}$ & -0.003$^{**}$ & -0.001$^{}$ & -0.001$^{**}$ & -0.001$^{}$  \\
 &  (0.013) & (0.013) & (0.001) & (0.001) & (0.001) & (0.001)  \\
Treatment $\times$ Department Ranking  &  0.006$^{}$ & 0.005$^{}$ & 0.005$^{**}$ & 0.005$^{**}$ & 0.001$^{+}$ & 0.001$^{+}$  \\
 &  (0.016) & (0.016) & (0.002) & (0.002) & (0.001) & (0.001)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,654 & 1,654 & 1,654 & 1,654 & 1,654 & 1,654  \\
Adjusted $R^2$ &  0.013 & 0.016 & 0.035 & 0.044 & 0.033 & 0.043  \\
\bottomrule
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize \vspace{2pt}Clustered standard errors at department level in parentheses.}}\\
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize $^{+}p<0.1$; $^{*}p<0.05$; $^{**}p<0.01$; $^{***}p<0.001$\vspace{2pt}}}\\
\end{tabularx}
\end{table}


\begin{table}[H]
\caption{Moderation by Department Ranking: Black Speakers}
\label{tab:mod_department_ranking_black}
\centering
\scriptsize
\begin{tabularx}{\textwidth}{l*{6}{>{\centering\arraybackslash}X}}
\toprule
 & Model 1 & Model 2 & Model 3 & Model 4 & Model 5 & Model 6 \\
 &  (1) & (2) & (3) & (4) & (5) & (6)  \\
\midrule
Treatment  &  0.655$^{*}$ & 0.652$^{*}$ & 0.083$^{*}$ & 0.081$^{*}$ & 0.058$^{*}$ & 0.055$^{*}$  \\
 &  (0.303) & (0.286) & (0.039) & (0.037) & (0.022) & (0.022)  \\
Constant  &  2.960$^{***}$ & 1.284$^{}$ & 0.466$^{***}$ & 0.158$^{}$ & 0.246$^{***}$ & 0.038$^{}$  \\
 &  (0.801) & (1.129) & (0.111) & (0.147) & (0.063) & (0.095)  \\
Department Ranking  &  0.005$^{}$ & 0.010$^{}$ & -0.000$^{}$ & 0.000$^{}$ & -0.001$^{*}$ & -0.000$^{}$  \\
 &  (0.007) & (0.008) & (0.001) & (0.001) & (0.000) & (0.001)  \\
Treatment $\times$ Department Ranking  &  0.006$^{}$ & 0.004$^{}$ & 0.003$^{*}$ & 0.002$^{*}$ & 0.001$^{+}$ & 0.001$^{+}$  \\
 &  (0.009) & (0.009) & (0.001) & (0.001) & (0.001) & (0.001)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,654 & 1,654 & 1,654 & 1,654 & 1,654 & 1,654  \\
Adjusted $R^2$ &  0.027 & 0.032 & 0.052 & 0.060 & 0.038 & 0.046  \\
\bottomrule
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize \vspace{2pt}Clustered standard errors at department level in parentheses.}}\\
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize $^{+}p<0.1$; $^{*}p<0.05$; $^{**}p<0.01$; $^{***}p<0.001$\vspace{2pt}}}\\
\end{tabularx}
\end{table}


\begin{table}[H]
\caption{Moderation by Department Ranking: Hispanic Speakers}
\label{tab:mod_department_ranking_hispanic}
\centering
\scriptsize
\begin{tabularx}{\textwidth}{l*{6}{>{\centering\arraybackslash}X}}
\toprule
 & Model 1 & Model 2 & Model 3 & Model 4 & Model 5 & Model 6 \\
 &  (1) & (2) & (3) & (4) & (5) & (6)  \\
\midrule
Treatment  &  0.118$^{}$ & 0.124$^{}$ & 0.021$^{}$ & -0.008$^{}$ & -0.013$^{}$ & -0.025$^{}$  \\
 &  (0.472) & (0.482) & (0.049) & (0.048) & (0.025) & (0.025)  \\
Constant  &  5.640$^{***}$ & 3.427$^{+}$ & 0.515$^{***}$ & 0.001$^{}$ & 0.380$^{***}$ & 0.145$^{}$  \\
 &  (1.564) & (1.841) & (0.150) & (0.201) & (0.073) & (0.100)  \\
Department Ranking  &  0.016$^{}$ & 0.024$^{*}$ & -0.003$^{**}$ & -0.001$^{}$ & -0.001$^{+}$ & -0.000$^{}$  \\
 &  (0.011) & (0.011) & (0.001) & (0.001) & (0.001) & (0.001)  \\
Treatment $\times$ Department Ranking  &  0.000$^{}$ & 0.001$^{}$ & 0.002$^{+}$ & 0.003$^{*}$ & 0.001$^{}$ & 0.001$^{}$  \\
 &  (0.014) & (0.014) & (0.001) & (0.001) & (0.001) & (0.001)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,654 & 1,654 & 1,654 & 1,654 & 1,654 & 1,654  \\
Adjusted $R^2$ &  0.005 & 0.005 & 0.017 & 0.022 & 0.021 & 0.025  \\
\bottomrule
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize \vspace{2pt}Clustered standard errors at department level in parentheses.}}\\
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize $^{+}p<0.1$; $^{*}p<0.05$; $^{**}p<0.01$; $^{***}p<0.001$\vspace{2pt}}}\\
\end{tabularx}
\end{table}


\begin{table}[H]
\caption{Moderation by Department Ranking: Female Speakers}
\label{tab:mod_department_ranking_female}
\centering
\scriptsize
\begin{tabularx}{\textwidth}{l*{6}{>{\centering\arraybackslash}X}}
\toprule
 & Model 1 & Model 2 & Model 3 & Model 4 & Model 5 & Model 6 \\
 &  (1) & (2) & (3) & (4) & (5) & (6)  \\
\midrule
Treatment  &  -0.024$^{}$ & -0.547$^{}$ & -0.056$^{}$ & -0.146$^{}$ & 0.004$^{}$ & -0.004$^{}$  \\
 &  (0.835) & (0.812) & (0.128) & (0.125) & (0.022) & (0.022)  \\
Constant  &  21.094$^{***}$ & 13.475$^{***}$ & 3.127$^{***}$ & 1.823$^{***}$ & 0.806$^{***}$ & 0.667$^{***}$  \\
 &  (2.243) & (3.710) & (0.373) & (0.551) & (0.071) & (0.096)  \\
Department Ranking  &  -0.018$^{}$ & -0.009$^{}$ & -0.011$^{***}$ & -0.010$^{***}$ & -0.002$^{***}$ & -0.001$^{**}$  \\
 &  (0.018) & (0.019) & (0.003) & (0.003) & (0.000) & (0.000)  \\
Treatment $\times$ Department Ranking  &  0.019$^{}$ & 0.024$^{}$ & 0.007$^{*}$ & 0.007$^{*}$ & 0.001$^{+}$ & 0.001$^{*}$  \\
 &  (0.023) & (0.023) & (0.003) & (0.003) & (0.001) & (0.001)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,654 & 1,654 & 1,654 & 1,654 & 1,654 & 1,654  \\
Adjusted $R^2$ &  0.053 & 0.061 & 0.094 & 0.101 & 0.023 & 0.026  \\
\bottomrule
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize \vspace{2pt}Clustered standard errors at department level in parentheses.}}\\
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize $^{+}p<0.1$; $^{*}p<0.05$; $^{**}p<0.01$; $^{***}p<0.001$\vspace{2pt}}}\\
\end{tabularx}
\end{table}

\newpage

## Moderation by Total Faculty Size

\begin{table}[H]
\caption{Moderation by Total Faculty: URM Speakers}
\label{tab:mod_total_faculty_urm}
\centering
\scriptsize
\begin{tabularx}{\textwidth}{l*{6}{>{\centering\arraybackslash}X}}
\toprule
 & Model 1 & Model 2 & Model 3 & Model 4 & Model 5 & Model 6 \\
 &  (1) & (2) & (3) & (4) & (5) & (6)  \\
\midrule
Treatment  &  1.043$^{+}$ & 0.816$^{}$ & 0.088$^{}$ & 0.080$^{}$ & 0.015$^{}$ & 0.016$^{}$  \\
 &  (0.537) & (0.514) & (0.068) & (0.064) & (0.025) & (0.023)  \\
Constant  &  7.211$^{***}$ & 2.085$^{}$ & 1.033$^{***}$ & 0.146$^{}$ & 0.531$^{***}$ & 0.171$^{}$  \\
 &  (1.537) & (2.020) & (0.176) & (0.281) & (0.067) & (0.110)  \\
Total Faculty  &  -0.051$^{+}$ & -0.040$^{}$ & 0.002$^{}$ & 0.001$^{}$ & 0.000$^{}$ & -0.001$^{}$  \\
 &  (0.026) & (0.026) & (0.003) & (0.003) & (0.001) & (0.001)  \\
Treatment $\times$ Total Faculty  &  0.042$^{}$ & 0.028$^{}$ & -0.000$^{}$ & -0.002$^{}$ & 0.001$^{}$ & 0.001$^{}$  \\
 &  (0.029) & (0.029) & (0.003) & (0.003) & (0.001) & (0.001)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,654 & 1,654 & 1,654 & 1,654 & 1,654 & 1,654  \\
Adjusted $R^2$ &  0.011 & 0.016 & 0.030 & 0.038 & 0.030 & 0.042  \\
\bottomrule
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize \vspace{2pt}Clustered standard errors at department level in parentheses.}}\\
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize $^{+}p<0.1$; $^{*}p<0.05$; $^{**}p<0.01$; $^{***}p<0.001$\vspace{2pt}}}\\
\end{tabularx}
\end{table}


\begin{table}[H]
\caption{Moderation by Total Faculty: Black Speakers}
\label{tab:mod_total_faculty_black}
\centering
\scriptsize
\begin{tabularx}{\textwidth}{l*{6}{>{\centering\arraybackslash}X}}
\toprule
 & Model 1 & Model 2 & Model 3 & Model 4 & Model 5 & Model 6 \\
 &  (1) & (2) & (3) & (4) & (5) & (6)  \\
\midrule
Treatment  &  0.767$^{*}$ & 0.652$^{*}$ & 0.092$^{*}$ & 0.080$^{*}$ & 0.057$^{*}$ & 0.054$^{*}$  \\
 &  (0.307) & (0.285) & (0.041) & (0.037) & (0.023) & (0.022)  \\
Constant  &  2.584$^{***}$ & 0.074$^{}$ & 0.449$^{***}$ & 0.024$^{}$ & 0.289$^{***}$ & 0.005$^{}$  \\
 &  (0.761) & (1.300) & (0.100) & (0.169) & (0.062) & (0.103)  \\
Total Faculty  &  -0.014$^{}$ & -0.014$^{}$ & -0.000$^{}$ & -0.000$^{}$ & 0.001$^{}$ & -0.000$^{}$  \\
 &  (0.010) & (0.010) & (0.001) & (0.002) & (0.001) & (0.001)  \\
Treatment $\times$ Total Faculty  &  0.003$^{}$ & -0.004$^{}$ & -0.002$^{}$ & -0.003$^{+}$ & -0.001$^{}$ & -0.002$^{}$  \\
 &  (0.014) & (0.014) & (0.002) & (0.002) & (0.001) & (0.001)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,654 & 1,654 & 1,654 & 1,654 & 1,654 & 1,654  \\
Adjusted $R^2$ &  0.027 & 0.032 & 0.048 & 0.057 & 0.036 & 0.046  \\
\bottomrule
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize \vspace{2pt}Clustered standard errors at department level in parentheses.}}\\
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize $^{+}p<0.1$; $^{*}p<0.05$; $^{**}p<0.01$; $^{***}p<0.001$\vspace{2pt}}}\\
\end{tabularx}
\end{table}


\begin{table}[H]
\caption{Moderation by Total Faculty: Hispanic Speakers}
\label{tab:mod_total_faculty_hispanic}
\centering
\scriptsize
\begin{tabularx}{\textwidth}{l*{6}{>{\centering\arraybackslash}X}}
\toprule
 & Model 1 & Model 2 & Model 3 & Model 4 & Model 5 & Model 6 \\
 &  (1) & (2) & (3) & (4) & (5) & (6)  \\
\midrule
Treatment  &  0.281$^{}$ & 0.168$^{}$ & -0.006$^{}$ & -0.002$^{}$ & -0.023$^{}$ & -0.021$^{}$  \\
 &  (0.487) & (0.480) & (0.049) & (0.048) & (0.025) & (0.025)  \\
Constant  &  4.421$^{**}$ & 1.834$^{}$ & 0.555$^{***}$ & 0.093$^{}$ & 0.378$^{***}$ & 0.175$^{}$  \\
 &  (1.497) & (1.781) & (0.152) & (0.208) & (0.070) & (0.107)  \\
Total Faculty  &  -0.035$^{}$ & -0.025$^{}$ & 0.003$^{}$ & 0.001$^{}$ & 0.000$^{}$ & -0.000$^{}$  \\
 &  (0.026) & (0.026) & (0.003) & (0.003) & (0.001) & (0.001)  \\
Treatment $\times$ Total Faculty  &  0.037$^{}$ & 0.030$^{}$ & 0.002$^{}$ & 0.001$^{}$ & 0.002$^{}$ & 0.002$^{}$  \\
 &  (0.027) & (0.027) & (0.003) & (0.003) & (0.001) & (0.001)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,654 & 1,654 & 1,654 & 1,654 & 1,654 & 1,654  \\
Adjusted $R^2$ &  0.004 & 0.006 & 0.017 & 0.020 & 0.023 & 0.025  \\
\bottomrule
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize \vspace{2pt}Clustered standard errors at department level in parentheses.}}\\
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize $^{+}p<0.1$; $^{*}p<0.05$; $^{**}p<0.01$; $^{***}p<0.001$\vspace{2pt}}}\\
\end{tabularx}
\end{table}


\begin{table}[H]
\caption{Moderation by Total Faculty: Female Speakers}
\label{tab:mod_total_faculty_female}
\centering
\scriptsize
\begin{tabularx}{\textwidth}{l*{6}{>{\centering\arraybackslash}X}}
\toprule
 & Model 1 & Model 2 & Model 3 & Model 4 & Model 5 & Model 6 \\
 &  (1) & (2) & (3) & (4) & (5) & (6)  \\
\midrule
Treatment  &  -0.107$^{}$ & -0.490$^{}$ & -0.127$^{}$ & -0.145$^{}$ & -0.009$^{}$ & -0.004$^{}$  \\
 &  (0.819) & (0.809) & (0.129) & (0.125) & (0.022) & (0.022)  \\
Constant  &  21.280$^{***}$ & 13.612$^{***}$ & 3.633$^{***}$ & 2.251$^{***}$ & 0.874$^{***}$ & 0.733$^{***}$  \\
 &  (2.361) & (3.713) & (0.349) & (0.595) & (0.060) & (0.103)  \\
Total Faculty  &  0.003$^{}$ & -0.005$^{}$ & 0.012$^{*}$ & 0.005$^{}$ & 0.002$^{+}$ & 0.001$^{}$  \\
 &  (0.042) & (0.042) & (0.006) & (0.005) & (0.001) & (0.001)  \\
Treatment $\times$ Total Faculty  &  0.014$^{}$ & 0.015$^{}$ & -0.009$^{}$ & -0.008$^{}$ & -0.001$^{}$ & -0.001$^{}$  \\
 &  (0.062) & (0.063) & (0.006) & (0.006) & (0.001) & (0.001)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,654 & 1,654 & 1,654 & 1,654 & 1,654 & 1,654  \\
Adjusted $R^2$ &  0.053 & 0.061 & 0.085 & 0.099 & 0.018 & 0.024  \\
\bottomrule
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize \vspace{2pt}Clustered standard errors at department level in parentheses.}}\\
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize $^{+}p<0.1$; $^{*}p<0.05$; $^{**}p<0.01$; $^{***}p<0.001$\vspace{2pt}}}\\
\end{tabularx}
\end{table}

\newpage

## Moderation by URM Faculty in Peer Departments

\begin{table}[H]
\caption{Moderation by Peer URM Faculty: URM Speakers}
\label{tab:mod_peer_urm_faculty_urm}
\centering
\scriptsize
\begin{tabularx}{\textwidth}{l*{6}{>{\centering\arraybackslash}X}}
\toprule
 & Model 1 & Model 2 & Model 3 & Model 4 & Model 5 & Model 6 \\
 &  (1) & (2) & (3) & (4) & (5) & (6)  \\
\midrule
Treatment  &  0.808$^{}$ & 0.759$^{}$ & 0.108$^{+}$ & 0.080$^{}$ & 0.022$^{}$ & 0.014$^{}$  \\
 &  (0.528) & (0.520) & (0.064) & (0.063) & (0.024) & (0.023)  \\
Constant  &  7.283$^{***}$ & 6.890$^{***}$ & 1.004$^{***}$ & 0.739$^{***}$ & 0.534$^{***}$ & 0.400$^{***}$  \\
 &  (1.591) & (1.819) & (0.162) & (0.223) & (0.064) & (0.096)  \\
Peer URM Faculty  &  0.052$^{}$ & 0.135$^{*}$ & 0.017$^{**}$ & 0.021$^{***}$ & 0.007$^{**}$ & 0.007$^{**}$  \\
 &  (0.054) & (0.054) & (0.005) & (0.006) & (0.002) & (0.002)  \\
Treatment $\times$ Peer URM Faculty  &  -0.051$^{}$ & -0.038$^{}$ & -0.005$^{}$ & -0.006$^{}$ & -0.001$^{}$ & -0.001$^{}$  \\
 &  (0.072) & (0.071) & (0.008) & (0.008) & (0.003) & (0.003)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,654 & 1,654 & 1,654 & 1,654 & 1,654 & 1,654  \\
Adjusted $R^2$ &  0.009 & 0.016 & 0.036 & 0.039 & 0.037 & 0.041  \\
\bottomrule
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize \vspace{2pt}Clustered standard errors at department level in parentheses.}}\\
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize $^{+}p<0.1$; $^{*}p<0.05$; $^{**}p<0.01$; $^{***}p<0.001$\vspace{2pt}}}\\
\end{tabularx}
\end{table}


\begin{table}[H]
\caption{Moderation by Peer URM Faculty: Black Speakers}
\label{tab:mod_peer_urm_faculty_black}
\centering
\scriptsize
\begin{tabularx}{\textwidth}{l*{6}{>{\centering\arraybackslash}X}}
\toprule
 & Model 1 & Model 2 & Model 3 & Model 4 & Model 5 & Model 6 \\
 &  (1) & (2) & (3) & (4) & (5) & (6)  \\
\midrule
Treatment  &  0.674$^{*}$ & 0.659$^{*}$ & 0.086$^{*}$ & 0.085$^{*}$ & 0.058$^{**}$ & 0.058$^{*}$  \\
 &  (0.302) & (0.286) & (0.039) & (0.037) & (0.023) & (0.022)  \\
Constant  &  2.460$^{**}$ & 2.126$^{*}$ & 0.406$^{***}$ & 0.345$^{*}$ & 0.263$^{***}$ & 0.209$^{*}$  \\
 &  (0.751) & (0.967) & (0.099) & (0.140) & (0.059) & (0.083)  \\
Peer URM Faculty  &  0.013$^{}$ & 0.041$^{}$ & 0.003$^{}$ & 0.007$^{+}$ & 0.003$^{}$ & 0.003$^{}$  \\
 &  (0.023) & (0.029) & (0.003) & (0.004) & (0.002) & (0.002)  \\
Treatment $\times$ Peer URM Faculty  &  -0.005$^{}$ & 0.003$^{}$ & 0.000$^{}$ & 0.001$^{}$ & 0.002$^{}$ & 0.003$^{}$  \\
 &  (0.037) & (0.037) & (0.005) & (0.005) & (0.003) & (0.003)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,654 & 1,654 & 1,654 & 1,654 & 1,654 & 1,654  \\
Adjusted $R^2$ &  0.026 & 0.032 & 0.048 & 0.056 & 0.041 & 0.045  \\
\bottomrule
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize \vspace{2pt}Clustered standard errors at department level in parentheses.}}\\
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize $^{+}p<0.1$; $^{*}p<0.05$; $^{**}p<0.01$; $^{***}p<0.001$\vspace{2pt}}}\\
\end{tabularx}
\end{table}


\begin{table}[H]
\caption{Moderation by Peer URM Faculty: Hispanic Speakers}
\label{tab:mod_peer_urm_faculty_hispanic}
\centering
\scriptsize
\begin{tabularx}{\textwidth}{l*{6}{>{\centering\arraybackslash}X}}
\toprule
 & Model 1 & Model 2 & Model 3 & Model 4 & Model 5 & Model 6 \\
 &  (1) & (2) & (3) & (4) & (5) & (6)  \\
\midrule
Treatment  &  0.149$^{}$ & 0.105$^{}$ & 0.021$^{}$ & -0.007$^{}$ & -0.012$^{}$ & -0.024$^{}$  \\
 &  (0.478) & (0.487) & (0.048) & (0.048) & (0.025) & (0.025)  \\
Constant  &  4.608$^{**}$ & 4.461$^{*}$ & 0.572$^{***}$ & 0.349$^{+}$ & 0.401$^{***}$ & 0.284$^{**}$  \\
 &  (1.477) & (1.736) & (0.135) & (0.188) & (0.068) & (0.086)  \\
Peer URM Faculty  &  0.040$^{}$ & 0.093$^{+}$ & 0.014$^{***}$ & 0.014$^{**}$ & 0.005$^{*}$ & 0.005$^{+}$  \\
 &  (0.050) & (0.052) & (0.004) & (0.005) & (0.002) & (0.003)  \\
Treatment $\times$ Peer URM Faculty  &  -0.047$^{}$ & -0.043$^{}$ & -0.005$^{}$ & -0.006$^{}$ & -0.000$^{}$ & -0.001$^{}$  \\
 &  (0.063) & (0.064) & (0.006) & (0.006) & (0.003) & (0.003)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,654 & 1,654 & 1,654 & 1,654 & 1,654 & 1,654  \\
Adjusted $R^2$ &  0.003 & 0.005 & 0.021 & 0.020 & 0.024 & 0.024  \\
\bottomrule
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize \vspace{2pt}Clustered standard errors at department level in parentheses.}}\\
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize $^{+}p<0.1$; $^{*}p<0.05$; $^{**}p<0.01$; $^{***}p<0.001$\vspace{2pt}}}\\
\end{tabularx}
\end{table}


\begin{table}[H]
\caption{Moderation by Peer URM Faculty: Female Speakers}
\label{tab:mod_peer_urm_faculty_female}
\centering
\scriptsize
\begin{tabularx}{\textwidth}{l*{6}{>{\centering\arraybackslash}X}}
\toprule
 & Model 1 & Model 2 & Model 3 & Model 4 & Model 5 & Model 6 \\
 &  (1) & (2) & (3) & (4) & (5) & (6)  \\
\midrule
Treatment  &  -0.034$^{}$ & -0.602$^{}$ & -0.063$^{}$ & -0.133$^{}$ & 0.003$^{}$ & -0.003$^{}$  \\
 &  (0.824) & (0.812) & (0.127) & (0.126) & (0.022) & (0.022)  \\
Constant  &  21.205$^{***}$ & 15.397$^{***}$ & 3.534$^{***}$ & 2.558$^{***}$ & 0.860$^{***}$ & 0.779$^{***}$  \\
 &  (2.069) & (3.419) & (0.332) & (0.417) & (0.060) & (0.076)  \\
Peer URM Faculty  &  0.162$^{*}$ & 0.174$^{*}$ & 0.021$^{+}$ & 0.009$^{}$ & 0.005$^{**}$ & 0.003$^{+}$  \\
 &  (0.075) & (0.082) & (0.011) & (0.013) & (0.002) & (0.002)  \\
Treatment $\times$ Peer URM Faculty  &  -0.184$^{+}$ & -0.199$^{*}$ & 0.006$^{}$ & 0.003$^{}$ & -0.002$^{}$ & -0.002$^{}$  \\
 &  (0.095) & (0.099) & (0.014) & (0.014) & (0.002) & (0.002)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,654 & 1,654 & 1,654 & 1,654 & 1,654 & 1,654  \\
Adjusted $R^2$ &  0.056 & 0.063 & 0.088 & 0.098 & 0.020 & 0.024  \\
\bottomrule
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize \vspace{2pt}Clustered standard errors at department level in parentheses.}}\\
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize $^{+}p<0.1$; $^{*}p<0.05$; $^{**}p<0.01$; $^{***}p<0.001$\vspace{2pt}}}\\
\end{tabularx}
\end{table}

\newpage

## Moderation by % Female Email Recipients


### Error: Moderator variable 'pct_female_recipients' not found in data

\newpage

## Moderation by % URM Email Recipients


### Error: Moderator variable 'pct_urm_recipients' not found in data

\newpage

## Moderation by % URM Faculty in Department

\begin{table}[H]
\caption{Moderation by % URM Faculty: URM Speakers}
\label{tab:mod___urm_faculty_urm}
\centering
\scriptsize
\begin{tabularx}{\textwidth}{l*{6}{>{\centering\arraybackslash}X}}
\toprule
 & Model 1 & Model 2 & Model 3 & Model 4 & Model 5 & Model 6 \\
 &  (1) & (2) & (3) & (4) & (5) & (6)  \\
\midrule
Treatment  &  -0.425$^{}$ & -0.255$^{}$ & -0.025$^{}$ & -0.040$^{}$ & 0.009$^{}$ & 0.001$^{}$  \\
 &  (0.746) & (0.738) & (0.093) & (0.092) & (0.034) & (0.033)  \\
Constant  &  7.478$^{***}$ & 3.562$^{+}$ & 1.057$^{***}$ & 0.191$^{}$ & 0.556$^{***}$ & 0.199$^{+}$  \\
 &  (1.655) & (2.074) & (0.170) & (0.272) & (0.067) & (0.116)  \\
\% URM Faculty  &  -8.383$^{}$ & -6.528$^{}$ & -0.794$^{}$ & -0.982$^{}$ & -0.146$^{}$ & -0.320$^{}$  \\
 &  (9.756) & (9.705) & (1.213) & (1.156) & (0.546) & (0.508)  \\
Treatment $\times$ \% URM Faculty  &  32.301$^{*}$ & 28.599$^{+}$ & 3.379$^{+}$ & 3.406$^{+}$ & 0.310$^{}$ & 0.367$^{}$  \\
 &  (15.556) & (15.306) & (1.965) & (1.938) & (0.664) & (0.647)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,654 & 1,654 & 1,654 & 1,654 & 1,654 & 1,654  \\
Adjusted $R^2$ &  0.012 & 0.018 & 0.032 & 0.041 & 0.028 & 0.042  \\
\bottomrule
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize \vspace{2pt}Clustered standard errors at department level in parentheses.}}\\
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize $^{+}p<0.1$; $^{*}p<0.05$; $^{**}p<0.01$; $^{***}p<0.001$\vspace{2pt}}}\\
\end{tabularx}
\end{table}


\begin{table}[H]
\caption{Moderation by % URM Faculty: Black Speakers}
\label{tab:mod___urm_faculty_black}
\centering
\scriptsize
\begin{tabularx}{\textwidth}{l*{6}{>{\centering\arraybackslash}X}}
\toprule
 & Model 1 & Model 2 & Model 3 & Model 4 & Model 5 & Model 6 \\
 &  (1) & (2) & (3) & (4) & (5) & (6)  \\
\midrule
Treatment  &  0.013$^{}$ & 0.074$^{}$ & -0.001$^{}$ & 0.005$^{}$ & 0.020$^{}$ & 0.021$^{}$  \\
 &  (0.361) & (0.361) & (0.050) & (0.050) & (0.031) & (0.030)  \\
Constant  &  2.465$^{**}$ & 0.941$^{}$ & 0.420$^{***}$ & 0.126$^{}$ & 0.273$^{***}$ & 0.056$^{}$  \\
 &  (0.774) & (1.286) & (0.103) & (0.164) & (0.059) & (0.104)  \\
\% URM Faculty  &  -0.958$^{}$ & -0.954$^{}$ & -0.562$^{}$ & -0.603$^{}$ & -0.124$^{}$ & -0.245$^{}$  \\
 &  (4.641) & (4.652) & (0.629) & (0.615) & (0.425) & (0.402)  \\
Treatment $\times$ \% URM Faculty  &  16.768$^{*}$ & 16.191$^{+}$ & 2.255$^{*}$ & 2.208$^{*}$ & 0.946$^{}$ & 0.994$^{+}$  \\
 &  (8.342) & (8.278) & (1.086) & (1.024) & (0.586) & (0.565)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,654 & 1,654 & 1,654 & 1,654 & 1,654 & 1,654  \\
Adjusted $R^2$ &  0.031 & 0.034 & 0.051 & 0.059 & 0.037 & 0.046  \\
\bottomrule
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize \vspace{2pt}Clustered standard errors at department level in parentheses.}}\\
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize $^{+}p<0.1$; $^{*}p<0.05$; $^{**}p<0.01$; $^{***}p<0.001$\vspace{2pt}}}\\
\end{tabularx}
\end{table}


\begin{table}[H]
\caption{Moderation by % URM Faculty: Hispanic Speakers}
\label{tab:mod___urm_faculty_hispanic}
\centering
\scriptsize
\begin{tabularx}{\textwidth}{l*{6}{>{\centering\arraybackslash}X}}
\toprule
 & Model 1 & Model 2 & Model 3 & Model 4 & Model 5 & Model 6 \\
 &  (1) & (2) & (3) & (4) & (5) & (6)  \\
\midrule
Treatment  &  -0.447$^{}$ & -0.342$^{}$ & -0.032$^{}$ & -0.054$^{}$ & 0.007$^{}$ & -0.004$^{}$  \\
 &  (0.743) & (0.743) & (0.081) & (0.081) & (0.036) & (0.036)  \\
Constant  &  4.798$^{**}$ & 2.411$^{}$ & 0.612$^{***}$ & 0.031$^{}$ & 0.416$^{***}$ & 0.137$^{}$  \\
 &  (1.548) & (1.897) & (0.143) & (0.215) & (0.070) & (0.108)  \\
\% URM Faculty  &  -7.376$^{}$ & -5.611$^{}$ & -0.321$^{}$ & -0.480$^{}$ & 0.007$^{}$ & -0.067$^{}$  \\
 &  (8.658) & (8.457) & (0.973) & (0.937) & (0.515) & (0.496)  \\
Treatment $\times$ \% URM Faculty  &  16.104$^{}$ & 12.950$^{}$ & 1.334$^{}$ & 1.394$^{}$ & -0.534$^{}$ & -0.548$^{}$  \\
 &  (15.089) & (14.903) & (1.718) & (1.748) & (0.669) & (0.661)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,654 & 1,654 & 1,654 & 1,654 & 1,654 & 1,654  \\
Adjusted $R^2$ &  0.003 & 0.005 & 0.014 & 0.020 & 0.020 & 0.025  \\
\bottomrule
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize \vspace{2pt}Clustered standard errors at department level in parentheses.}}\\
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize $^{+}p<0.1$; $^{*}p<0.05$; $^{**}p<0.01$; $^{***}p<0.001$\vspace{2pt}}}\\
\end{tabularx}
\end{table}


\begin{table}[H]
\caption{Moderation by % URM Faculty: Female Speakers}
\label{tab:mod___urm_faculty_female}
\centering
\scriptsize
\begin{tabularx}{\textwidth}{l*{6}{>{\centering\arraybackslash}X}}
\toprule
 & Model 1 & Model 2 & Model 3 & Model 4 & Model 5 & Model 6 \\
 &  (1) & (2) & (3) & (4) & (5) & (6)  \\
\midrule
Treatment  &  1.003$^{}$ & 0.904$^{}$ & 0.061$^{}$ & 0.014$^{}$ & 0.015$^{}$ & 0.005$^{}$  \\
 &  (1.139) & (1.132) & (0.164) & (0.164) & (0.029) & (0.029)  \\
Constant  &  20.810$^{***}$ & 12.972$^{***}$ & 3.512$^{***}$ & 2.142$^{***}$ & 0.873$^{***}$ & 0.711$^{***}$  \\
 &  (2.165) & (3.821) & (0.332) & (0.584) & (0.062) & (0.101)  \\
\% URM Faculty  &  39.914$^{**}$ & 38.323$^{*}$ & 4.792$^{*}$ & 3.671$^{+}$ & 0.072$^{}$ & -0.080$^{}$  \\
 &  (15.116) & (16.526) & (2.364) & (2.122) & (0.396) & (0.394)  \\
Treatment $\times$ \% URM Faculty  &  -31.800$^{}$ & -39.227$^{}$ & -3.969$^{}$ & -4.107$^{}$ & -0.326$^{}$ & -0.192$^{}$  \\
 &  (23.029) & (24.034) & (3.115) & (2.970) & (0.557) & (0.559)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,654 & 1,654 & 1,654 & 1,654 & 1,654 & 1,654  \\
Adjusted $R^2$ &  0.056 & 0.062 & 0.085 & 0.099 & 0.015 & 0.024  \\
\bottomrule
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize \vspace{2pt}Clustered standard errors at department level in parentheses.}}\\
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize $^{+}p<0.1$; $^{*}p<0.05$; $^{**}p<0.01$; $^{***}p<0.001$\vspace{2pt}}}\\
\end{tabularx}
\end{table}

\newpage

## Moderation by % Women Faculty in Department

\begin{table}[H]
\caption{Moderation by % Women Faculty: URM Speakers}
\label{tab:mod___women_faculty_urm}
\centering
\scriptsize
\begin{tabularx}{\textwidth}{l*{6}{>{\centering\arraybackslash}X}}
\toprule
 & Model 1 & Model 2 & Model 3 & Model 4 & Model 5 & Model 6 \\
 &  (1) & (2) & (3) & (4) & (5) & (6)  \\
\midrule
Treatment  &  1.495$^{}$ & 1.844$^{}$ & 0.184$^{}$ & 0.145$^{}$ & 0.106$^{}$ & 0.081$^{}$  \\
 &  (1.529) & (1.497) & (0.200) & (0.198) & (0.073) & (0.069)  \\
Constant  &  5.751$^{**}$ & 2.882$^{}$ & 0.915$^{***}$ & 0.127$^{}$ & 0.468$^{***}$ & 0.176$^{}$  \\
 &  (1.946) & (2.154) & (0.218) & (0.279) & (0.084) & (0.118)  \\
\% Women Faculty  &  8.003$^{}$ & 8.087$^{}$ & 0.680$^{}$ & 0.693$^{}$ & 0.457$^{}$ & 0.492$^{+}$  \\
 &  (5.031) & (4.932) & (0.726) & (0.708) & (0.281) & (0.264)  \\
Treatment $\times$ \% Women Faculty  &  -4.051$^{}$ & -5.416$^{}$ & -0.447$^{}$ & -0.317$^{}$ & -0.454$^{}$ & -0.338$^{}$  \\
 &  (7.405) & (7.163) & (1.013) & (0.982) & (0.356) & (0.336)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,654 & 1,654 & 1,654 & 1,654 & 1,654 & 1,654  \\
Adjusted $R^2$ &  0.010 & 0.016 & 0.030 & 0.038 & 0.030 & 0.042  \\
\bottomrule
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize \vspace{2pt}Clustered standard errors at department level in parentheses.}}\\
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize $^{+}p<0.1$; $^{*}p<0.05$; $^{**}p<0.01$; $^{***}p<0.001$\vspace{2pt}}}\\
\end{tabularx}
\end{table}


\begin{table}[H]
\caption{Moderation by % Women Faculty: Black Speakers}
\label{tab:mod___women_faculty_black}
\centering
\scriptsize
\begin{tabularx}{\textwidth}{l*{6}{>{\centering\arraybackslash}X}}
\toprule
 & Model 1 & Model 2 & Model 3 & Model 4 & Model 5 & Model 6 \\
 &  (1) & (2) & (3) & (4) & (5) & (6)  \\
\midrule
Treatment  &  0.228$^{}$ & 0.442$^{}$ & 0.050$^{}$ & 0.058$^{}$ & 0.040$^{}$ & 0.042$^{}$  \\
 &  (0.782) & (0.746) & (0.112) & (0.107) & (0.068) & (0.067)  \\
Constant  &  2.108$^{*}$ & 0.770$^{}$ & 0.359$^{**}$ & 0.102$^{}$ & 0.238$^{**}$ & 0.046$^{}$  \\
 &  (0.850) & (1.305) & (0.117) & (0.166) & (0.073) & (0.105)  \\
\% Women Faculty  &  1.350$^{}$ & 1.715$^{}$ & 0.220$^{}$ & 0.273$^{}$ & 0.144$^{}$ & 0.193$^{}$  \\
 &  (2.742) & (2.603) & (0.381) & (0.353) & (0.250) & (0.232)  \\
Treatment $\times$ \% Women Faculty  &  2.053$^{}$ & 1.094$^{}$ & 0.155$^{}$ & 0.133$^{}$ & 0.073$^{}$ & 0.073$^{}$  \\
 &  (4.337) & (3.966) & (0.614) & (0.567) & (0.343) & (0.331)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,654 & 1,654 & 1,654 & 1,654 & 1,654 & 1,654  \\
Adjusted $R^2$ &  0.026 & 0.032 & 0.047 & 0.056 & 0.036 & 0.045  \\
\bottomrule
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize \vspace{2pt}Clustered standard errors at department level in parentheses.}}\\
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize $^{+}p<0.1$; $^{*}p<0.05$; $^{**}p<0.01$; $^{***}p<0.001$\vspace{2pt}}}\\
\end{tabularx}
\end{table}


\begin{table}[H]
\caption{Moderation by % Women Faculty: Hispanic Speakers}
\label{tab:mod___women_faculty_hispanic}
\centering
\scriptsize
\begin{tabularx}{\textwidth}{l*{6}{>{\centering\arraybackslash}X}}
\toprule
 & Model 1 & Model 2 & Model 3 & Model 4 & Model 5 & Model 6 \\
 &  (1) & (2) & (3) & (4) & (5) & (6)  \\
\midrule
Treatment  &  1.228$^{}$ & 1.372$^{}$ & 0.130$^{}$ & 0.082$^{}$ & 0.099$^{}$ & 0.063$^{}$  \\
 &  (1.366) & (1.373) & (0.149) & (0.149) & (0.073) & (0.073)  \\
Constant  &  3.379$^{+}$ & 1.904$^{}$ & 0.515$^{**}$ & -0.011$^{}$ & 0.337$^{***}$ & 0.122$^{}$  \\
 &  (1.809) & (1.956) & (0.177) & (0.223) & (0.081) & (0.109)  \\
\% Women Faculty  &  6.834$^{}$ & 6.551$^{}$ & 0.520$^{}$ & 0.479$^{}$ & 0.446$^{+}$ & 0.425$^{}$  \\
 &  (4.339) & (4.266) & (0.537) & (0.547) & (0.255) & (0.260)  \\
Treatment $\times$ \% Women Faculty  &  -5.861$^{}$ & -6.330$^{}$ & -0.588$^{}$ & -0.438$^{}$ & -0.589$^{+}$ & -0.442$^{}$  \\
 &  (6.261) & (6.223) & (0.703) & (0.699) & (0.337) & (0.340)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,654 & 1,654 & 1,654 & 1,654 & 1,654 & 1,654  \\
Adjusted $R^2$ &  0.004 & 0.005 & 0.014 & 0.020 & 0.021 & 0.025  \\
\bottomrule
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize \vspace{2pt}Clustered standard errors at department level in parentheses.}}\\
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize $^{+}p<0.1$; $^{*}p<0.05$; $^{**}p<0.01$; $^{***}p<0.001$\vspace{2pt}}}\\
\end{tabularx}
\end{table}


\begin{table}[H]
\caption{Moderation by % Women Faculty: Female Speakers}
\label{tab:mod___women_faculty_female}
\centering
\scriptsize
\begin{tabularx}{\textwidth}{l*{6}{>{\centering\arraybackslash}X}}
\toprule
 & Model 1 & Model 2 & Model 3 & Model 4 & Model 5 & Model 6 \\
 &  (1) & (2) & (3) & (4) & (5) & (6)  \\
\midrule
Treatment  &  -2.092$^{}$ & -1.824$^{}$ & 0.345$^{}$ & 0.352$^{}$ & 0.105$^{+}$ & 0.084$^{}$  \\
 &  (2.777) & (2.892) & (0.337) & (0.340) & (0.063) & (0.064)  \\
Constant  &  17.105$^{***}$ & 13.865$^{***}$ & 2.788$^{***}$ & 2.073$^{***}$ & 0.840$^{***}$ & 0.691$^{***}$  \\
 &  (2.868) & (3.844) & (0.405) & (0.590) & (0.076) & (0.101)  \\
\% Women Faculty  &  18.143$^{+}$ & 18.129$^{+}$ & 4.005$^{**}$ & 4.221$^{***}$ & 0.240$^{}$ & 0.261$^{}$  \\
 &  (9.695) & (9.651) & (1.229) & (1.173) & (0.233) & (0.233)  \\
Treatment $\times$ \% Women Faculty  &  8.530$^{}$ & 6.664$^{}$ & -2.368$^{}$ & -2.470$^{}$ & -0.522$^{+}$ & -0.437$^{}$  \\
 &  (13.976) & (14.248) & (1.698) & (1.697) & (0.312) & (0.324)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,654 & 1,654 & 1,654 & 1,654 & 1,654 & 1,654  \\
Adjusted $R^2$ &  0.061 & 0.061 & 0.089 & 0.099 & 0.017 & 0.025  \\
\bottomrule
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize \vspace{2pt}Clustered standard errors at department level in parentheses.}}\\
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize $^{+}p<0.1$; $^{*}p<0.05$; $^{**}p<0.01$; $^{***}p<0.001$\vspace{2pt}}}\\
\end{tabularx}
\end{table}

\newpage

## Moderation by Number of Distinct Seminars


### Error: Moderator variable 'num_distinct_seminars' not found in data

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
Seminars with senior speakers: 1537 (92.9\%)\\[0.3em]
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
\% of speakers & 0.9617 & 0.5704 & & 0.6797 & 0.8575 \\
Count & 0.0634 & 0.0454 & & -0.0236 & -0.0207 \\
Any (0/1) & 0.0247 & 0.0133 & & -0.0117 & -0.0068 \\
\midrule
\textit{Mean (Control)} & & & & & \\
\% of speakers & 6.775 & & & 5.946 & \\
Count & 0.406 & & & 0.400 & \\
Any (0/1) & 0.299 & & & 0.285 & \\
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
\% of speakers & 0.8015+ & 0.6425 & & 0.4454 & 0.5024 \\
Count & 0.0449* & 0.0450* & & 0.0076 & 0.0071 \\
Any (0/1) & 0.0399* & 0.0401* & & 0.0147 & 0.0148 \\
\midrule
\textit{Mean (Control)} & & & & & \\
\% of speakers & 2.007 & & & 1.261 & \\
Count & 0.110 & & & 0.109 & \\
Any (0/1) & 0.094 & & & 0.086 & \\
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
\% of speakers & 0.1317 & -0.1187 & & 0.2343 & 0.3551 \\
Count & 0.0170 & -0.0029 & & -0.0312 & -0.0278 \\
Any (0/1) & -0.0077 & -0.0205 & & -0.0178 & -0.0134 \\
\midrule
\textit{Mean (Control)} & & & & & \\
\% of speakers & 4.755 & & & 4.686 & \\
Count & 0.294 & & & 0.292 & \\
Any (0/1) & 0.233 & & & 0.224 & \\
\bottomrule
\end{tabular}
\parbox{\linewidth}{\footnotesize Note: + p$<$0.1; * p$<$0.05; ** p$<$0.01; *** p$<$0.001. Standard errors clustered at the department level. Junior speakers are defined as those below the median years since PhD; senior speakers are above the median. Model 1 includes baseline controls; Model 2 adds extended controls.}
\end{table}


\clearpage
\section{Summary of All Significant Results}

\begin{landscape}
\begin{table}[H]
\caption{All Significant Results (p < 0.1) from All Analyses - Part 1 of 2}
\label{tab:all_significant_results}
\centering
\tiny
\setlength{\tabcolsep}{2pt}
\begin{tabular}{p{2.8cm}p{1.8cm}p{2.5cm}p{0.8cm}p{1.2cm}p{1.2cm}p{1.0cm}p{1.0cm}c}
\toprule
Analysis & Outcome & Variable & Model & Coef & SE & t-stat & p-val & Sig \\
\midrule
\multicolumn{9}{l}{\textbf{Career Stage Analysis}} \\
\midrule
Junior/Senior Black Speakers & Junior Any (0/1) & Treatment & Simple & 0.0399 & 0.0159 & 2.502 & 0.0125 & * \\
Junior/Senior Black Speakers & Junior Count & Treatment & Simple & 0.0449 & 0.0201 & 2.232 & 0.0257 & * \\
Junior/Senior Black Speakers & Junior \\% of speakers & Treatment & Simple & 0.8015 & 0.4765 & 1.682 & 0.0927 & + \\
\addlinespace[0.5em]
\multicolumn{9}{l}{\textbf{Demographic Subgroups}} \\
\midrule
Demographic Subgroup & \% Black & Treatment & Extended & 0.6576 & 0.2888 & 2.277 & 0.0229 & * \\
Demographic Subgroup & \% Black Female & Treatment & Extended & 0.1465 & 0.0698 & 2.098 & 0.0360 & * \\
Demographic Subgroup & \% Black Male & Treatment & Extended & 0.5111 & 0.2461 & 2.077 & 0.0380 & * \\
Demographic Subgroup & Any Black & Treatment & Extended & 0.0565 & 0.0224 & 2.517 & 0.0119 & * \\
Demographic Subgroup & Any Black Female & Treatment & Extended & 0.0144 & 0.0081 & 1.778 & 0.0756 & + \\
Demographic Subgroup & Any Black Male & Treatment & Simple & 0.0601 & 0.0224 & 2.682 & 0.0074 & ** \\
Demographic Subgroup & Count Black & Treatment & Extended & 0.0844 & 0.0375 & 2.249 & 0.0247 & * \\
Demographic Subgroup & Count Black Male & Treatment & Extended & 0.0733 & 0.0324 & 2.261 & 0.0239 & * \\
\addlinespace[0.5em]
\multicolumn{9}{l}{\textbf{Discipline Analysis}} \\
\midrule
Chemistry & Any Hispanic & Treatment & Extended & -0.1288 & 0.0641 & -2.009 & 0.0456 & * \\
Computer Science & Any Hispanic & Treatment & Extended & 0.1648 & 0.0886 & 1.860 & 0.0655 & + \\
Mathematics & \% URM & Treatment & Extended & 1.4230 & 0.8152 & 1.746 & 0.0813 & + \\
Mathematics & Count Black & Treatment & Extended & 0.1199 & 0.0546 & 2.195 & 0.0284 & * \\
Mathematics & Count URM & Treatment & Simple & 0.1806 & 0.0939 & 1.923 & 0.0548 & + \\
Mechanical Engineering & \% Black & Treatment & Simple & 3.9420 & 0.9989 & 3.946 & 0.0002 & *** \\
Mechanical Engineering & \% URM & Treatment & Simple & 3.8590 & 2.0259 & 1.905 & 0.0613 & + \\
Mechanical Engineering & Any Black & Treatment & Simple & 0.3462 & 0.0898 & 3.855 & 0.0003 & *** \\
Mechanical Engineering & Count Black & Treatment & Simple & 0.6458 & 0.1853 & 3.486 & 0.0009 & *** \\
Mechanical Engineering & Count URM & Treatment & Simple & 0.6652 & 0.2998 & 2.219 & 0.0301 & * \\
Physics & \% Black & Treatment & Extended & 1.6060 & 0.6155 & 2.609 & 0.0095 & ** \\
Physics & Any Black & Treatment & Simple & 0.1244 & 0.0480 & 2.589 & 0.0100 & * \\
Physics & Count Black & Treatment & Extended & 0.1840 & 0.0695 & 2.646 & 0.0085 & ** \\
\addlinespace[0.5em]
\multicolumn{9}{l}{\textbf{Heterogeneity Analysis}} \\
\midrule
Department Ranking & Any Black & Treatment × Department Ranking & Simple & 0.0010 & 0.0006 & 1.733 & 0.0833 & + \\
Department Ranking & Any Female & Treatment × Department Ranking & Extended & 0.0011 & 0.0006 & 1.989 & 0.0469 & * \\
Department Ranking & Any URM & Treatment × Department Ranking & Extended & 0.0012 & 0.0006 & 1.876 & 0.0608 & + \\
Department Ranking & Count Black & Treatment × Department Ranking & Simple & 0.0025 & 0.0012 & 2.184 & 0.0291 & * \\
Department Ranking & Count Female & Treatment × Department Ranking & Extended & 0.0075 & 0.0031 & 2.381 & 0.0174 & * \\
Department Ranking & Count Hispanic & Treatment × Department Ranking & Extended & 0.0027 & 0.0012 & 2.245 & 0.0249 & * \\
Department Ranking & Count URM & Treatment × Department Ranking & Extended & 0.0053 & 0.0018 & 2.975 & 0.0030 & ** \\
Peer URM Faculty & \% Female & Treatment × Peer URM Faculty & Extended & -0.1988 & 0.0995 & -1.999 & 0.0457 & * \\
Total Faculty & Count Black & Treatment × Total Faculty & Extended & -0.0031 & 0.0018 & -1.692 & 0.0908 & + \\
\\% URM Faculty & \% Black & Treatment × \\% URM Faculty & Simple & 16.7675 & 8.3415 & 2.010 & 0.0446 & * \\
\\% URM Faculty & \% URM & Treatment × \\% URM Faculty & Simple & 32.3011 & 15.5565 & 2.076 & 0.0380 & * \\
\\% URM Faculty & Any Black & Treatment × \\% URM Faculty & Extended & 0.9937 & 0.5647 & 1.760 & 0.0786 & + \\
\\% URM Faculty & Count Black & Treatment × \\% URM Faculty & Extended & 2.2082 & 1.0243 & 2.156 & 0.0312 & * \\
\\% URM Faculty & Count URM & Treatment × \\% URM Faculty & Extended & 3.4060 & 1.9384 & 1.757 & 0.0791 & + \\
\\% Women Faculty & Any Female & Treatment × \\% Women Faculty & Simple & -0.5224 & 0.3118 & -1.676 & 0.0940 & + \\
\\% Women Faculty & Any Hispanic & Treatment × \\% Women Faculty & Simple & -0.5888 & 0.3367 & -1.749 & 0.0805 & + \\
\bottomrule
\end{tabular}
\end{table}
\end{landscape}
\clearpage
\begin{landscape}
\begin{table}[H]
\caption{All Significant Results (p < 0.1) from All Analyses - Part 2 of 2}
\label{tab:all_significant_results_2}
\centering
\tiny
\setlength{\tabcolsep}{2pt}
\begin{tabular}{p{2.8cm}p{1.8cm}p{2.5cm}p{0.8cm}p{1.2cm}p{1.2cm}p{1.0cm}p{1.0cm}c}
\toprule
Analysis & Outcome & Variable & Model & Coef & SE & t-stat & p-val & Sig \\
\midrule
\multicolumn{9}{l}{\textbf{Semester Analysis}} \\
\midrule
Fall Semester & Any Black & Treatment & Simple & 0.0434 & 0.0167 & 2.603 & 0.0093 & ** \\
Fall Semester & Count Black & Treatment & Simple & 0.0531 & 0.0209 & 2.541 & 0.0112 & * \\
Fall Semester & Count URM & Treatment & Simple & 0.0778 & 0.0456 & 1.707 & 0.0880 & + \\
Spring Semester & \% Black & Treatment & Extended & 0.9177 & 0.4280 & 2.144 & 0.0322 & * \\
\bottomrule
\end{tabular}
\vspace{0.5em}
\parbox{\linewidth}{\tiny Note: Significance levels: + p<0.1; * p<0.05; ** p<0.01; *** p<0.001. SE = Clustered standard errors at department level. For moderation analyses, only significant interaction terms are shown.}
\end{table}
\end{landscape}
