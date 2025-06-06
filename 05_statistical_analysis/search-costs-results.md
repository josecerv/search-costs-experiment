---
title: "Search Costs Field Experiment"
date: "2025-06-06"
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
URM & 7.49 & 11.14 & 1.01 & 1.28 & 54.4 \\
Black & 2.25 & 5.98 & 0.32 & 0.69 & 23.4 \\
Hispanic & 5.21 & 9.54 & 0.69 & 1.01 & 43.1 \\
Female & 16.95 & 16.24 & 2.40 & 2.48 & 75.9 \\
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
Total faculty per department & 34.0 & 18.0 \\
\% URM faculty & 4.11 & 4.40 \\
\% Women faculty & 20.39 & 7.59 \\
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
Chemistry & 271 & 8.95 & 10.52 & 1.28 & 64.6 \\
Computer Science & 142 & 4.44 & 8.01 & 0.56 & 36.6 \\
Mathematics & 811 & 7.10 & 10.75 & 0.94 & 50.3 \\
Mechanical Engineering & 82 & 8.07 & 9.06 & 1.10 & 62.2 \\
Physics & 350 & 8.35 & 13.53 & 1.13 & 61.4 \\
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
Chemistry & 4.23 & 39.5 & 4.61 & 46.1 & 23.48 & 86.3 \\
Computer Science & 1.54 & 17.6 & 2.91 & 24.6 & 19.14 & 78.2 \\
Mathematics & 1.78 & 19.2 & 5.31 & 41.1 & 13.98 & 70.4 \\
Mechanical Engineering & 3.00 & 29.3 & 5.08 & 46.3 & 19.56 & 75.6 \\
Physics & 1.91 & 21.4 & 6.44 & 52.0 & 17.27 & 79.7 \\
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
Chemistry & 123 & 28.5 & 11.9 & 4.81 & 4.48 & 24.42 & 7.15 \\
Computer Science & 82 & 43.5 & 25.0 & 2.79 & 3.27 & 20.12 & 7.28 \\
Mathematics & 134 & 33.9 & 16.2 & 3.63 & 3.54 & 19.82 & 7.67 \\
Mechanical Engineering & 66 & 36.1 & 19.1 & 5.56 & 5.44 & 19.56 & 7.63 \\
Physics & 125 & 32.0 & 16.4 & 4.03 & 4.90 & 17.64 & 6.52 \\
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
Fall (1448) & 7.08 & 0.53 & 36.3 & 1.73 & 11.7 & 5.33 & 28.9 \\
Spring (1397) & 7.58 & 0.64 & 42.1 & 2.71 & 18.5 & 4.84 & 30.0 \\
\midrule
 & \multicolumn{3}{c}{Female} & \multicolumn{2}{c}{Total Speakers} & & \\
Semester & Mean \% & Mean Count & Pct. Any & Mean & SD & & \\
\midrule
Fall & 16.17 & 1.27 & 62.0 & 7.75 & 5.50 & & \\
Spring & 17.74 & 1.52 & 64.2 & 8.56 & 6.92 & & \\
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
Treatment  &  0.691$^{}$ & 0.649$^{}$ & 0.087$^{}$ & 0.059$^{}$ & 0.015$^{}$ & 0.009$^{}$  \\
 &  (0.525) & (0.519) & (0.067) & (0.065) & (0.025) & (0.023)  \\
Constant  &  8.561$^{***}$ & 4.641$^{*}$ & 1.178$^{***}$ & 0.302$^{}$ & 0.596$^{***}$ & 0.257$^{*}$  \\
 &  (1.632) & (2.132) & (0.172) & (0.285) & (0.072) & (0.115)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,656 & 1,656 & 1,656 & 1,656 & 1,656 & 1,656  \\
Adjusted $R^2$ &  0.010 & 0.014 & 0.028 & 0.035 & 0.027 & 0.040  \\
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
Treatment  &  -0.461$^{}$ & -0.427$^{}$ & 0.087$^{}$ & 0.059$^{}$ & -0.548$^{}$ & -0.485$^{}$  \\
 &  (0.554) & (0.546) & (0.067) & (0.065) & (0.528) & (0.521)  \\
Constant  &  16.810$^{***}$ & 13.460$^{***}$ & 1.178$^{***}$ & 0.302$^{}$ & 15.631$^{***}$ & 13.159$^{***}$  \\
 &  (1.313) & (2.452) & (0.172) & (0.285) & (1.247) & (2.317)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,656 & 1,656 & 1,656 & 1,656 & 1,656 & 1,656  \\
Adjusted $R^2$ &  0.031 & 0.058 & 0.028 & 0.035 & 0.030 & 0.058  \\
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
URM Speakers & 0.0871 & (0.0631) \\
Non-URM Speakers & -0.5482 & (0.4619) \\
\midrule
Sum of Effects & -0.4611 & --- \\
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
Treatment  &  0.632$^{*}$ & 0.611$^{*}$ & 0.077$^{+}$ & 0.075$^{*}$ & 0.048$^{*}$ & 0.047$^{*}$  \\
 &  (0.310) & (0.294) & (0.039) & (0.038) & (0.023) & (0.022)  \\
Constant  &  2.841$^{***}$ & 1.121$^{}$ & 0.435$^{***}$ & 0.119$^{}$ & 0.294$^{***}$ & 0.070$^{}$  \\
 &  (0.799) & (1.306) & (0.103) & (0.167) & (0.061) & (0.104)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,656 & 1,656 & 1,656 & 1,656 & 1,656 & 1,656  \\
Adjusted $R^2$ &  0.025 & 0.029 & 0.046 & 0.054 & 0.034 & 0.042  \\
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
Treatment  &  0.074$^{}$ & 0.045$^{}$ & 0.010$^{}$ & -0.018$^{}$ & -0.019$^{}$ & -0.030$^{}$  \\
 &  (0.458) & (0.472) & (0.049) & (0.049) & (0.025) & (0.025)  \\
Constant  &  5.508$^{***}$ & 3.304$^{+}$ & 0.718$^{***}$ & 0.147$^{}$ & 0.450$^{***}$ & 0.186$^{+}$  \\
 &  (1.528) & (1.936) & (0.149) & (0.230) & (0.076) & (0.110)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,656 & 1,656 & 1,656 & 1,656 & 1,656 & 1,656  \\
Adjusted $R^2$ &  0.006 & 0.006 & 0.014 & 0.020 & 0.019 & 0.025  \\
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
Treatment  &  0.192$^{}$ & -0.310$^{}$ & -0.059$^{}$ & -0.124$^{}$ & -0.003$^{}$ & -0.008$^{}$  \\
 &  (0.837) & (0.829) & (0.129) & (0.128) & (0.022) & (0.021)  \\
Constant  &  21.803$^{***}$ & 13.564$^{***}$ & 3.630$^{***}$ & 2.267$^{***}$ & 0.869$^{***}$ & 0.678$^{***}$  \\
 &  (2.082) & (3.961) & (0.353) & (0.597) & (0.063) & (0.099)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,656 & 1,656 & 1,656 & 1,656 & 1,656 & 1,656  \\
Adjusted $R^2$ &  0.049 & 0.057 & 0.086 & 0.102 & 0.017 & 0.029  \\
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
Treatment  &  -0.004$^{}$ & -0.064$^{}$ & 0.019$^{}$ & 0.011$^{}$ & 0.011$^{}$ & 0.004$^{}$  \\
 &  (0.172) & (0.183) & (0.019) & (0.019) & (0.016) & (0.017)  \\
Constant  &  1.900$^{**}$ & 0.036$^{}$ & 0.217$^{***}$ & 0.003$^{}$ & 0.186$^{***}$ & -0.008$^{}$  \\
 &  (0.605) & (0.593) & (0.060) & (0.091) & (0.049) & (0.078)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,656 & 1,656 & 1,656 & 1,656 & 1,656 & 1,656  \\
Adjusted $R^2$ &  0.015 & 0.019 & 0.038 & 0.048 & 0.040 & 0.048  \\
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
Treatment  &  0.118$^{+}$ & 0.127$^{+}$ & 0.011$^{}$ & 0.011$^{}$ & 0.013$^{}$ & 0.013$^{+}$  \\
 &  (0.071) & (0.073) & (0.009) & (0.009) & (0.008) & (0.008)  \\
Constant  &  0.561$^{***}$ & 0.139$^{}$ & 0.061$^{**}$ & 0.005$^{}$ & 0.049$^{*}$ & 0.005$^{}$  \\
 &  (0.165) & (0.276) & (0.023) & (0.042) & (0.020) & (0.036)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,656 & 1,656 & 1,656 & 1,656 & 1,656 & 1,656  \\
Adjusted $R^2$ &  0.028 & 0.030 & 0.025 & 0.030 & 0.021 & 0.026  \\
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
Treatment  &  0.514$^{+}$ & 0.484$^{+}$ & 0.067$^{+}$ & 0.064$^{*}$ & 0.052$^{*}$ & 0.051$^{*}$  \\
 &  (0.264) & (0.248) & (0.034) & (0.033) & (0.022) & (0.022)  \\
Constant  &  2.281$^{**}$ & 0.982$^{}$ & 0.367$^{***}$ & 0.110$^{}$ & 0.281$^{***}$ & 0.051$^{}$  \\
 &  (0.711) & (1.168) & (0.092) & (0.143) & (0.060) & (0.102)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,656 & 1,656 & 1,656 & 1,656 & 1,656 & 1,656  \\
Adjusted $R^2$ &  0.017 & 0.021 & 0.038 & 0.044 & 0.033 & 0.041  \\
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
Treatment  &  -0.126$^{}$ & -0.197$^{}$ & 0.010$^{}$ & 0.001$^{}$ & 0.005$^{}$ & -0.002$^{}$  \\
 &  (0.161) & (0.174) & (0.013) & (0.013) & (0.012) & (0.012)  \\
Constant  &  1.315$^{*}$ & -0.146$^{}$ & 0.065$^{}$ & -0.064$^{}$ & 0.057$^{+}$ & -0.066$^{}$  \\
 &  (0.587) & (0.492) & (0.044) & (0.066) & (0.034) & (0.057)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,656 & 1,656 & 1,656 & 1,656 & 1,656 & 1,656  \\
Adjusted $R^2$ &  0.002 & 0.004 & 0.008 & 0.016 & 0.007 & 0.015  \\
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
Treatment  &  0.199$^{}$ & 0.242$^{}$ & 0.000$^{}$ & -0.019$^{}$ & -0.020$^{}$ & -0.030$^{}$  \\
 &  (0.391) & (0.402) & (0.044) & (0.044) & (0.025) & (0.025)  \\
Constant  &  4.194$^{**}$ & 3.450$^{*}$ & 0.647$^{***}$ & 0.209$^{}$ & 0.446$^{***}$ & 0.200$^{+}$  \\
 &  (1.352) & (1.719) & (0.130) & (0.199) & (0.076) & (0.109)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,656 & 1,656 & 1,656 & 1,656 & 1,656 & 1,656  \\
Adjusted $R^2$ &  0.009 & 0.008 & 0.013 & 0.019 & 0.020 & 0.025  \\
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
Treatment  &  0.287$^{}$ & -0.531$^{}$ & -0.141$^{}$ & -0.206$^{}$ & 0.028$^{}$ & 0.009$^{}$  \\
 &  (1.181) & (1.167) & (0.166) & (0.165) & (0.052) & (0.055)  \\
Constant  &  6.404$^{*}$ & -2.294$^{}$ & 0.914$^{*}$ & -0.769$^{}$ & 0.179$^{}$ & -0.364$^{}$  \\
 &  (2.648) & (5.808) & (0.412) & (0.778) & (0.120) & (0.259)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  271 & 271 & 271 & 271 & 271 & 271  \\
Adjusted $R^2$ &  -0.028 & -0.023 & 0.092 & 0.097 & 0.095 & 0.102  \\
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
Treatment  &  0.599$^{}$ & 0.268$^{}$ & -0.004$^{}$ & -0.000$^{}$ & 0.068$^{}$ & 0.041$^{}$  \\
 &  (1.051) & (0.846) & (0.121) & (0.101) & (0.065) & (0.060)  \\
Constant  &  2.511$^{}$ & -8.666$^{*}$ & 0.336$^{}$ & -1.537$^{**}$ & 0.137$^{}$ & -0.900$^{**}$  \\
 &  (2.539) & (3.863) & (0.243) & (0.534) & (0.154) & (0.297)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  271 & 271 & 271 & 271 & 271 & 271  \\
Adjusted $R^2$ &  -0.033 & -0.014 & 0.039 & 0.076 & 0.034 & 0.082  \\
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
Treatment  &  -0.244$^{}$ & -0.754$^{}$ & -0.149$^{}$ & -0.225$^{+}$ & -0.104$^{+}$ & -0.141$^{*}$  \\
 &  (0.968) & (0.979) & (0.114) & (0.123) & (0.061) & (0.061)  \\
Constant  &  3.058$^{+}$ & 4.161$^{}$ & 0.545$^{}$ & 0.508$^{}$ & 0.211$^{}$ & 0.153$^{}$  \\
 &  (1.807) & (4.909) & (0.360) & (0.543) & (0.156) & (0.297)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  271 & 271 & 271 & 271 & 271 & 271  \\
Adjusted $R^2$ &  -0.026 & -0.024 & 0.043 & 0.068 & 0.032 & 0.052  \\
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
Treatment  &  0.952$^{}$ & 1.220$^{}$ & 0.157$^{+}$ & 0.153$^{}$ & 0.020$^{}$ & 0.010$^{}$  \\
 &  (0.723) & (0.801) & (0.095) & (0.104) & (0.034) & (0.032)  \\
Constant  &  6.297$^{***}$ & 6.722$^{}$ & 0.880$^{***}$ & 0.307$^{}$ & 0.507$^{***}$ & 0.236$^{}$  \\
 &  (1.437) & (4.219) & (0.147) & (0.558) & (0.068) & (0.189)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  811 & 811 & 811 & 811 & 811 & 811  \\
Adjusted $R^2$ &  0.001 & -0.002 & -0.000 & -0.003 & -0.011 & -0.001  \\
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
Treatment  &  0.213$^{}$ & 0.504$^{}$ & 0.074$^{}$ & 0.109$^{*}$ & 0.016$^{}$ & 0.024$^{}$  \\
 &  (0.393) & (0.428) & (0.049) & (0.054) & (0.029) & (0.026)  \\
Constant  &  0.913$^{+}$ & 1.800$^{}$ & 0.198$^{**}$ & 0.347$^{}$ & 0.173$^{***}$ & 0.066$^{}$  \\
 &  (0.534) & (2.399) & (0.072) & (0.262) & (0.051) & (0.150)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  811 & 811 & 811 & 811 & 811 & 811  \\
Adjusted $R^2$ &  0.010 & 0.019 & 0.009 & 0.022 & 0.003 & 0.017  \\
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
Treatment  &  0.757$^{}$ & 0.720$^{}$ & 0.088$^{}$ & 0.044$^{}$ & 0.026$^{}$ & 0.008$^{}$  \\
 &  (0.640) & (0.686) & (0.074) & (0.072) & (0.034) & (0.036)  \\
Constant  &  5.309$^{***}$ & 4.770$^{}$ & 0.664$^{***}$ & -0.076$^{}$ & 0.402$^{***}$ & 0.203$^{}$  \\
 &  (1.408) & (3.409) & (0.136) & (0.439) & (0.080) & (0.198)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  811 & 811 & 811 & 811 & 811 & 811  \\
Adjusted $R^2$ &  -0.004 & -0.003 & -0.001 & 0.002 & -0.002 & -0.001  \\
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
Treatment  &  0.230$^{}$ & 0.305$^{}$ & 0.159$^{}$ & 0.133$^{}$ & -0.005$^{}$ & 0.001$^{}$  \\
 &  (1.230) & (1.179) & (0.133) & (0.132) & (0.060) & (0.053)  \\
Constant  &  14.006$^{***}$ & 8.049$^{}$ & 1.272$^{***}$ & 1.378$^{}$ & 0.430$^{***}$ & 0.831$^{}$  \\
 &  (2.417) & (13.134) & (0.167) & (1.510) & (0.073) & (0.559)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  350 & 350 & 350 & 350 & 350 & 350  \\
Adjusted $R^2$ &  -0.001 & -0.009 & 0.006 & 0.013 & 0.003 & 0.029  \\
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
Treatment  &  1.431$^{*}$ & 1.588$^{*}$ & 0.175$^{*}$ & 0.186$^{**}$ & 0.124$^{*}$ & 0.132$^{**}$  \\
 &  (0.610) & (0.618) & (0.068) & (0.069) & (0.048) & (0.050)  \\
Constant  &  0.296$^{}$ & -0.493$^{}$ & 0.053$^{}$ & 0.245$^{}$ & 0.022$^{}$ & 0.033$^{}$  \\
 &  (0.616) & (4.537) & (0.081) & (0.642) & (0.053) & (0.437)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  350 & 350 & 350 & 350 & 350 & 350  \\
Adjusted $R^2$ &  -0.001 & -0.003 & 0.022 & 0.012 & 0.015 & 0.020  \\
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
Treatment  &  -1.201$^{}$ & -1.284$^{}$ & -0.016$^{}$ & -0.053$^{}$ & -0.063$^{}$ & -0.062$^{}$  \\
 &  (1.209) & (1.196) & (0.116) & (0.119) & (0.065) & (0.060)  \\
Constant  &  13.710$^{***}$ & 8.542$^{}$ & 1.219$^{***}$ & 1.133$^{}$ & 0.437$^{***}$ & 0.766$^{}$  \\
 &  (2.404) & (12.043) & (0.153) & (1.276) & (0.081) & (0.581)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  350 & 350 & 350 & 350 & 350 & 350  \\
Adjusted $R^2$ &  -0.002 & -0.013 & -0.008 & 0.013 & -0.002 & 0.008  \\
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
Treatment  &  2.529$^{+}$ & 2.932$^{+}$ & 0.113$^{}$ & 0.079$^{}$ & 0.110$^{}$ & 0.109$^{}$  \\
 &  (1.323) & (1.732) & (0.154) & (0.211) & (0.091) & (0.094)  \\
Constant  &  7.667$^{***}$ & 12.539$^{}$ & 1.462$^{***}$ & 4.042$^{**}$ & 0.882$^{***}$ & 2.540$^{***}$  \\
 &  (1.824) & (12.270) & (0.310) & (1.464) & (0.186) & (0.674)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  142 & 142 & 142 & 142 & 142 & 142  \\
Adjusted $R^2$ &  0.057 & 0.104 & 0.092 & 0.080 & 0.081 & 0.100  \\
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
Treatment  &  0.382$^{}$ & -0.051$^{}$ & -0.043$^{}$ & -0.060$^{}$ & -0.018$^{}$ & -0.042$^{}$  \\
 &  (0.678) & (0.669) & (0.065) & (0.073) & (0.055) & (0.067)  \\
Constant  &  4.467$^{**}$ & 1.582$^{}$ & 0.745$^{***}$ & 2.020$^{*}$ & 0.603$^{***}$ & 1.437$^{*}$  \\
 &  (1.552) & (9.001) & (0.218) & (0.931) & (0.155) & (0.696)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  142 & 142 & 142 & 142 & 142 & 142  \\
Adjusted $R^2$ &  -0.022 & -0.058 & 0.052 & 0.033 & 0.051 & 0.026  \\
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
Treatment  &  2.147$^{}$ & 2.983$^{+}$ & 0.156$^{}$ & 0.139$^{}$ & 0.136$^{}$ & 0.156$^{+}$  \\
 &  (1.412) & (1.733) & (0.137) & (0.181) & (0.096) & (0.089)  \\
Constant  &  3.200$^{}$ & 10.957$^{}$ & 0.716$^{*}$ & 2.022$^{+}$ & 0.589$^{**}$ & 2.245$^{**}$  \\
 &  (2.091) & (10.855) & (0.289) & (1.098) & (0.224) & (0.704)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  142 & 142 & 142 & 142 & 142 & 142  \\
Adjusted $R^2$ &  0.047 & 0.113 & 0.042 & 0.028 & 0.066 & 0.088  \\
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
Treatment  &  3.433$^{+}$ & 3.004$^{}$ & 0.612$^{*}$ & 0.762$^{*}$ & 0.057$^{}$ & 0.080$^{}$  \\
 &  (1.998) & (1.939) & (0.292) & (0.350) & (0.113) & (0.126)  \\
Constant  &  14.686$^{*}$ & 3.479$^{}$ & 2.184$^{*}$ & 2.258$^{}$ & 0.703$^{*}$ & 0.419$^{}$  \\
 &  (5.796) & (10.441) & (0.918) & (2.200) & (0.269) & (0.567)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  82 & 82 & 82 & 82 & 82 & 82  \\
Adjusted $R^2$ &  0.020 & 0.010 & 0.011 & 0.132 & 0.020 & 0.021  \\
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
Treatment  &  3.515$^{***}$ & 2.751$^{**}$ & 0.586$^{**}$ & 0.523$^{*}$ & 0.292$^{**}$ & 0.283$^{**}$  \\
 &  (0.993) & (0.894) & (0.185) & (0.205) & (0.091) & (0.094)  \\
Constant  &  7.647$^{**}$ & 7.606$^{}$ & 0.858$^{***}$ & 0.622$^{}$ & 0.738$^{***}$ & 0.770$^{+}$  \\
 &  (2.371) & (4.930) & (0.191) & (1.707) & (0.176) & (0.460)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  82 & 82 & 82 & 82 & 82 & 82  \\
Adjusted $R^2$ &  0.131 & 0.138 & 0.111 & 0.163 & 0.135 & 0.174  \\
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
Treatment  &  -0.082$^{}$ & 0.253$^{}$ & 0.026$^{}$ & 0.239$^{}$ & -0.050$^{}$ & 0.004$^{}$  \\
 &  (1.869) & (1.894) & (0.216) & (0.227) & (0.122) & (0.132)  \\
Constant  &  7.039$^{}$ & -4.127$^{}$ & 1.326$^{}$ & 1.636$^{}$ & 0.495$^{+}$ & 0.086$^{}$  \\
 &  (4.326) & (10.326) & (0.839) & (1.453) & (0.274) & (0.613)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  82 & 82 & 82 & 82 & 82 & 82  \\
Adjusted $R^2$ &  -0.068 & -0.084 & -0.011 & 0.064 & -0.018 & -0.005  \\
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
Treatment  &  0.949$^{}$ & 0.859$^{}$ & 0.078$^{+}$ & 0.049$^{}$ & 0.033$^{}$ & 0.020$^{}$  \\
 &  (0.695) & (0.687) & (0.046) & (0.044) & (0.025) & (0.025)  \\
Constant  &  6.357$^{**}$ & -2.483$^{}$ & 0.538$^{***}$ & -0.283$^{}$ & 0.366$^{***}$ & -0.058$^{}$  \\
 &  (2.449) & (3.059) & (0.145) & (0.212) & (0.070) & (0.111)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,448 & 1,448 & 1,448 & 1,448 & 1,448 & 1,448  \\
Adjusted $R^2$ &  0.018 & 0.026 & 0.024 & 0.040 & 0.023 & 0.035  \\
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
Treatment  &  0.494$^{}$ & 0.456$^{}$ & 0.053$^{*}$ & 0.050$^{*}$ & 0.043$^{**}$ & 0.042$^{*}$  \\
 &  (0.333) & (0.334) & (0.021) & (0.021) & (0.017) & (0.017)  \\
Constant  &  2.863$^{**}$ & -1.651$^{}$ & 0.224$^{***}$ & -0.075$^{}$ & 0.172$^{***}$ & -0.067$^{}$  \\
 &  (0.987) & (1.434) & (0.061) & (0.097) & (0.046) & (0.080)  \\
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
Treatment  &  0.437$^{}$ & 0.371$^{}$ & 0.024$^{}$ & -0.003$^{}$ & 0.009$^{}$ & -0.006$^{}$  \\
 &  (0.635) & (0.657) & (0.038) & (0.038) & (0.024) & (0.025)  \\
Constant  &  3.351$^{}$ & -1.075$^{}$ & 0.301$^{*}$ & -0.231$^{}$ & 0.236$^{**}$ & -0.066$^{}$  \\
 &  (2.358) & (2.931) & (0.134) & (0.188) & (0.073) & (0.109)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,448 & 1,448 & 1,448 & 1,448 & 1,448 & 1,448  \\
Adjusted $R^2$ &  0.011 & 0.010 & 0.020 & 0.030 & 0.022 & 0.028  \\
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
Treatment  &  0.573$^{}$ & 0.569$^{}$ & 0.006$^{}$ & 0.006$^{}$ & -0.010$^{}$ & -0.012$^{}$  \\
 &  (0.735) & (0.745) & (0.055) & (0.056) & (0.028) & (0.028)  \\
Constant  &  8.888$^{***}$ & 9.945$^{**}$ & 0.988$^{***}$ & 0.919$^{***}$ & 0.546$^{***}$ & 0.438$^{***}$  \\
 &  (1.847) & (3.098) & (0.144) & (0.248) & (0.072) & (0.120)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,397 & 1,397 & 1,397 & 1,397 & 1,397 & 1,397  \\
Adjusted $R^2$ &  0.001 & 0.000 & 0.020 & 0.017 & 0.022 & 0.023  \\
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
Treatment  &  0.716$^{}$ & 0.701$^{}$ & 0.028$^{}$ & 0.030$^{}$ & 0.019$^{}$ & 0.021$^{}$  \\
 &  (0.469) & (0.444) & (0.035) & (0.034) & (0.023) & (0.023)  \\
Constant  &  2.050$^{*}$ & 1.753$^{}$ & 0.321$^{***}$ & 0.306$^{*}$ & 0.237$^{***}$ & 0.184$^{+}$  \\
 &  (1.030) & (1.736) & (0.086) & (0.148) & (0.058) & (0.102)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,397 & 1,397 & 1,397 & 1,397 & 1,397 & 1,397  \\
Adjusted $R^2$ &  0.008 & 0.007 & 0.030 & 0.031 & 0.020 & 0.019  \\
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
Treatment  &  -0.122$^{}$ & -0.117$^{}$ & -0.021$^{}$ & -0.024$^{}$ & -0.030$^{}$ & -0.033$^{}$  \\
 &  (0.611) & (0.636) & (0.040) & (0.040) & (0.026) & (0.026)  \\
Constant  &  6.620$^{***}$ & 7.974$^{**}$ & 0.650$^{***}$ & 0.592$^{**}$ & 0.425$^{***}$ & 0.346$^{**}$  \\
 &  (1.684) & (2.846) & (0.115) & (0.190) & (0.073) & (0.107)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,397 & 1,397 & 1,397 & 1,397 & 1,397 & 1,397  \\
Adjusted $R^2$ &  -0.006 & -0.006 & 0.006 & 0.008 & 0.012 & 0.015  \\
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
Treatment  &  0.644$^{}$ & 0.639$^{}$ & 0.088$^{}$ & 0.051$^{}$ & 0.018$^{}$ & 0.007$^{}$  \\
 &  (0.516) & (0.515) & (0.066) & (0.064) & (0.025) & (0.023)  \\
Constant  &  9.759$^{***}$ & 6.148$^{**}$ & 1.128$^{***}$ & 0.341$^{}$ & 0.531$^{***}$ & 0.232$^{*}$  \\
 &  (1.635) & (1.990) & (0.178) & (0.257) & (0.078) & (0.109)  \\
Dept Ranking (centered)  &  0.016$^{}$ & 0.028$^{*}$ & -0.003$^{*}$ & -0.001$^{}$ & -0.002$^{**}$ & -0.001$^{}$  \\
 &  (0.013) & (0.013) & (0.001) & (0.001) & (0.001) & (0.001)  \\
Treatment $\times$ Dept Ranking (centered)  &  0.007$^{}$ & 0.007$^{}$ & 0.005$^{*}$ & 0.005$^{**}$ & 0.001$^{}$ & 0.001$^{}$  \\
 &  (0.016) & (0.016) & (0.002) & (0.002) & (0.001) & (0.001)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,656 & 1,656 & 1,656 & 1,656 & 1,656 & 1,656  \\
Adjusted $R^2$ &  0.012 & 0.014 & 0.031 & 0.039 & 0.031 & 0.041  \\
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
Treatment  &  0.867$^{}$ & 0.671$^{}$ & 0.063$^{}$ & 0.055$^{}$ & 0.007$^{}$ & 0.010$^{}$  \\
 &  (0.535) & (0.515) & (0.069) & (0.065) & (0.025) & (0.023)  \\
Constant  &  8.467$^{***}$ & 3.811$^{+}$ & 1.161$^{***}$ & 0.353$^{}$ & 0.575$^{***}$ & 0.246$^{*}$  \\
 &  (1.590) & (2.139) & (0.180) & (0.296) & (0.070) & (0.113)  \\
Total Faculty (centered)  &  -0.037$^{}$ & -0.029$^{}$ & 0.004$^{}$ & 0.003$^{}$ & 0.001$^{}$ & -0.001$^{}$  \\
 &  (0.026) & (0.026) & (0.003) & (0.003) & (0.001) & (0.001)  \\
Treatment $\times$ Total Faculty (centered)  &  0.027$^{}$ & 0.016$^{}$ & -0.001$^{}$ & -0.003$^{}$ & 0.001$^{}$ & 0.001$^{}$  \\
 &  (0.029) & (0.029) & (0.003) & (0.003) & (0.001) & (0.001)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,656 & 1,656 & 1,656 & 1,656 & 1,656 & 1,656  \\
Adjusted $R^2$ &  0.011 & 0.014 & 0.028 & 0.035 & 0.028 & 0.039  \\
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
Treatment  &  0.694$^{}$ & 0.624$^{}$ & 0.091$^{}$ & 0.056$^{}$ & 0.017$^{}$ & 0.008$^{}$  \\
 &  (0.521) & (0.520) & (0.065) & (0.064) & (0.024) & (0.023)  \\
Constant  &  8.435$^{***}$ & 7.800$^{***}$ & 1.135$^{***}$ & 0.824$^{***}$ & 0.577$^{***}$ & 0.434$^{***}$  \\
 &  (1.569) & (1.795) & (0.168) & (0.235) & (0.069) & (0.099)  \\
Peer URM Faculty (centered)  &  0.059$^{}$ & 0.127$^{*}$ & 0.016$^{**}$ & 0.019$^{**}$ & 0.007$^{**}$ & 0.006$^{*}$  \\
 &  (0.054) & (0.055) & (0.005) & (0.006) & (0.002) & (0.002)  \\
Treatment $\times$ Peer URM Faculty (centered)  &  -0.064$^{}$ & -0.054$^{}$ & -0.004$^{}$ & -0.005$^{}$ & -0.001$^{}$ & -0.001$^{}$  \\
 &  (0.073) & (0.072) & (0.008) & (0.008) & (0.003) & (0.003)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,656 & 1,656 & 1,656 & 1,656 & 1,656 & 1,656  \\
Adjusted $R^2$ &  0.010 & 0.014 & 0.033 & 0.035 & 0.035 & 0.039  \\
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
Chemistry & Any Hispanic & Treatment & Extended & -0.1409 & 0.0611 & -2.307 & 0.0219 & * \\
Chemistry & Count Hispanic & Treatment & Extended & -0.2251 & 0.1229 & -1.831 & 0.0682 & + \\
Computer Science & \% Hispanic & Treatment & Extended & 2.9825 & 1.7330 & 1.721 & 0.0879 & + \\
Computer Science & \% URM & Treatment & Simple & 2.5293 & 1.3234 & 1.911 & 0.0583 & + \\
Computer Science & Any Hispanic & Treatment & Extended & 0.1556 & 0.0892 & 1.745 & 0.0836 & + \\
Mathematics & Count Black & Treatment & Extended & 0.1093 & 0.0540 & 2.024 & 0.0433 & * \\
Mathematics & Count URM & Treatment & Simple & 0.1570 & 0.0947 & 1.658 & 0.0978 & + \\
Mechanical Engineering & \% Black & Treatment & Simple & 3.5151 & 0.9928 & 3.540 & 0.0007 & *** \\
Mechanical Engineering & \% URM & Treatment & Simple & 3.4328 & 1.9981 & 1.718 & 0.0906 & + \\
Mechanical Engineering & Any Black & Treatment & Simple & 0.2919 & 0.0914 & 3.192 & 0.0022 & ** \\
Mechanical Engineering & Count Black & Treatment & Simple & 0.5865 & 0.1852 & 3.167 & 0.0023 & ** \\
Mechanical Engineering & Count URM & Treatment & Extended & 0.7615 & 0.3497 & 2.178 & 0.0336 & * \\
Physics & \% Black & Treatment & Extended & 1.5883 & 0.6182 & 2.569 & 0.0106 & * \\
Physics & Any Black & Treatment & Extended & 0.1322 & 0.0504 & 2.620 & 0.0092 & ** \\
Physics & Count Black & Treatment & Extended & 0.1862 & 0.0693 & 2.686 & 0.0076 & ** \\
\addlinespace[0.5em]
\multicolumn{9}{l}{\textbf{Identity Analysis}} \\
\midrule
Demographic Subgroup & \% Black & Treatment & Extended & 0.6107 & 0.2938 & 2.079 & 0.0378 & * \\
Demographic Subgroup & \% Black Female & Treatment & Extended & 0.1265 & 0.0733 & 1.726 & 0.0846 & + \\
Demographic Subgroup & \% Black Male & Treatment & Extended & 0.4842 & 0.2481 & 1.952 & 0.0511 & + \\
Demographic Subgroup & Any Black & Treatment & Simple & 0.0480 & 0.0226 & 2.126 & 0.0337 & * \\
Demographic Subgroup & Any Black Female & Treatment & Extended & 0.0134 & 0.0081 & 1.660 & 0.0970 & + \\
Demographic Subgroup & Any Black Male & Treatment & Simple & 0.0523 & 0.0223 & 2.340 & 0.0194 & * \\
Demographic Subgroup & Count Black & Treatment & Extended & 0.0746 & 0.0375 & 1.989 & 0.0469 & * \\
Demographic Subgroup & Count Black Male & Treatment & Extended & 0.0644 & 0.0325 & 1.980 & 0.0478 & * \\
\addlinespace[0.5em]
\multicolumn{9}{l}{\textbf{Moderation Analysis}} \\
\midrule
Department Rank & Count URM & Treatment $\times$ Dept Ranking & Extended & 0.0049 & 0.0019 & 2.650 & 0.0081 & ** \\
\addlinespace[0.5em]
\multicolumn{9}{l}{\textbf{Semester Analysis}} \\
\midrule
Fall Semester & Any Black & Treatment & Simple & 0.0434 & 0.0167 & 2.603 & 0.0093 & ** \\
Fall Semester & Count Black & Treatment & Simple & 0.0531 & 0.0209 & 2.541 & 0.0112 & * \\
Fall Semester & Count URM & Treatment & Simple & 0.0780 & 0.0456 & 1.711 & 0.0873 & + \\
\bottomrule
\end{tabular}
} % End group for scriptsize and tabcolsep
\parbox{\linewidth}{\footnotesize Note: Significance levels: + p<0.1; * p<0.05; ** p<0.01; *** p<0.001. SE = Clustered standard errors at department level. Constant terms are excluded from this summary.}
\end{table}

## Exploratory Analysis: Seniority Moderation

### Analysis 1: Does speaker seniority moderate the treatment effect?


\clearpage
\section{Exploratory Analysis: Seniority Moderation}

\subsection{Distribution of Years Since PhD}

\textbf{Seniority Data Coverage:}

- Total seminars with seniority data: 1627 (98.2\% of total)
- Number of departments: 523
- Mean of seminar-level mean years since PhD: 15.7 (SD = 7.5)
- Median of seminar-level mean years since PhD: 15.1
- Range of seminar means: 1.0 to 59.0 years
- IQR of seminar means: 10.5 to 19.9 years

\subsection{Continuous Moderation Analysis}

We test whether the average seniority of speakers in a seminar moderates the treatment effect on Black speaker representation.

Note: Seniority is measured as the mean years since PhD for speakers in each seminar.

\subsubsection{Outcome: Percentage Black Speakers}

\begin{table}[H]
\caption{Seniority Moderation Analysis: Percentage Black Speakers}
\centering
\begin{tabular}{lccc}
\toprule
 & (1) & (2) & (3) \\
 & Main Effects & Interaction & With Controls \\
\midrule
Treatment & 0.7693* & 0.7858* & 0.8519** \\
 & (0.3360) & (0.3442) & (0.3273) \\
Years Since PhD (centered) & -0.0156 & -0.0033 & -0.0034 \\
 & (0.0187) & (0.0232) & (0.0231) \\
Treatment × Years Since PhD &   & -0.0267 & -0.0321 \\
 &   & (0.0381) & (0.0382) \\
\midrule
Observations & 1627 & 1627 & 1627 \\
R-squared & 0.004 & 0.005 & 0.016 \\
Controls & No & No & Yes \\
\bottomrule
\end{tabular}
\parbox{\linewidth}{\footnotesize Note: Clustered standard errors at department level in parentheses. Years since PhD is the mean years since PhD for speakers in each seminar, centered at the median. Controls include department ranking, total faculty, and fraction URM faculty. Significance: + p<0.1; * p<0.05; ** p<0.01; *** p<0.001.}
\end{table}

\subsubsection{Outcome: Any Black Speakers}

\begin{table}[H]
\caption{Seniority Moderation Analysis: Any Black Speakers}
\centering
\begin{tabular}{lccc}
\toprule
 & (1) & (2) & (3) \\
 & Main Effects & Interaction & With Controls \\
\midrule
Treatment & 0.0573* & 0.0551* & 0.0632** \\
 & (0.0238) & (0.0239) & (0.0235) \\
Years Since PhD (centered) & 0.0003 & -0.0013 & -0.0013 \\
 & (0.0013) & (0.0016) & (0.0016) \\
Treatment × Years Since PhD &   & 0.0035 & 0.0032 \\
 &   & (0.0027) & (0.0027) \\
\midrule
Observations & 1627 & 1627 & 1627 \\
R-squared & 0.005 & 0.006 & 0.013 \\
Controls & No & No & Yes \\
\bottomrule
\end{tabular}
\parbox{\linewidth}{\footnotesize Note: Clustered standard errors at department level in parentheses. Years since PhD is the mean years since PhD for speakers in each seminar, centered at the median. Controls include department ranking, total faculty, and fraction URM faculty. Significance: + p<0.1; * p<0.05; ** p<0.01; *** p<0.001.}
\end{table}

\subsection{Subgroup Analysis: Seminars with Senior vs Junior Speakers}

\textbf{Median Split Groups:}

- Seminars with junior speakers (n=815): Mean = 10.0 years, Range = 1.0-15.1 years
- Seminars with senior speakers (n=812): Mean = 21.5 years, Range = 15.1-59.0 years

\subsubsection{Outcome: Percentage Black Speakers}

\begin{table}[H]
\caption{Subgroup Analysis by Seniority: Percentage Black Speakers}
\centering
\begin{tabular}{lcccc}
\toprule
 & \multicolumn{2}{c}{Seminars with Junior Speakers} & \multicolumn{2}{c}{Seminars with Senior Speakers} \\
 & (1) & (2) & (3) & (4) \\
 & Simple & With Controls & Simple & With Controls \\
\midrule
Treatment & 1.0131* & 1.1295* & 0.4977 & 0.5375 \\
 & (0.4793) & (0.4811) & (0.4165) & (0.4002) \\
\midrule
Observations & 815 & 815 & 812 & 812 \\
R-squared & 0.006 & 0.022 & 0.002 & 0.010 \\
Controls & No & Yes & No & Yes \\
\bottomrule
\end{tabular}
\parbox{\linewidth}{\footnotesize Note: Clustered standard errors at department level in parentheses. Junior/Senior split at median of seminar-level mean years since PhD. Controls include department ranking, total faculty, and fraction URM faculty. Significance: + p<0.1; * p<0.05; ** p<0.01; *** p<0.001.}
\end{table}

\textbf{Test for Difference Between Groups:}

Difference in treatment effect (Senior - Junior): -0.5154 (SE = 0.5984), p = 0.3892

\subsubsection{Outcome: Any Black Speakers}

\begin{table}[H]
\caption{Subgroup Analysis by Seniority: Any Black Speakers}
\centering
\begin{tabular}{lcccc}
\toprule
 & \multicolumn{2}{c}{Seminars with Junior Speakers} & \multicolumn{2}{c}{Seminars with Senior Speakers} \\
 & (1) & (2) & (3) & (4) \\
 & Simple & With Controls & Simple & With Controls \\
\midrule
Treatment & 0.0273 & 0.0384 & 0.0849* & 0.0868* \\
 & (0.0300) & (0.0303) & (0.0342) & (0.0341) \\
\midrule
Observations & 815 & 815 & 812 & 812 \\
R-squared & 0.001 & 0.006 & 0.009 & 0.019 \\
Controls & No & Yes & No & Yes \\
\bottomrule
\end{tabular}
\parbox{\linewidth}{\footnotesize Note: Clustered standard errors at department level in parentheses. Junior/Senior split at median of seminar-level mean years since PhD. Controls include department ranking, total faculty, and fraction URM faculty. Significance: + p<0.1; * p<0.05; ** p<0.01; *** p<0.001.}
\end{table}

\textbf{Test for Difference Between Groups:}

Difference in treatment effect (Senior - Junior): 0.0577 (SE = 0.0437), p = 0.1871

## Exploratory Analysis: Discipline Moderation

### Analysis 2: Does academic discipline moderate the treatment effect?


\clearpage
\section{Exploratory Analysis: Discipline Moderation}

\subsection{Distribution Across Disciplines}

\begin{table}[H]
\caption{Sample Distribution by Discipline}
\centering
\begin{tabular}{lrrrrr}
\toprule
Discipline & Seminars & Departments & Treatment & Control & \% of Total \\
\midrule
Mathematics & 811 & 134 & 381 & 430 & 49.0\% \\
Physics & 350 & 125 & 181 & 169 & 21.1\% \\
Chemistry & 271 & 123 & 144 & 127 & 16.4\% \\
Computer Science & 142 & 82 & 66 & 76 & 8.6\% \\
Mechanical Engineering & 82 & 66 & 39 & 43 & 5.0\% \\
\midrule
Total & 1656 & 530 & 811 & 845 & 100.0\% \\
\bottomrule
\end{tabular}
\end{table}

\subsection{Full Interaction Model}

We estimate the following model where treatment effects vary by discipline:

$$Y_{it} = \beta_0 + \sum_{d} \beta_{1d} \cdot \text{Treatment}_i \times \text{Discipline}_d + \sum_{d} \beta_{2d} \cdot \text{Discipline}_d + \epsilon_{it}$$

\subsubsection{Outcome: Percentage Black Speakers}

\begin{table}[H]
\caption{Treatment Effects by Discipline: Percentage Black Speakers}
\centering
\begin{tabular}{lccc}
\toprule
 & (1) & (2) & (3) \\
 & Pooled Effect & By Discipline & With Controls \\
\midrule
\textbf{Treatment Effects} & & & \\
Pooled & 0.6816* & & \\
 & (0.3104) & & \\
 & & & \\
Physics & & 1.4040* & 1.4338* \\
 & & (0.6165) & (0.6437) \\
Mathematics & & 0.2479 & 0.3371 \\
 & & (0.4093) & (0.4050) \\
Chemistry & & 0.3708 & 0.1699 \\
 & & (1.0355) & (0.9852) \\
MAE & & 3.9953*** & 3.6238** \\
 & & (1.2023) & (1.2158) \\
Computer Science & & 0.0499 & 0.2937 \\
 & & (0.8294) & (0.8247) \\
\midrule
Observations & 1656 & 1656 & 1656 \\
R-squared & 0.027 & 0.032 & 0.038 \\
Controls & No & No & Yes \\
\bottomrule
\end{tabular}
\parbox{\linewidth}{\footnotesize Note: Clustered standard errors at department level in parentheses. Computer Science is the reference category. MAE = Mechanical Engineering. Controls include department ranking, total faculty, and fraction URM faculty. Significance: + p<0.1; * p<0.05; ** p<0.01; *** p<0.001.}
\end{table}

\textbf{Wald Tests: Pairwise Comparisons of Treatment Effects}

\begin{table}[H]
\caption{Pairwise Comparisons of Discipline-Specific Treatment Effects}
\centering
\begin{tabular}{lcc}
\toprule
Comparison & Difference (SE) & p-value \\
\midrule
Physics - Mathematics & 1.0968 (0.7569) & 0.1474 \\
Physics - Chemistry & 1.2640 (1.1829) & 0.2853 \\
Physics - MAE & -2.1900 (1.3680) & 0.1094 \\
Physics - Computer Science & 1.1401 (1.0588) & 0.2816 \\
Mathematics - Chemistry & 0.1672 (1.0713) & 0.8760 \\
Mathematics - MAE & -3.2867 (1.2901) & 0.0108* \\
Mathematics - Computer Science & 0.0433 (0.9278) & 0.9628 \\
Chemistry - MAE & -3.4539 (1.5687) & 0.0277* \\
Chemistry - Computer Science & -0.1239 (1.3108) & 0.9247 \\
MAE - Computer Science & 3.3300 (1.4762) & 0.0241* \\
\bottomrule
\end{tabular}
\parbox{\linewidth}{\footnotesize Note: Based on Model 3 with controls. Positive values indicate the first discipline has a larger treatment effect. Significance: + p<0.1; * p<0.05; ** p<0.01; *** p<0.001.}
\end{table}

\subsubsection{Outcome: Any Black Speakers}

\begin{table}[H]
\caption{Treatment Effects by Discipline: Any Black Speakers}
\centering
\begin{tabular}{lccc}
\toprule
 & (1) & (2) & (3) \\
 & Pooled Effect & By Discipline & With Controls \\
\midrule
\textbf{Treatment Effects} & & & \\
Pooled & 0.0510* & & \\
 & (0.0224) & & \\
 & & & \\
Physics & & 0.0940+ & 0.0973* \\
 & & (0.0481) & (0.0487) \\
Mathematics & & 0.0233 & 0.0309 \\
 & & (0.0294) & (0.0299) \\
Chemistry & & 0.0466 & 0.0385 \\
 & & (0.0682) & (0.0672) \\
MAE & & 0.3220*** & 0.3104** \\
 & & (0.0962) & (0.0978) \\
Computer Science & & -0.0459 & -0.0314 \\
 & & (0.0710) & (0.0718) \\
\midrule
Observations & 1656 & 1656 & 1656 \\
R-squared & 0.035 & 0.042 & 0.044 \\
Controls & No & No & Yes \\
\bottomrule
\end{tabular}
\parbox{\linewidth}{\footnotesize Note: Clustered standard errors at department level in parentheses. Computer Science is the reference category. MAE = Mechanical Engineering. Controls include department ranking, total faculty, and fraction URM faculty. Significance: + p<0.1; * p<0.05; ** p<0.01; *** p<0.001.}
\end{table}

\textbf{Wald Tests: Pairwise Comparisons of Treatment Effects}

\begin{table}[H]
\caption{Pairwise Comparisons of Discipline-Specific Treatment Effects}
\centering
\begin{tabular}{lcc}
\toprule
Comparison & Difference (SE) & p-value \\
\midrule
Physics - Mathematics & 0.0664 (0.0570) & 0.2437 \\
Physics - Chemistry & 0.0587 (0.0827) & 0.4777 \\
Physics - MAE & -0.2131 (0.1086) & 0.0496* \\
Physics - Computer Science & 0.1286 (0.0874) & 0.1412 \\
Mathematics - Chemistry & -0.0077 (0.0737) & 0.9171 \\
Mathematics - MAE & -0.2795 (0.1018) & 0.0061** \\
Mathematics - Computer Science & 0.0622 (0.0776) & 0.4223 \\
Chemistry - MAE & -0.2718 (0.1184) & 0.0216* \\
Chemistry - Computer Science & 0.0699 (0.0991) & 0.4807 \\
MAE - Computer Science & 0.3418 (0.1213) & 0.0048** \\
\bottomrule
\end{tabular}
\parbox{\linewidth}{\footnotesize Note: Based on Model 3 with controls. Positive values indicate the first discipline has a larger treatment effect. Significance: + p<0.1; * p<0.05; ** p<0.01; *** p<0.001.}
\end{table}

\subsection{Summary of Exploratory Analyses}

\textbf{Key Findings:}

\begin{enumerate}
\item \textbf{Seniority Moderation:} We examined whether the treatment effect varies by speaker seniority (years since PhD). The continuous moderation analysis tests for a linear interaction between treatment and years since PhD, while the subgroup analysis compares effects for junior vs senior speakers (split at median).

\item \textbf{Discipline Moderation:} We tested whether treatment effects differ across the five academic disciplines in our sample. The full interaction model allows each discipline to have its own treatment effect, and pairwise Wald tests examine whether these differences are statistically significant.
\end{enumerate}

\textbf{Note:} These are exploratory analyses not pre-registered in our analysis plan. Results should be interpreted with appropriate caution regarding multiple testing.
