---
title: "Search Costs Field Experiment"
date: "2025-06-11"
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
Number of seminars & 1655 \\
Number of unique departments & 528 \\
Total speakers across all seminars & 23193 \\
Mean speakers per seminar & 14.01 \\
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
URM & 7.42 & 11.10 & 1.00 & 1.28 & 54.1 \\
Black & 2.23 & 5.95 & 0.32 & 0.68 & 23.3 \\
Hispanic & 5.17 & 9.51 & 0.68 & 1.01 & 42.7 \\
Female & 16.97 & 16.17 & 2.40 & 2.47 & 76.1 \\
\bottomrule
\end{tabular}
\parbox{\linewidth}{\footnotesize Note: N =  1655  seminars. Percentages calculated among speakers with demographic data available. 'Pct. Any' indicates the percentage of seminars that have at least one speaker from that demographic group.}
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
Total faculty per department & 34.0 & 18.1 \\
\% URM faculty & 4.09 & 4.40 \\
\% Women faculty & 20.40 & 7.58 \\
\bottomrule
\end{tabular}
\parbox{\linewidth}{\footnotesize Note: N =  528  unique departments. Department faculty demographics based on 2024 coding.}
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
Physics & 350 & 125 & 15.8 & 10.4 \\
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
Chemistry & 270 & 8.92 & 10.51 & 1.27 & 64.4 \\
Computer Science & 142 & 4.48 & 8.21 & 0.54 & 36.6 \\
Mathematics & 812 & 7.02 & 10.67 & 0.93 & 50.0 \\
Mechanical Engineering & 81 & 8.20 & 9.17 & 1.12 & 61.7 \\
Physics & 350 & 8.21 & 13.45 & 1.12 & 60.9 \\
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
Chemistry & 4.23 & 39.6 & 4.58 & 45.6 & 23.70 & 86.7 \\
Computer Science & 1.55 & 17.6 & 2.93 & 24.6 & 19.23 & 78.2 \\
Mathematics & 1.79 & 19.5 & 5.22 & 40.6 & 14.01 & 70.8 \\
Mechanical Engineering & 2.95 & 28.4 & 5.25 & 46.9 & 19.83 & 76.5 \\
Physics & 1.82 & 20.9 & 6.39 & 51.7 & 17.05 & 79.4 \\
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
Spring (1389) & 7.51 & 0.64 & 41.7 & 2.68 & 18.4 & 4.81 & 29.6 \\
\midrule
 & \multicolumn{3}{c}{Female} & \multicolumn{2}{c}{Total Speakers} & & \\
Semester & Mean \% & Mean Count & Pct. Any & Mean & SD & & \\
\midrule
Fall & 16.16 & 1.27 & 62.0 & 7.75 & 5.50 & & \\
Spring & 17.71 & 1.53 & 65.0 & 8.62 & 6.86 & & \\
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
Treatment  &  0.773$^{}$ & 0.721$^{}$ & 0.101$^{}$ & 0.076$^{}$ & 0.021$^{}$ & 0.013$^{}$  \\
 &  (0.523) & (0.515) & (0.066) & (0.064) & (0.025) & (0.023)  \\
Constant  &  7.902$^{***}$ & 3.183$^{}$ & 1.102$^{***}$ & 0.163$^{}$ & 0.573$^{***}$ & 0.197$^{+}$  \\
 &  (1.636) & (2.097) & (0.168) & (0.272) & (0.072) & (0.115)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,655 & 1,655 & 1,655 & 1,655 & 1,655 & 1,655  \\
Adjusted $R^2$ &  0.011 & 0.017 & 0.030 & 0.039 & 0.028 & 0.042  \\
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
Treatment  &  -0.508$^{}$ & -0.468$^{}$ & 0.101$^{}$ & 0.076$^{}$ & -0.609$^{}$ & -0.544$^{}$  \\
 &  (0.546) & (0.545) & (0.066) & (0.064) & (0.519) & (0.520)  \\
Constant  &  17.111$^{***}$ & 13.874$^{***}$ & 1.102$^{***}$ & 0.163$^{}$ & 16.009$^{***}$ & 13.712$^{***}$  \\
 &  (1.257) & (2.406) & (0.168) & (0.272) & (1.175) & (2.252)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,655 & 1,655 & 1,655 & 1,655 & 1,655 & 1,655  \\
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
URM Speakers & 0.1006 & (0.0630) \\
Non-URM Speakers & -0.6088 & (0.4599) \\
\midrule
Sum of Effects & -0.5081 & --- \\
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
Treatment  &  0.676$^{*}$ & 0.660$^{*}$ & 0.084$^{*}$ & 0.083$^{*}$ & 0.056$^{*}$ & 0.055$^{*}$  \\
 &  (0.308) & (0.294) & (0.039) & (0.038) & (0.023) & (0.023)  \\
Constant  &  2.714$^{***}$ & 0.929$^{}$ & 0.428$^{***}$ & 0.103$^{}$ & 0.287$^{***}$ & 0.051$^{}$  \\
 &  (0.791) & (1.301) & (0.103) & (0.167) & (0.061) & (0.104)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,655 & 1,655 & 1,655 & 1,655 & 1,655 & 1,655  \\
Adjusted $R^2$ &  0.026 & 0.031 & 0.048 & 0.056 & 0.036 & 0.044  \\
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
Treatment  &  0.111$^{}$ & 0.067$^{}$ & 0.017$^{}$ & -0.009$^{}$ & -0.017$^{}$ & -0.029$^{}$  \\
 &  (0.455) & (0.469) & (0.049) & (0.048) & (0.025) & (0.025)  \\
Constant  &  4.976$^{***}$ & 2.037$^{}$ & 0.648$^{***}$ & 0.023$^{}$ & 0.429$^{***}$ & 0.141$^{}$  \\
 &  (1.496) & (1.865) & (0.138) & (0.209) & (0.074) & (0.106)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,655 & 1,655 & 1,655 & 1,655 & 1,655 & 1,655  \\
Adjusted $R^2$ &  0.006 & 0.006 & 0.015 & 0.022 & 0.020 & 0.026  \\
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
Treatment  &  0.341$^{}$ & -0.126$^{}$ & -0.061$^{}$ & -0.122$^{}$ & 0.005$^{}$ & 0.001$^{}$  \\
 &  (0.836) & (0.830) & (0.128) & (0.128) & (0.022) & (0.022)  \\
Constant  &  22.012$^{***}$ & 13.852$^{***}$ & 3.650$^{***}$ & 2.285$^{***}$ & 0.872$^{***}$ & 0.691$^{***}$  \\
 &  (2.105) & (4.017) & (0.339) & (0.592) & (0.061) & (0.100)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,655 & 1,655 & 1,655 & 1,655 & 1,655 & 1,655  \\
Adjusted $R^2$ &  0.051 & 0.059 & 0.083 & 0.098 & 0.016 & 0.026  \\
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
Treatment  &  0.024$^{}$ & -0.040$^{}$ & 0.021$^{}$ & 0.014$^{}$ & 0.014$^{}$ & 0.008$^{}$  \\
 &  (0.172) & (0.183) & (0.019) & (0.019) & (0.017) & (0.017)  \\
Constant  &  1.802$^{**}$ & -0.051$^{}$ & 0.206$^{***}$ & -0.002$^{}$ & 0.175$^{***}$ & -0.014$^{}$  \\
 &  (0.604) & (0.582) & (0.060) & (0.091) & (0.049) & (0.078)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,655 & 1,655 & 1,655 & 1,655 & 1,655 & 1,655  \\
Adjusted $R^2$ &  0.014 & 0.019 & 0.040 & 0.049 & 0.040 & 0.048  \\
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
Treatment  &  0.145$^{*}$ & 0.155$^{*}$ & 0.012$^{}$ & 0.013$^{}$ & 0.014$^{+}$ & 0.015$^{+}$  \\
 &  (0.069) & (0.072) & (0.009) & (0.009) & (0.008) & (0.008)  \\
Constant  &  0.484$^{**}$ & 0.068$^{}$ & 0.056$^{*}$ & 0.003$^{}$ & 0.044$^{*}$ & 0.003$^{}$  \\
 &  (0.152) & (0.271) & (0.024) & (0.042) & (0.020) & (0.036)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,655 & 1,655 & 1,655 & 1,655 & 1,655 & 1,655  \\
Adjusted $R^2$ &  0.032 & 0.035 & 0.024 & 0.029 & 0.020 & 0.025  \\
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
Treatment  &  0.531$^{*}$ & 0.506$^{*}$ & 0.072$^{*}$ & 0.071$^{*}$ & 0.059$^{**}$ & 0.058$^{**}$  \\
 &  (0.264) & (0.248) & (0.034) & (0.033) & (0.022) & (0.022)  \\
Constant  &  2.229$^{**}$ & 0.860$^{}$ & 0.363$^{***}$ & 0.097$^{}$ & 0.278$^{***}$ & 0.035$^{}$  \\
 &  (0.709) & (1.165) & (0.092) & (0.142) & (0.060) & (0.102)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,655 & 1,655 & 1,655 & 1,655 & 1,655 & 1,655  \\
Adjusted $R^2$ &  0.018 & 0.022 & 0.040 & 0.047 & 0.035 & 0.043  \\
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
Treatment  &  -0.125$^{}$ & -0.202$^{}$ & 0.006$^{}$ & -0.000$^{}$ & 0.003$^{}$ & -0.003$^{}$  \\
 &  (0.161) & (0.175) & (0.013) & (0.013) & (0.012) & (0.012)  \\
Constant  &  1.293$^{*}$ & -0.163$^{}$ & 0.061$^{}$ & -0.063$^{}$ & 0.055$^{}$ & -0.066$^{}$  \\
 &  (0.588) & (0.486) & (0.044) & (0.066) & (0.034) & (0.057)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,655 & 1,655 & 1,655 & 1,655 & 1,655 & 1,655  \\
Adjusted $R^2$ &  0.002 & 0.004 & 0.009 & 0.016 & 0.008 & 0.015  \\
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
Treatment  &  0.236$^{}$ & 0.269$^{}$ & 0.010$^{}$ & -0.009$^{}$ & -0.018$^{}$ & -0.029$^{}$  \\
 &  (0.387) & (0.397) & (0.044) & (0.043) & (0.025) & (0.025)  \\
Constant  &  3.683$^{**}$ & 2.199$^{}$ & 0.581$^{***}$ & 0.084$^{}$ & 0.425$^{***}$ & 0.156$^{}$  \\
 &  (1.314) & (1.634) & (0.116) & (0.178) & (0.074) & (0.106)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,655 & 1,655 & 1,655 & 1,655 & 1,655 & 1,655  \\
Adjusted $R^2$ &  0.008 & 0.007 & 0.014 & 0.021 & 0.020 & 0.026  \\
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
Treatment  &  0.516$^{}$ & -0.291$^{}$ & -0.101$^{}$ & -0.174$^{}$ & 0.027$^{}$ & 0.005$^{}$  \\
 &  (1.173) & (1.162) & (0.165) & (0.165) & (0.052) & (0.057)  \\
Constant  &  5.938$^{*}$ & -2.041$^{}$ & 0.894$^{*}$ & -0.763$^{}$ & 0.197$^{}$ & -0.304$^{}$  \\
 &  (2.653) & (5.789) & (0.408) & (0.779) & (0.130) & (0.266)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  270 & 270 & 270 & 270 & 270 & 270  \\
Adjusted $R^2$ &  -0.025 & -0.021 & 0.101 & 0.107 & 0.111 & 0.119  \\
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
Treatment  &  0.740$^{}$ & 0.399$^{}$ & 0.021$^{}$ & 0.024$^{}$ & 0.090$^{}$ & 0.062$^{}$  \\
 &  (1.057) & (0.848) & (0.121) & (0.100) & (0.065) & (0.059)  \\
Constant  &  2.261$^{}$ & -8.839$^{*}$ & 0.314$^{}$ & -1.603$^{**}$ & 0.120$^{}$ & -0.963$^{**}$  \\
 &  (2.566) & (3.921) & (0.246) & (0.535) & (0.155) & (0.295)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  270 & 270 & 270 & 270 & 270 & 270  \\
Adjusted $R^2$ &  -0.033 & -0.013 & 0.045 & 0.084 & 0.045 & 0.098  \\
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
Treatment  &  -0.158$^{}$ & -0.649$^{}$ & -0.135$^{}$ & -0.219$^{+}$ & -0.101$^{}$ & -0.142$^{*}$  \\
 &  (0.974) & (0.985) & (0.116) & (0.125) & (0.063) & (0.063)  \\
Constant  &  2.845$^{}$ & 4.591$^{}$ & 0.548$^{}$ & 0.580$^{}$ & 0.223$^{}$ & 0.246$^{}$  \\
 &  (1.778) & (4.882) & (0.359) & (0.546) & (0.161) & (0.303)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  270 & 270 & 270 & 270 & 270 & 270  \\
Adjusted $R^2$ &  -0.025 & -0.022 & 0.047 & 0.075 & 0.037 & 0.061  \\
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
Treatment  &  1.080$^{}$ & 1.330$^{+}$ & 0.183$^{+}$ & 0.183$^{+}$ & 0.026$^{}$ & 0.017$^{}$  \\
 &  (0.727) & (0.793) & (0.093) & (0.101) & (0.034) & (0.032)  \\
Constant  &  5.667$^{***}$ & 4.366$^{}$ & 0.786$^{***}$ & -0.028$^{}$ & 0.484$^{***}$ & 0.143$^{}$  \\
 &  (1.385) & (4.164) & (0.129) & (0.514) & (0.067) & (0.186)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  812 & 812 & 812 & 812 & 812 & 812  \\
Adjusted $R^2$ &  0.002 & 0.000 & 0.002 & 0.001 & -0.009 & 0.001  \\
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
Treatment  &  0.229$^{}$ & 0.513$^{}$ & 0.080$^{}$ & 0.116$^{*}$ & 0.022$^{}$ & 0.032$^{}$  \\
 &  (0.392) & (0.428) & (0.049) & (0.054) & (0.029) & (0.027)  \\
Constant  &  0.908$^{+}$ & 1.732$^{}$ & 0.191$^{**}$ & 0.326$^{}$ & 0.166$^{**}$ & 0.045$^{}$  \\
 &  (0.532) & (2.406) & (0.072) & (0.262) & (0.051) & (0.150)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  812 & 812 & 812 & 812 & 812 & 812  \\
Adjusted $R^2$ &  0.012 & 0.020 & 0.011 & 0.023 & 0.006 & 0.019  \\
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
Treatment  &  0.869$^{}$ & 0.821$^{}$ & 0.107$^{}$ & 0.067$^{}$ & 0.029$^{}$ & 0.011$^{}$  \\
 &  (0.627) & (0.676) & (0.071) & (0.068) & (0.033) & (0.035)  \\
Constant  &  4.683$^{***}$ & 2.482$^{}$ & 0.577$^{***}$ & -0.390$^{}$ & 0.384$^{***}$ & 0.117$^{}$  \\
 &  (1.262) & (3.194) & (0.106) & (0.376) & (0.073) & (0.184)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  812 & 812 & 812 & 812 & 812 & 812  \\
Adjusted $R^2$ &  -0.004 & -0.003 & -0.000 & 0.004 & -0.002 & -0.000  \\
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
Treatment  &  0.227$^{}$ & 0.131$^{}$ & 0.150$^{}$ & 0.126$^{}$ & -0.005$^{}$ & -0.004$^{}$  \\
 &  (1.191) & (1.161) & (0.131) & (0.130) & (0.059) & (0.051)  \\
Constant  &  13.463$^{***}$ & 6.977$^{}$ & 1.248$^{***}$ & 1.542$^{}$ & 0.408$^{***}$ & 0.871$^{}$  \\
 &  (2.401) & (13.865) & (0.170) & (1.447) & (0.074) & (0.555)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  350 & 350 & 350 & 350 & 350 & 350  \\
Adjusted $R^2$ &  0.004 & -0.003 & 0.003 & 0.010 & 0.002 & 0.032  \\
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
Treatment  &  1.479$^{*}$ & 1.604$^{**}$ & 0.174$^{*}$ & 0.182$^{**}$ & 0.123$^{*}$ & 0.128$^{*}$  \\
 &  (0.603) & (0.613) & (0.068) & (0.069) & (0.048) & (0.050)  \\
Constant  &  -0.216$^{}$ & -0.091$^{}$ & 0.031$^{}$ & 0.229$^{}$ & 0.001$^{}$ & 0.017$^{}$  \\
 &  (0.409) & (4.601) & (0.082) & (0.649) & (0.052) & (0.443)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  350 & 350 & 350 & 350 & 350 & 350  \\
Adjusted $R^2$ &  0.002 & -0.002 & 0.020 & 0.009 & 0.012 & 0.015  \\
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
Treatment  &  -1.251$^{}$ & -1.473$^{}$ & -0.024$^{}$ & -0.056$^{}$ & -0.067$^{}$ & -0.069$^{}$  \\
 &  (1.177) & (1.180) & (0.114) & (0.116) & (0.064) & (0.059)  \\
Constant  &  13.679$^{***}$ & 7.068$^{}$ & 1.217$^{***}$ & 1.313$^{}$ & 0.436$^{***}$ & 0.780$^{}$  \\
 &  (2.400) & (12.765) & (0.153) & (1.192) & (0.081) & (0.574)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  350 & 350 & 350 & 350 & 350 & 350  \\
Adjusted $R^2$ &  -0.000 & -0.007 & -0.008 & 0.011 & -0.003 & 0.011  \\
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
F-statistic: 3.608 
p-value: 0.0062 
Degrees of freedom: 4 

The treatment effect on Black speaker representation varies significantly across disciplines (p < 0.05).
This indicates that the diversity intervention has heterogeneous effects depending on the academic field.

\textbf{F-test for Treatment × Discipline Interactions (URM Speakers):}
F-statistic: 0.649 
p-value: 0.6276 
Degrees of freedom: 4 

\textbf{F-test for Treatment × Discipline Interactions (% Black Speakers):}
F-statistic: 2.431 
p-value: 0.0458 
Degrees of freedom: 4 

\textbf{F-test for Treatment × Discipline Interactions (Total Black Speakers):}
F-statistic: 4.13 
p-value: 0.0025 
Degrees of freedom: 4 

\textbf{Individual Interaction Effects (Black Speakers):}
                                      Estimate Std. Error t value Pr(>|t|)
treatment:disc_mathematics             -0.0584     0.0605 -0.9662   0.3341
treatment:disc_physics                  0.0222     0.0685  0.3244   0.7457
treatment:disc_computer_science        -0.1074     0.0879 -1.2225   0.2217
treatment:disc_mechanical_engineering   0.2797     0.1059  2.6419   0.0083

\newpage

# Semester-Specific Analysis

## Fall Semester


Call:
lm(formula = as.formula(formula_str), data = data_complete)

Residuals:
    Min      1Q  Median      3Q     Max 
-12.605  -7.477  -4.980   3.554  95.007 

Coefficients:
                            Estimate Std. Error t value Pr(>|t|)   
(Intercept)                  6.35696    2.14015   2.970  0.00302 **
treatment                    0.94922    0.72180   1.315  0.18870   
bin_0_1                      1.48922    1.89568   0.786  0.43224   
bin_1_3                      1.14316    1.82433   0.627  0.53101   
bin_3_5                      2.00801    1.74786   1.149  0.25081   
bin_5_7                     -0.03272    1.74150  -0.019  0.98501   
bin_7_11                     2.18899    1.68911   1.296  0.19520   
bin_11_17                   -1.42973    1.67659  -0.853  0.39393   
disc_mathematics             0.05245    1.19124   0.044  0.96489   
disc_physics                 0.34638    1.21922   0.284  0.77637   
disc_computer_science       -4.91430    1.54564  -3.179  0.00151 **
disc_mechanical_engineering -2.70485    1.89142  -1.430  0.15292   
batch_1                      0.87044    1.66325   0.523  0.60082   
batch_2                      1.38845    1.96032   0.708  0.47889   
batch_3                     -2.13347    1.55207  -1.375  0.16947   
batch_4                      2.76342    1.55058   1.782  0.07493 . 
batch_5                      0.89058    1.51030   0.590  0.55551   
batch_6                     -0.14252    1.51698  -0.094  0.92516   
batch_7                     -1.22984    1.50242  -0.819  0.41317   
batch_8                      0.61867    1.60368   0.386  0.69972   
batch_9                     -2.64601    1.53713  -1.721  0.08539 . 
---
Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1

Residual standard error: 13.5 on 1427 degrees of freedom
Multiple R-squared:  0.03113,	Adjusted R-squared:  0.01755 
F-statistic: 2.292 on 20 and 1427 DF,  p-value: 0.000971

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
Treatment  &  0.783$^{}$ & 0.878$^{}$ & 0.027$^{}$ & 0.030$^{}$ & -0.007$^{}$ & -0.007$^{}$  \\
 &  (0.744) & (0.777) & (0.055) & (0.056) & (0.029) & (0.028)  \\
Constant  &  7.449$^{***}$ & 6.781$^{*}$ & 0.886$^{***}$ & 0.761$^{**}$ & 0.509$^{***}$ & 0.378$^{**}$  \\
 &  (1.709) & (2.884) & (0.140) & (0.240) & (0.075) & (0.121)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,389 & 1,389 & 1,389 & 1,389 & 1,389 & 1,389  \\
Adjusted $R^2$ &  0.006 & 0.006 & 0.024 & 0.022 & 0.025 & 0.028  \\
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
Treatment  &  0.822$^{+}$ & 0.820$^{+}$ & 0.038$^{}$ & 0.040$^{}$ & 0.028$^{}$ & 0.030$^{}$  \\
 &  (0.460) & (0.440) & (0.035) & (0.034) & (0.023) & (0.023)  \\
Constant  &  1.802$^{+}$ & 1.456$^{}$ & 0.315$^{***}$ & 0.301$^{*}$ & 0.230$^{***}$ & 0.174$^{+}$  \\
 &  (1.023) & (1.712) & (0.088) & (0.147) & (0.059) & (0.100)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,389 & 1,389 & 1,389 & 1,389 & 1,389 & 1,389  \\
Adjusted $R^2$ &  0.010 & 0.010 & 0.032 & 0.034 & 0.023 & 0.022  \\
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
Treatment  &  -0.018$^{}$ & 0.072$^{}$ & -0.010$^{}$ & -0.011$^{}$ & -0.030$^{}$ & -0.031$^{}$  \\
 &  (0.628) & (0.675) & (0.040) & (0.040) & (0.026) & (0.027)  \\
Constant  &  5.424$^{***}$ & 5.097$^{*}$ & 0.553$^{***}$ & 0.438$^{**}$ & 0.389$^{***}$ & 0.296$^{**}$  \\
 &  (1.403) & (2.466) & (0.097) & (0.169) & (0.071) & (0.103)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,389 & 1,389 & 1,389 & 1,389 & 1,389 & 1,389  \\
Adjusted $R^2$ &  -0.004 & -0.003 & 0.008 & 0.010 & 0.014 & 0.017  \\
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
Treatment  &  0.729$^{}$ & 0.710$^{}$ & 0.101$^{}$ & 0.068$^{}$ & 0.022$^{}$ & 0.011$^{}$  \\
 &  (0.515) & (0.512) & (0.065) & (0.063) & (0.025) & (0.023)  \\
Constant  &  9.084$^{***}$ & 4.778$^{*}$ & 1.059$^{***}$ & 0.220$^{}$ & 0.515$^{***}$ & 0.185$^{+}$  \\
 &  (1.636) & (1.962) & (0.178) & (0.249) & (0.079) & (0.109)  \\
Department Ranking  &  0.015$^{}$ & 0.029$^{*}$ & -0.003$^{*}$ & -0.001$^{}$ & -0.002$^{**}$ & -0.001$^{}$  \\
 &  (0.013) & (0.013) & (0.001) & (0.001) & (0.001) & (0.001)  \\
Treatment $\times$ Department Ranking  &  0.008$^{}$ & 0.007$^{}$ & 0.005$^{*}$ & 0.005$^{**}$ & 0.001$^{}$ & 0.001$^{+}$  \\
 &  (0.016) & (0.016) & (0.002) & (0.002) & (0.001) & (0.001)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,655 & 1,655 & 1,655 & 1,655 & 1,655 & 1,655  \\
Adjusted $R^2$ &  0.013 & 0.017 & 0.034 & 0.044 & 0.031 & 0.043  \\
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
Treatment  &  0.658$^{*}$ & 0.657$^{*}$ & 0.081$^{*}$ & 0.079$^{*}$ & 0.056$^{*}$ & 0.054$^{*}$  \\
 &  (0.307) & (0.291) & (0.039) & (0.037) & (0.023) & (0.023)  \\
Constant  &  3.202$^{***}$ & 1.541$^{}$ & 0.483$^{***}$ & 0.171$^{}$ & 0.263$^{***}$ & 0.052$^{}$  \\
 &  (0.840) & (1.168) & (0.115) & (0.151) & (0.066) & (0.097)  \\
Department Ranking  &  0.006$^{}$ & 0.012$^{}$ & -0.000$^{}$ & 0.001$^{}$ & -0.001$^{+}$ & -0.000$^{}$  \\
 &  (0.007) & (0.008) & (0.001) & (0.001) & (0.000) & (0.001)  \\
Treatment $\times$ Department Ranking  &  0.004$^{}$ & 0.002$^{}$ & 0.002$^{*}$ & 0.002$^{+}$ & 0.001$^{}$ & 0.001$^{}$  \\
 &  (0.009) & (0.009) & (0.001) & (0.001) & (0.001) & (0.001)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,655 & 1,655 & 1,655 & 1,655 & 1,655 & 1,655  \\
Adjusted $R^2$ &  0.027 & 0.030 & 0.052 & 0.059 & 0.037 & 0.044  \\
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
Treatment  &  0.088$^{}$ & 0.058$^{}$ & 0.020$^{}$ & -0.013$^{}$ & -0.016$^{}$ & -0.030$^{}$  \\
 &  (0.453) & (0.468) & (0.049) & (0.048) & (0.025) & (0.025)  \\
Constant  &  5.606$^{***}$ & 2.954$^{}$ & 0.541$^{***}$ & 0.005$^{}$ & 0.389$^{***}$ & 0.138$^{}$  \\
 &  (1.522) & (1.796) & (0.149) & (0.198) & (0.079) & (0.101)  \\
Department Ranking  &  0.008$^{}$ & 0.017$^{}$ & -0.003$^{**}$ & -0.001$^{}$ & -0.001$^{*}$ & -0.000$^{}$  \\
 &  (0.011) & (0.011) & (0.001) & (0.001) & (0.001) & (0.001)  \\
Treatment $\times$ Department Ranking  &  0.005$^{}$ & 0.005$^{}$ & 0.002$^{+}$ & 0.003$^{*}$ & 0.001$^{}$ & 0.001$^{}$  \\
 &  (0.013) & (0.013) & (0.001) & (0.001) & (0.001) & (0.001)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,655 & 1,655 & 1,655 & 1,655 & 1,655 & 1,655  \\
Adjusted $R^2$ &  0.005 & 0.006 & 0.018 & 0.024 & 0.021 & 0.026  \\
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
Treatment  &  0.958$^{+}$ & 0.744$^{}$ & 0.080$^{}$ & 0.072$^{}$ & 0.012$^{}$ & 0.014$^{}$  \\
 &  (0.531) & (0.511) & (0.068) & (0.064) & (0.025) & (0.024)  \\
Constant  &  7.792$^{***}$ & 2.224$^{}$ & 1.087$^{***}$ & 0.191$^{}$ & 0.551$^{***}$ & 0.185$^{+}$  \\
 &  (1.568) & (2.043) & (0.177) & (0.279) & (0.071) & (0.111)  \\
Total Faculty  &  -0.039$^{}$ & -0.032$^{}$ & 0.003$^{}$ & 0.002$^{}$ & 0.001$^{}$ & -0.001$^{}$  \\
 &  (0.026) & (0.026) & (0.003) & (0.003) & (0.001) & (0.001)  \\
Treatment $\times$ Total Faculty  &  0.030$^{}$ & 0.016$^{}$ & -0.001$^{}$ & -0.003$^{}$ & 0.001$^{}$ & 0.000$^{}$  \\
 &  (0.029) & (0.028) & (0.003) & (0.003) & (0.001) & (0.001)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,655 & 1,655 & 1,655 & 1,655 & 1,655 & 1,655  \\
Adjusted $R^2$ &  0.012 & 0.017 & 0.030 & 0.039 & 0.029 & 0.041  \\
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
Treatment  &  0.769$^{*}$ & 0.655$^{*}$ & 0.091$^{*}$ & 0.078$^{*}$ & 0.055$^{*}$ & 0.053$^{*}$  \\
 &  (0.310) & (0.290) & (0.041) & (0.037) & (0.023) & (0.023)  \\
Constant  &  2.798$^{***}$ & 0.320$^{}$ & 0.462$^{***}$ & 0.034$^{}$ & 0.302$^{***}$ & 0.016$^{}$  \\
 &  (0.795) & (1.329) & (0.103) & (0.170) & (0.064) & (0.104)  \\
Total Faculty  &  -0.014$^{}$ & -0.013$^{}$ & -0.000$^{}$ & -0.000$^{}$ & 0.001$^{}$ & -0.000$^{}$  \\
 &  (0.011) & (0.010) & (0.001) & (0.002) & (0.001) & (0.001)  \\
Treatment $\times$ Total Faculty  &  0.004$^{}$ & -0.004$^{}$ & -0.002$^{}$ & -0.003$^{+}$ & -0.001$^{}$ & -0.002$^{}$  \\
 &  (0.015) & (0.014) & (0.002) & (0.002) & (0.001) & (0.001)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,655 & 1,655 & 1,655 & 1,655 & 1,655 & 1,655  \\
Adjusted $R^2$ &  0.026 & 0.030 & 0.048 & 0.057 & 0.035 & 0.045  \\
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
Treatment  &  0.194$^{}$ & 0.093$^{}$ & -0.012$^{}$ & -0.008$^{}$ & -0.029$^{}$ & -0.027$^{}$  \\
 &  (0.467) & (0.465) & (0.048) & (0.048) & (0.025) & (0.025)  \\
Constant  &  4.788$^{**}$ & 1.726$^{}$ & 0.597$^{***}$ & 0.127$^{}$ & 0.393$^{***}$ & 0.182$^{+}$  \\
 &  (1.489) & (1.764) & (0.149) & (0.202) & (0.071) & (0.107)  \\
Total Faculty  &  -0.023$^{}$ & -0.017$^{}$ & 0.004$^{}$ & 0.002$^{}$ & 0.001$^{}$ & 0.000$^{}$  \\
 &  (0.026) & (0.026) & (0.003) & (0.003) & (0.001) & (0.001)  \\
Treatment $\times$ Total Faculty  &  0.024$^{}$ & 0.019$^{}$ & 0.001$^{}$ & 0.001$^{}$ & 0.002$^{}$ & 0.001$^{}$  \\
 &  (0.027) & (0.026) & (0.003) & (0.003) & (0.001) & (0.001)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,655 & 1,655 & 1,655 & 1,655 & 1,655 & 1,655  \\
Adjusted $R^2$ &  0.005 & 0.006 & 0.018 & 0.022 & 0.023 & 0.026  \\
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
Treatment  &  0.779$^{}$ & 0.696$^{}$ & 0.105$^{}$ & 0.073$^{}$ & 0.022$^{}$ & 0.013$^{}$  \\
 &  (0.519) & (0.516) & (0.064) & (0.064) & (0.025) & (0.023)  \\
Constant  &  7.738$^{***}$ & 6.936$^{***}$ & 1.054$^{***}$ & 0.760$^{***}$ & 0.552$^{***}$ & 0.409$^{***}$  \\
 &  (1.569) & (1.811) & (0.162) & (0.220) & (0.069) & (0.098)  \\
Peer URM Faculty  &  0.072$^{}$ & 0.145$^{**}$ & 0.017$^{**}$ & 0.021$^{***}$ & 0.007$^{**}$ & 0.007$^{**}$  \\
 &  (0.053) & (0.054) & (0.005) & (0.006) & (0.002) & (0.002)  \\
Treatment $\times$ Peer URM Faculty  &  -0.064$^{}$ & -0.054$^{}$ & -0.004$^{}$ & -0.006$^{}$ & -0.001$^{}$ & -0.001$^{}$  \\
 &  (0.072) & (0.071) & (0.008) & (0.008) & (0.003) & (0.003)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,655 & 1,655 & 1,655 & 1,655 & 1,655 & 1,655  \\
Adjusted $R^2$ &  0.011 & 0.017 & 0.037 & 0.039 & 0.037 & 0.041  \\
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
Treatment  &  0.679$^{*}$ & 0.663$^{*}$ & 0.085$^{*}$ & 0.083$^{*}$ & 0.057$^{*}$ & 0.057$^{*}$  \\
 &  (0.305) & (0.291) & (0.039) & (0.037) & (0.023) & (0.023)  \\
Constant  &  2.682$^{***}$ & 2.371$^{*}$ & 0.419$^{***}$ & 0.357$^{*}$ & 0.277$^{***}$ & 0.222$^{**}$  \\
 &  (0.784) & (1.006) & (0.102) & (0.143) & (0.061) & (0.085)  \\
Peer URM Faculty  &  0.011$^{}$ & 0.039$^{}$ & 0.003$^{}$ & 0.007$^{}$ & 0.003$^{}$ & 0.003$^{}$  \\
 &  (0.023) & (0.029) & (0.003) & (0.004) & (0.002) & (0.002)  \\
Treatment $\times$ Peer URM Faculty  &  -0.001$^{}$ & 0.007$^{}$ & 0.000$^{}$ & 0.001$^{}$ & 0.003$^{}$ & 0.003$^{}$  \\
 &  (0.037) & (0.037) & (0.005) & (0.005) & (0.002) & (0.003)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,655 & 1,655 & 1,655 & 1,655 & 1,655 & 1,655  \\
Adjusted $R^2$ &  0.025 & 0.030 & 0.048 & 0.056 & 0.040 & 0.044  \\
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
Treatment  &  0.114$^{}$ & 0.038$^{}$ & 0.020$^{}$ & -0.012$^{}$ & -0.015$^{}$ & -0.029$^{}$  \\
 &  (0.454) & (0.472) & (0.047) & (0.048) & (0.025) & (0.025)  \\
Constant  &  4.841$^{***}$ & 4.262$^{*}$ & 0.608$^{***}$ & 0.357$^{+}$ & 0.415$^{***}$ & 0.282$^{**}$  \\
 &  (1.426) & (1.696) & (0.131) & (0.182) & (0.072) & (0.087)  \\
Peer URM Faculty  &  0.062$^{}$ & 0.104$^{*}$ & 0.015$^{***}$ & 0.014$^{**}$ & 0.005$^{*}$ & 0.005$^{+}$  \\
 &  (0.048) & (0.051) & (0.004) & (0.005) & (0.002) & (0.003)  \\
Treatment $\times$ Peer URM Faculty  &  -0.064$^{}$ & -0.062$^{}$ & -0.005$^{}$ & -0.007$^{}$ & 0.000$^{}$ & -0.001$^{}$  \\
 &  (0.063) & (0.063) & (0.006) & (0.006) & (0.003) & (0.003)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,655 & 1,655 & 1,655 & 1,655 & 1,655 & 1,655  \\
Adjusted $R^2$ &  0.006 & 0.006 & 0.022 & 0.022 & 0.024 & 0.025  \\
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
Treatment  &  0.046$^{}$ & 0.039$^{}$ & 0.041$^{}$ & 0.016$^{}$ & -0.006$^{}$ & -0.011$^{}$  \\
 &  (0.669) & (0.659) & (0.084) & (0.082) & (0.032) & (0.030)  \\
Constant  &  8.300$^{***}$ & 3.639$^{+}$ & 1.161$^{***}$ & 0.216$^{}$ & 0.602$^{***}$ & 0.219$^{+}$  \\
 &  (1.668) & (2.070) & (0.177) & (0.275) & (0.073) & (0.115)  \\
\% Female Recipients  &  -1.112$^{}$ & -1.145$^{}$ & -0.206$^{}$ & -0.215$^{}$ & -0.104$^{}$ & -0.093$^{}$  \\
 &  (1.314) & (1.318) & (0.158) & (0.160) & (0.064) & (0.063)  \\
Treatment $\times$ \% Female Recipients  &  3.723$^{+}$ & 3.469$^{+}$ & 0.277$^{}$ & 0.271$^{}$ & 0.120$^{}$ & 0.108$^{}$  \\
 &  (1.923) & (1.917) & (0.226) & (0.223) & (0.086) & (0.083)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,655 & 1,655 & 1,655 & 1,655 & 1,655 & 1,655  \\
Adjusted $R^2$ &  0.012 & 0.018 & 0.030 & 0.039 & 0.028 & 0.042  \\
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
Treatment  &  0.389$^{}$ & 0.432$^{}$ & 0.078$^{}$ & 0.085$^{+}$ & 0.044$^{}$ & 0.048$^{+}$  \\
 &  (0.391) & (0.390) & (0.050) & (0.050) & (0.029) & (0.029)  \\
Constant  &  2.799$^{**}$ & 1.028$^{}$ & 0.443$^{***}$ & 0.106$^{}$ & 0.291$^{***}$ & 0.053$^{}$  \\
 &  (0.858) & (1.305) & (0.110) & (0.168) & (0.064) & (0.105)  \\
\% Female Recipients  &  -0.133$^{}$ & 0.071$^{}$ & -0.060$^{}$ & -0.031$^{}$ & -0.007$^{}$ & 0.007$^{}$  \\
 &  (0.848) & (0.847) & (0.099) & (0.101) & (0.060) & (0.061)  \\
Treatment $\times$ \% Female Recipients  &  1.546$^{}$ & 1.285$^{}$ & 0.016$^{}$ & -0.020$^{}$ & 0.063$^{}$ & 0.043$^{}$  \\
 &  (1.383) & (1.374) & (0.132) & (0.131) & (0.085) & (0.084)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,655 & 1,655 & 1,655 & 1,655 & 1,655 & 1,655  \\
Adjusted $R^2$ &  0.027 & 0.031 & 0.047 & 0.055 & 0.035 & 0.043  \\
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
Treatment  &  -0.318$^{}$ & -0.377$^{}$ & -0.038$^{}$ & -0.071$^{}$ & -0.023$^{}$ & -0.038$^{}$  \\
 &  (0.594) & (0.602) & (0.063) & (0.062) & (0.032) & (0.033)  \\
Constant  &  5.266$^{***}$ & 2.381$^{}$ & 0.690$^{***}$ & 0.074$^{}$ & 0.446$^{***}$ & 0.155$^{}$  \\
 &  (1.536) & (1.847) & (0.146) & (0.212) & (0.076) & (0.107)  \\
\% Female Recipients  &  -0.889$^{}$ & -1.145$^{}$ & -0.137$^{}$ & -0.179$^{}$ & -0.067$^{}$ & -0.079$^{}$  \\
 &  (1.069) & (1.103) & (0.122) & (0.123) & (0.066) & (0.067)  \\
Treatment $\times$ \% Female Recipients  &  2.143$^{}$ & 2.145$^{}$ & 0.264$^{}$ & 0.294$^{}$ & 0.018$^{}$ & 0.027$^{}$  \\
 &  (1.708) & (1.701) & (0.184) & (0.183) & (0.090) & (0.092)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,655 & 1,655 & 1,655 & 1,655 & 1,655 & 1,655  \\
Adjusted $R^2$ &  0.005 & 0.006 & 0.015 & 0.022 & 0.019 & 0.025  \\
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
Treatment  &  0.261$^{}$ & 0.269$^{}$ & 0.099$^{}$ & 0.077$^{}$ & 0.021$^{}$ & 0.015$^{}$  \\
 &  (0.565) & (0.563) & (0.074) & (0.072) & (0.028) & (0.026)  \\
Constant  &  8.132$^{***}$ & 3.390$^{}$ & 1.103$^{***}$ & 0.161$^{}$ & 0.572$^{***}$ & 0.193$^{}$  \\
 &  (1.635) & (2.072) & (0.171) & (0.278) & (0.073) & (0.118)  \\
\% URM Recipients  &  0.556$^{}$ & 0.897$^{}$ & -0.007$^{}$ & 0.010$^{}$ & 0.017$^{}$ & 0.041$^{}$  \\
 &  (2.108) & (2.039) & (0.225) & (0.225) & (0.102) & (0.100)  \\
Treatment $\times$ \% URM Recipients  &  7.348$^{*}$ & 6.524$^{+}$ & 0.026$^{}$ & -0.012$^{}$ & -0.001$^{}$ & -0.020$^{}$  \\
 &  (3.594) & (3.551) & (0.348) & (0.343) & (0.143) & (0.136)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,655 & 1,655 & 1,655 & 1,655 & 1,655 & 1,655  \\
Adjusted $R^2$ &  0.016 & 0.022 & 0.029 & 0.038 & 0.027 & 0.041  \\
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
Treatment  &  0.287$^{}$ & 0.285$^{}$ & 0.065$^{}$ & 0.068$^{}$ & 0.044$^{+}$ & 0.044$^{+}$  \\
 &  (0.320) & (0.312) & (0.043) & (0.042) & (0.025) & (0.025)  \\
Constant  &  2.961$^{***}$ & 1.224$^{}$ & 0.447$^{***}$ & 0.124$^{}$ & 0.299$^{***}$ & 0.065$^{}$  \\
 &  (0.798) & (1.291) & (0.103) & (0.169) & (0.060) & (0.104)  \\
\% URM Recipients  &  -0.912$^{}$ & -0.897$^{}$ & -0.177$^{}$ & -0.154$^{}$ & -0.112$^{}$ & -0.106$^{}$  \\
 &  (1.102) & (1.081) & (0.124) & (0.121) & (0.081) & (0.077)  \\
Treatment $\times$ \% URM Recipients  &  5.395$^{*}$ & 5.131$^{+}$ & 0.235$^{}$ & 0.182$^{}$ & 0.148$^{}$ & 0.133$^{}$  \\
 &  (2.647) & (2.675) & (0.213) & (0.207) & (0.132) & (0.124)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,655 & 1,655 & 1,655 & 1,655 & 1,655 & 1,655  \\
Adjusted $R^2$ &  0.032 & 0.036 & 0.048 & 0.056 & 0.036 & 0.044  \\
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
Treatment  &  -0.017$^{}$ & -0.019$^{}$ & 0.031$^{}$ & 0.005$^{}$ & -0.016$^{}$ & -0.027$^{}$  \\
 &  (0.509) & (0.523) & (0.056) & (0.054) & (0.028) & (0.028)  \\
Constant  &  4.963$^{**}$ & 1.958$^{}$ & 0.632$^{***}$ & 0.004$^{}$ & 0.425$^{***}$ & 0.135$^{}$  \\
 &  (1.522) & (1.891) & (0.140) & (0.211) & (0.076) & (0.108)  \\
\% URM Recipients  &  1.441$^{}$ & 1.734$^{}$ & 0.156$^{}$ & 0.146$^{}$ & 0.051$^{}$ & 0.069$^{}$  \\
 &  (1.779) & (1.760) & (0.172) & (0.177) & (0.092) & (0.095)  \\
Treatment $\times$ \% URM Recipients  &  2.018$^{}$ & 1.501$^{}$ & -0.187$^{}$ & -0.167$^{}$ & -0.012$^{}$ & -0.019$^{}$  \\
 &  (3.163) & (3.118) & (0.254) & (0.257) & (0.144) & (0.144)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,655 & 1,655 & 1,655 & 1,655 & 1,655 & 1,655  \\
Adjusted $R^2$ &  0.006 & 0.007 & 0.014 & 0.021 & 0.019 & 0.025  \\
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
Treatment  &  -0.339$^{}$ & -0.207$^{}$ & -0.024$^{}$ & -0.042$^{}$ & 0.009$^{}$ & -0.001$^{}$  \\
 &  (0.749) & (0.746) & (0.094) & (0.093) & (0.035) & (0.033)  \\
Constant  &  7.944$^{***}$ & 3.544$^{+}$ & 1.108$^{***}$ & 0.209$^{}$ & 0.575$^{***}$ & 0.203$^{+}$  \\
 &  (1.659) & (2.078) & (0.172) & (0.270) & (0.073) & (0.116)  \\
\% URM Faculty  &  -6.109$^{}$ & -4.914$^{}$ & -0.793$^{}$ & -0.983$^{}$ & -0.181$^{}$ & -0.360$^{}$  \\
 &  (9.919) & (9.809) & (1.207) & (1.144) & (0.548) & (0.509)  \\
Treatment $\times$ \% URM Faculty  &  28.946$^{+}$ & 25.697$^{+}$ & 3.257$^{+}$ & 3.273$^{+}$ & 0.327$^{}$ & 0.397$^{}$  \\
 &  (15.678) & (15.501) & (1.960) & (1.936) & (0.666) & (0.651)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,655 & 1,655 & 1,655 & 1,655 & 1,655 & 1,655  \\
Adjusted $R^2$ &  0.013 & 0.018 & 0.032 & 0.041 & 0.027 & 0.041  \\
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
Treatment  &  0.050$^{}$ & 0.109$^{}$ & -0.002$^{}$ & 0.003$^{}$ & 0.019$^{}$ & 0.020$^{}$  \\
 &  (0.374) & (0.374) & (0.051) & (0.051) & (0.031) & (0.031)  \\
Constant  &  2.684$^{**}$ & 1.144$^{}$ & 0.434$^{***}$ & 0.134$^{}$ & 0.287$^{***}$ & 0.065$^{}$  \\
 &  (0.815) & (1.314) & (0.107) & (0.165) & (0.062) & (0.104)  \\
\% URM Faculty  &  -0.853$^{}$ & -0.770$^{}$ & -0.603$^{}$ & -0.636$^{}$ & -0.163$^{}$ & -0.272$^{}$  \\
 &  (4.612) & (4.637) & (0.616) & (0.606) & (0.407) & (0.390)  \\
Treatment $\times$ \% URM Faculty  &  15.946$^{+}$ & 15.287$^{+}$ & 2.257$^{*}$ & 2.197$^{*}$ & 0.947$^{}$ & 0.976$^{+}$  \\
 &  (8.399) & (8.347) & (1.082) & (1.024) & (0.577) & (0.561)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,655 & 1,655 & 1,655 & 1,655 & 1,655 & 1,655  \\
Adjusted $R^2$ &  0.029 & 0.032 & 0.051 & 0.059 & 0.037 & 0.045  \\
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
Treatment  &  -0.397$^{}$ & -0.329$^{}$ & -0.030$^{}$ & -0.055$^{}$ & 0.002$^{}$ & -0.011$^{}$  \\
 &  (0.729) & (0.732) & (0.081) & (0.080) & (0.036) & (0.036)  \\
Constant  &  5.045$^{***}$ & 2.191$^{}$ & 0.650$^{***}$ & 0.041$^{}$ & 0.431$^{***}$ & 0.134$^{}$  \\
 &  (1.518) & (1.859) & (0.141) & (0.210) & (0.074) & (0.107)  \\
\% URM Faculty  &  -5.206$^{}$ & -4.176$^{}$ & -0.278$^{}$ & -0.448$^{}$ & -0.021$^{}$ & -0.103$^{}$  \\
 &  (8.634) & (8.437) & (0.969) & (0.926) & (0.516) & (0.495)  \\
Treatment $\times$ \% URM Faculty  &  13.570$^{}$ & 10.946$^{}$ & 1.209$^{}$ & 1.271$^{}$ & -0.485$^{}$ & -0.493$^{}$  \\
 &  (15.052) & (14.934) & (1.711) & (1.743) & (0.667) & (0.660)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,655 & 1,655 & 1,655 & 1,655 & 1,655 & 1,655  \\
Adjusted $R^2$ &  0.005 & 0.006 & 0.014 & 0.022 & 0.019 & 0.025  \\
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
Treatment  &  1.719$^{}$ & 2.020$^{}$ & 0.186$^{}$ & 0.138$^{}$ & 0.099$^{}$ & 0.069$^{}$  \\
 &  (1.514) & (1.482) & (0.198) & (0.197) & (0.074) & (0.069)  \\
Constant  &  6.082$^{**}$ & 2.843$^{}$ & 0.956$^{***}$ & 0.146$^{}$ & 0.494$^{***}$ & 0.182$^{}$  \\
 &  (1.921) & (2.141) & (0.217) & (0.276) & (0.088) & (0.118)  \\
\% Women Faculty  &  8.999$^{+}$ & 9.169$^{+}$ & 0.729$^{}$ & 0.730$^{}$ & 0.420$^{}$ & 0.451$^{+}$  \\
 &  (4.940) & (4.878) & (0.721) & (0.706) & (0.285) & (0.268)  \\
Treatment $\times$ \% Women Faculty  &  -5.394$^{}$ & -6.592$^{}$ & -0.479$^{}$ & -0.316$^{}$ & -0.421$^{}$ & -0.285$^{}$  \\
 &  (7.314) & (7.064) & (1.003) & (0.976) & (0.359) & (0.338)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,655 & 1,655 & 1,655 & 1,655 & 1,655 & 1,655  \\
Adjusted $R^2$ &  0.012 & 0.017 & 0.030 & 0.039 & 0.028 & 0.042  \\
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
Treatment  &  0.343$^{}$ & 0.547$^{}$ & 0.053$^{}$ & 0.060$^{}$ & 0.044$^{}$ & 0.045$^{}$  \\
 &  (0.803) & (0.769) & (0.111) & (0.108) & (0.067) & (0.067)  \\
Constant  &  2.287$^{**}$ & 0.958$^{}$ & 0.366$^{**}$ & 0.109$^{}$ & 0.246$^{***}$ & 0.053$^{}$  \\
 &  (0.884) & (1.329) & (0.120) & (0.167) & (0.074) & (0.106)  \\
\% Women Faculty  &  1.623$^{}$ & 1.941$^{}$ & 0.249$^{}$ & 0.296$^{}$ & 0.175$^{}$ & 0.220$^{}$  \\
 &  (2.746) & (2.604) & (0.380) & (0.352) & (0.246) & (0.231)  \\
Treatment $\times$ \% Women Faculty  &  1.493$^{}$ & 0.574$^{}$ & 0.128$^{}$ & 0.113$^{}$ & 0.045$^{}$ & 0.050$^{}$  \\
 &  (4.389) & (4.025) & (0.611) & (0.567) & (0.340) & (0.330)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,655 & 1,655 & 1,655 & 1,655 & 1,655 & 1,655  \\
Adjusted $R^2$ &  0.026 & 0.030 & 0.048 & 0.056 & 0.035 & 0.043  \\
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
Treatment  &  1.338$^{}$ & 1.443$^{}$ & 0.128$^{}$ & 0.074$^{}$ & 0.093$^{}$ & 0.053$^{}$  \\
 &  (1.332) & (1.338) & (0.147) & (0.147) & (0.073) & (0.073)  \\
Constant  &  3.532$^{*}$ & 1.677$^{}$ & 0.549$^{**}$ & 0.002$^{}$ & 0.351$^{***}$ & 0.120$^{}$  \\
 &  (1.750) & (1.912) & (0.173) & (0.217) & (0.084) & (0.108)  \\
\% Women Faculty  &  7.558$^{+}$ & 7.409$^{+}$ & 0.541$^{}$ & 0.493$^{}$ & 0.447$^{+}$ & 0.423$^{}$  \\
 &  (4.163) & (4.144) & (0.533) & (0.545) & (0.258) & (0.264)  \\
Treatment $\times$ \% Women Faculty  &  -6.645$^{}$ & -6.988$^{}$ & -0.593$^{}$ & -0.418$^{}$ & -0.579$^{+}$ & -0.417$^{}$  \\
 &  (6.114) & (6.073) & (0.696) & (0.693) & (0.338) & (0.340)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,655 & 1,655 & 1,655 & 1,655 & 1,655 & 1,655  \\
Adjusted $R^2$ &  0.006 & 0.006 & 0.014 & 0.022 & 0.021 & 0.026  \\
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
Treatment  &  0.748$^{}$ & 0.626$^{}$ & 0.099$^{}$ & 0.062$^{}$ & 0.020$^{}$ & 0.009$^{}$  \\
 &  (0.517) & (0.516) & (0.066) & (0.064) & (0.025) & (0.024)  \\
Constant  &  11.207$^{***}$ & 5.224$^{+}$ & 1.032$^{***}$ & 0.240$^{}$ & 0.432$^{***}$ & 0.149$^{}$  \\
 &  (2.763) & (2.726) & (0.288) & (0.321) & (0.121) & (0.160)  \\
Number of Seminars  &  -0.237$^{}$ & -0.161$^{}$ & 0.012$^{}$ & -0.001$^{}$ & 0.014$^{}$ & 0.007$^{}$  \\
 &  (0.191) & (0.179) & (0.022) & (0.021) & (0.009) & (0.010)  \\
Treatment $\times$ Number of Seminars  &  -0.074$^{}$ & -0.096$^{}$ & -0.008$^{}$ & -0.019$^{+}$ & -0.003$^{}$ & -0.008$^{+}$  \\
 &  (0.085) & (0.089) & (0.010) & (0.011) & (0.004) & (0.005)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,655 & 1,655 & 1,655 & 1,655 & 1,655 & 1,655  \\
Adjusted $R^2$ &  0.012 & 0.017 & 0.029 & 0.039 & 0.028 & 0.042  \\
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
Treatment  &  0.668$^{*}$ & 0.652$^{*}$ & 0.083$^{*}$ & 0.081$^{*}$ & 0.055$^{*}$ & 0.053$^{*}$  \\
 &  (0.303) & (0.286) & (0.038) & (0.037) & (0.022) & (0.022)  \\
Constant  &  1.117$^{}$ & -1.195$^{}$ & 0.085$^{}$ & -0.319$^{+}$ & 0.035$^{}$ & -0.192$^{}$  \\
 &  (1.259) & (1.738) & (0.146) & (0.192) & (0.097) & (0.118)  \\
Number of Seminars  &  0.187$^{*}$ & 0.225$^{*}$ & 0.038$^{***}$ & 0.044$^{***}$ & 0.028$^{***}$ & 0.026$^{***}$  \\
 &  (0.087) & (0.097) & (0.010) & (0.011) & (0.007) & (0.007)  \\
Treatment $\times$ Number of Seminars  &  -0.067$^{}$ & -0.068$^{}$ & -0.011$^{*}$ & -0.013$^{*}$ & -0.008$^{*}$ & -0.009$^{*}$  \\
 &  (0.041) & (0.044) & (0.005) & (0.006) & (0.004) & (0.004)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,655 & 1,655 & 1,655 & 1,655 & 1,655 & 1,655  \\
Adjusted $R^2$ &  0.027 & 0.032 & 0.053 & 0.063 & 0.043 & 0.050  \\
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
Treatment  &  0.094$^{}$ & -0.022$^{}$ & 0.017$^{}$ & -0.021$^{}$ & -0.016$^{}$ & -0.032$^{}$  \\
 &  (0.445) & (0.470) & (0.048) & (0.047) & (0.025) & (0.025)  \\
Constant  &  9.973$^{***}$ & 6.382$^{*}$ & 0.940$^{***}$ & 0.555$^{*}$ & 0.469$^{***}$ & 0.266$^{+}$  \\
 &  (2.348) & (2.609) & (0.203) & (0.241) & (0.106) & (0.137)  \\
Number of Seminars  &  -0.434$^{**}$ & -0.403$^{*}$ & -0.029$^{+}$ & -0.049$^{**}$ & -0.006$^{}$ & -0.011$^{}$  \\
 &  (0.158) & (0.165) & (0.016) & (0.016) & (0.008) & (0.008)  \\
Treatment $\times$ Number of Seminars  &  -0.005$^{}$ & -0.027$^{}$ & 0.004$^{}$ & -0.006$^{}$ & 0.003$^{}$ & -0.002$^{}$  \\
 &  (0.075) & (0.079) & (0.009) & (0.008) & (0.005) & (0.005)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,655 & 1,655 & 1,655 & 1,655 & 1,655 & 1,655  \\
Adjusted $R^2$ &  0.009 & 0.008 & 0.015 & 0.026 & 0.019 & 0.026  \\
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

Total seminars analyzed: 1655\\[0.3em]
Seminars with junior speakers: 1518 (91.7\%)\\[0.3em]
Seminars with senior speakers: 1536 (92.8\%)\\[0.3em]
Mean junior speakers per seminar: 5.99\\[0.3em]
Mean senior speakers per seminar: 5.87\\[0.3em]
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
\% of speakers & 0.0106 & 0.0062 & & 0.0056 & 0.0073 \\
Count & 0.0598 & 0.0386 & & -0.0258 & -0.0235 \\
Any (0/1) & 0.0237 & 0.0104 & & -0.0119 & -0.0066 \\
\midrule
\textit{Mean (Control)} & & & & & \\
\% of speakers & 0.069 & & & 0.059 & \\
Count & 0.410 & & & 0.401 & \\
Any (0/1) & 0.301 & & & 0.284 & \\
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
\% of speakers & 0.0090+ & 0.0075 & & 0.0041 & 0.0046 \\
Count & 0.0454* & 0.0454* & & 0.0053 & 0.0046 \\
Any (0/1) & 0.0411** & 0.0413* & & 0.0125 & 0.0123 \\
\midrule
\textit{Mean (Control)} & & & & & \\
\% of speakers & 0.020 & & & 0.013 & \\
Count & 0.109 & & & 0.111 & \\
Any (0/1) & 0.093 & & & 0.089 & \\
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
\% of speakers & 0.0013 & -0.0018 & & 0.0014 & 0.0027 \\
Count & 0.0130 & -0.0100 & & -0.0311 & -0.0280 \\
Any (0/1) & -0.0114 & -0.0273 & & -0.0173 & -0.0134 \\
\midrule
\textit{Mean (Control)} & & & & & \\
\% of speakers & 0.048 & & & 0.046 & \\
Count & 0.299 & & & 0.290 & \\
Any (0/1) & 0.238 & & & 0.222 & \\
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
\footnotesize
\setlength{\tabcolsep}{4pt}
\begin{tabular}{p{3.5cm} p{2.2cm} p{3.2cm} p{1.2cm} r r r r c}
\toprule
Analysis & Outcome & Variable & Model & Coef. & SE & t-stat & p-value & Sig. \\
\midrule
\multicolumn{9}{l}{\textbf{Career Stage Analysis}} \\
\midrule
Junior/Senior Black Speakers & Junior Any (0/1) & Treatment & Simple & 0.0411 & 0.0158 & 2.594 & 0.0096 & ** \\
Junior/Senior Black Speakers & Junior Count & Treatment & Simple & 0.0454 & 0.0200 & 2.265 & 0.0236 & * \\
Junior/Senior Black Speakers & Junior \\% of speakers & Treatment & Simple & 0.0090 & 0.0049 & 1.821 & 0.0688 & + \\
\addlinespace[0.5em]
\multicolumn{9}{l}{\textbf{Demographic Subgroups}} \\
\midrule
Demographic Subgroup & \% Black & Treatment & Extended & 0.6604 & 0.2936 & 2.249 & 0.0246 & * \\
Demographic Subgroup & \% Black Female & Treatment & Extended & 0.1546 & 0.0720 & 2.146 & 0.0320 & * \\
Demographic Subgroup & \% Black Male & Treatment & Extended & 0.5058 & 0.2483 & 2.037 & 0.0418 & * \\
Demographic Subgroup & Any Black & Treatment & Simple & 0.0558 & 0.0227 & 2.457 & 0.0141 & * \\
Demographic Subgroup & Any Black Female & Treatment & Extended & 0.0149 & 0.0081 & 1.837 & 0.0663 & + \\
Demographic Subgroup & Any Black Male & Treatment & Simple & 0.0590 & 0.0225 & 2.625 & 0.0087 & ** \\
Demographic Subgroup & Count Black & Treatment & Extended & 0.0826 & 0.0377 & 2.192 & 0.0285 & * \\
Demographic Subgroup & Count Black Male & Treatment & Extended & 0.0710 & 0.0326 & 2.176 & 0.0297 & * \\
\\% Female Recipients & \% URM & Treatment × \\% Female Recipients & Simple & 3.7233 & 1.9235 & 1.936 & 0.0531 & + \\
\addlinespace[0.5em]
\multicolumn{9}{l}{\textbf{Discipline Analysis}} \\
\midrule
Chemistry & Any Hispanic & Treatment & Extended & -0.1418 & 0.0630 & -2.250 & 0.0253 & * \\
Chemistry & Count Hispanic & Treatment & Extended & -0.2186 & 0.1246 & -1.755 & 0.0805 & + \\
Computer Science & Any Hispanic & Treatment & Extended & 0.1556 & 0.0892 & 1.745 & 0.0836 & + \\
Mathematics & \% URM & Treatment & Extended & 1.3298 & 0.7933 & 1.676 & 0.0941 & + \\
Mathematics & Count Black & Treatment & Extended & 0.1164 & 0.0542 & 2.146 & 0.0322 & * \\
Mathematics & Count URM & Treatment & Simple & 0.1828 & 0.0935 & 1.956 & 0.0508 & + \\
Mechanical Engineering & \% Black & Treatment & Simple & 3.9420 & 0.9989 & 3.946 & 0.0002 & *** \\
Mechanical Engineering & \% URM & Treatment & Simple & 3.8590 & 2.0259 & 1.905 & 0.0613 & + \\
Mechanical Engineering & Any Black & Treatment & Simple & 0.3462 & 0.0898 & 3.855 & 0.0003 & *** \\
Mechanical Engineering & Count Black & Treatment & Simple & 0.6458 & 0.1853 & 3.486 & 0.0009 & *** \\
Mechanical Engineering & Count URM & Treatment & Simple & 0.6652 & 0.2998 & 2.219 & 0.0301 & * \\
Physics & \% Black & Treatment & Extended & 1.6042 & 0.6127 & 2.618 & 0.0093 & ** \\
Physics & Any Black & Treatment & Simple & 0.1228 & 0.0479 & 2.561 & 0.0109 & * \\
Physics & Count Black & Treatment & Extended & 0.1820 & 0.0692 & 2.629 & 0.0090 & ** \\
\addlinespace[0.5em]
\multicolumn{9}{l}{\textbf{Heterogeneity Analysis}} \\
\midrule
Department Ranking & Any URM & Treatment × Department Ranking & Extended & 0.0012 & 0.0006 & 1.796 & 0.0727 & + \\
Department Ranking & Count Black & Treatment × Department Ranking & Simple & 0.0023 & 0.0012 & 1.967 & 0.0493 & * \\
Department Ranking & Count Hispanic & Treatment × Department Ranking & Extended & 0.0027 & 0.0012 & 2.216 & 0.0268 & * \\
Department Ranking & Count URM & Treatment × Department Ranking & Extended & 0.0050 & 0.0018 & 2.809 & 0.0050 & ** \\
Number of Seminars & Any Black & Treatment × Number of Seminars & Extended & -0.0094 & 0.0038 & -2.479 & 0.0133 & * \\
Number of Seminars & Any URM & Treatment × Number of Seminars & Extended & -0.0079 & 0.0046 & -1.727 & 0.0843 & + \\
Number of Seminars & Count Black & Treatment × Number of Seminars & Extended & -0.0126 & 0.0058 & -2.196 & 0.0282 & * \\
Number of Seminars & Count URM & Treatment × Number of Seminars & Extended & -0.0192 & 0.0110 & -1.753 & 0.0798 & + \\
Total Faculty & Count Black & Treatment × Total Faculty & Extended & -0.0030 & 0.0018 & -1.668 & 0.0955 & + \\
\\% URM Faculty & \% Black & Treatment × \\% URM Faculty & Simple & 15.9456 & 8.3988 & 1.899 & 0.0578 & + \\
\\% URM Faculty & \% URM & Treatment × \\% URM Faculty & Simple & 28.9457 & 15.6782 & 1.846 & 0.0650 & + \\
\\% URM Faculty & Any Black & Treatment × \\% URM Faculty & Extended & 0.9762 & 0.5607 & 1.741 & 0.0818 & + \\
\\% URM Faculty & Count Black & Treatment × \\% URM Faculty & Extended & 2.1965 & 1.0235 & 2.146 & 0.0320 & * \\
\\% URM Faculty & Count URM & Treatment × \\% URM Faculty & Extended & 3.2726 & 1.9360 & 1.690 & 0.0911 & + \\
\\% URM Recipients & \% Black & Treatment × \\% URM Recipients & Simple & 5.3952 & 2.6474 & 2.038 & 0.0417 & * \\
\\% URM Recipients & \% URM & Treatment × \\% URM Recipients & Simple & 7.3483 & 3.5938 & 2.045 & 0.0410 & * \\
\\% Women Faculty & Any Hispanic & Treatment × \\% Women Faculty & Simple & -0.5785 & 0.3375 & -1.714 & 0.0867 & + \\
\addlinespace[0.5em]
\multicolumn{9}{l}{\textbf{Semester Analysis}} \\
\midrule
Fall Semester & Any Black & Treatment & Simple & 0.0434 & 0.0167 & 2.603 & 0.0093 & ** \\
Fall Semester & Count Black & Treatment & Simple & 0.0531 & 0.0209 & 2.541 & 0.0112 & * \\
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
\footnotesize
\setlength{\tabcolsep}{4pt}
\begin{tabular}{p{3.5cm} p{2.2cm} p{3.2cm} p{1.2cm} r r r r c}
\toprule
Analysis & Outcome & Variable & Model & Coef. & SE & t-stat & p-value & Sig. \\
\midrule
\multicolumn{9}{l}{\textbf{Semester Analysis}} \\
\midrule
Fall Semester & Count URM & Treatment & Simple & 0.0780 & 0.0456 & 1.711 & 0.0873 & + \\
Spring Semester & \% Black & Treatment & Extended & 0.8204 & 0.4401 & 1.864 & 0.0625 & + \\
\bottomrule
\end{tabular}
\parbox{\linewidth}{\footnotesize Note: Significance levels: + p<0.1; * p<0.05; ** p<0.01; *** p<0.001. SE = Clustered standard errors at department level. For moderation analyses, only significant interaction terms are shown.}
\end{table}
\end{landscape}
