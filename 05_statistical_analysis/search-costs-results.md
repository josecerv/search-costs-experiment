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
Treatment  &  0.658$^{}$ & 0.611$^{}$ & 0.090$^{}$ & 0.060$^{}$ & 0.009$^{}$ & 0.003$^{}$  \\
 &  (0.539) & (0.535) & (0.070) & (0.067) & (0.025) & (0.023)  \\
Constant  &  8.523$^{***}$ & 3.953$^{+}$ & 1.251$^{***}$ & 0.280$^{}$ & 0.635$^{***}$ & 0.268$^{*}$  \\
 &  (1.580) & (2.152) & (0.176) & (0.294) & (0.063) & (0.110)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,656 & 1,656 & 1,656 & 1,656 & 1,656 & 1,656  \\
Adjusted $R^2$ &  0.011 & 0.015 & 0.026 & 0.034 & 0.032 & 0.046  \\
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
Treatment  &  -0.461$^{}$ & -0.427$^{}$ & 0.090$^{}$ & 0.060$^{}$ & -0.542$^{}$ & -0.483$^{}$  \\
 &  (0.554) & (0.546) & (0.070) & (0.067) & (0.524) & (0.516)  \\
Constant  &  16.810$^{***}$ & 13.460$^{***}$ & 1.251$^{***}$ & 0.280$^{}$ & 15.529$^{***}$ & 13.088$^{***}$  \\
 &  (1.313) & (2.452) & (0.176) & (0.294) & (1.234) & (2.298)  \\
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
Treatment  &  0.561$^{+}$ & 0.549$^{+}$ & 0.068$^{}$ & 0.067$^{+}$ & 0.042$^{+}$ & 0.044$^{+}$  \\
 &  (0.313) & (0.293) & (0.042) & (0.039) & (0.023) & (0.023)  \\
Constant  &  2.874$^{***}$ & 0.771$^{}$ & 0.459$^{***}$ & 0.124$^{}$ & 0.295$^{***}$ & 0.087$^{}$  \\
 &  (0.830) & (1.351) & (0.113) & (0.176) & (0.066) & (0.110)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,656 & 1,656 & 1,656 & 1,656 & 1,656 & 1,656  \\
Adjusted $R^2$ &  0.028 & 0.034 & 0.048 & 0.057 & 0.042 & 0.050  \\
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
Treatment  &  0.111$^{}$ & 0.068$^{}$ & 0.021$^{}$ & -0.009$^{}$ & -0.008$^{}$ & -0.016$^{}$  \\
 &  (0.468) & (0.484) & (0.052) & (0.051) & (0.025) & (0.025)  \\
Constant  &  5.437$^{***}$ & 2.967$^{}$ & 0.766$^{***}$ & 0.120$^{}$ & 0.504$^{***}$ & 0.239$^{*}$  \\
 &  (1.458) & (1.928) & (0.146) & (0.240) & (0.065) & (0.107)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,656 & 1,656 & 1,656 & 1,656 & 1,656 & 1,656  \\
Adjusted $R^2$ &  0.005 & 0.004 & 0.013 & 0.021 & 0.019 & 0.024  \\
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
Treatment  &  0.087$^{}$ & -0.441$^{}$ & -0.061$^{}$ & -0.129$^{}$ & -0.007$^{}$ & -0.013$^{}$  \\
 &  (0.823) & (0.810) & (0.129) & (0.127) & (0.021) & (0.021)  \\
Constant  &  22.166$^{***}$ & 13.612$^{***}$ & 3.631$^{***}$ & 2.188$^{***}$ & 0.884$^{***}$ & 0.688$^{***}$  \\
 &  (2.010) & (3.942) & (0.342) & (0.594) & (0.061) & (0.099)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,656 & 1,656 & 1,656 & 1,656 & 1,656 & 1,656  \\
Adjusted $R^2$ &  0.050 & 0.059 & 0.087 & 0.104 & 0.017 & 0.028  \\
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
Treatment  &  -0.056$^{}$ & -0.123$^{}$ & 0.017$^{}$ & 0.006$^{}$ & 0.011$^{}$ & 0.002$^{}$  \\
 &  (0.174) & (0.185) & (0.019) & (0.019) & (0.017) & (0.017)  \\
Constant  &  1.883$^{**}$ & -0.113$^{}$ & 0.220$^{***}$ & -0.056$^{}$ & 0.190$^{***}$ & -0.063$^{}$  \\
 &  (0.611) & (0.599) & (0.062) & (0.091) & (0.052) & (0.078)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,656 & 1,656 & 1,656 & 1,656 & 1,656 & 1,656  \\
Adjusted $R^2$ &  0.015 & 0.020 & 0.043 & 0.058 & 0.046 & 0.061  \\
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
Treatment  &  0.098$^{}$ & 0.111$^{}$ & 0.003$^{}$ & 0.003$^{}$ & 0.005$^{}$ & 0.006$^{}$  \\
 &  (0.073) & (0.074) & (0.010) & (0.009) & (0.009) & (0.009)  \\
Constant  &  0.584$^{***}$ & 0.138$^{}$ & 0.079$^{**}$ & 0.022$^{}$ & 0.066$^{**}$ & 0.022$^{}$  \\
 &  (0.176) & (0.296) & (0.025) & (0.043) & (0.022) & (0.038)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,656 & 1,656 & 1,656 & 1,656 & 1,656 & 1,656  \\
Adjusted $R^2$ &  0.032 & 0.036 & 0.023 & 0.027 & 0.018 & 0.023  \\
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
Treatment  &  0.463$^{+}$ & 0.438$^{+}$ & 0.065$^{+}$ & 0.064$^{+}$ & 0.048$^{*}$ & 0.050$^{*}$  \\
 &  (0.267) & (0.248) & (0.036) & (0.033) & (0.023) & (0.022)  \\
Constant  &  2.290$^{**}$ & 0.633$^{}$ & 0.375$^{***}$ & 0.098$^{}$ & 0.284$^{***}$ & 0.069$^{}$  \\
 &  (0.730) & (1.204) & (0.098) & (0.149) & (0.066) & (0.109)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,656 & 1,656 & 1,656 & 1,656 & 1,656 & 1,656  \\
Adjusted $R^2$ &  0.020 & 0.025 & 0.044 & 0.051 & 0.041 & 0.049  \\
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
Treatment  &  -0.158$^{}$ & -0.241$^{}$ & 0.004$^{}$ & -0.007$^{}$ & 0.002$^{}$ & -0.008$^{}$  \\
 &  (0.162) & (0.176) & (0.013) & (0.013) & (0.012) & (0.012)  \\
Constant  &  1.274$^{*}$ & -0.294$^{}$ & 0.067$^{}$ & -0.094$^{}$ & 0.062$^{+}$ & -0.092$^{}$  \\
 &  (0.587) & (0.498) & (0.044) & (0.069) & (0.035) & (0.059)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,656 & 1,656 & 1,656 & 1,656 & 1,656 & 1,656  \\
Adjusted $R^2$ &  0.001 & 0.004 & 0.006 & 0.019 & 0.006 & 0.020  \\
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
Treatment  &  0.269$^{}$ & 0.309$^{}$ & 0.016$^{}$ & -0.003$^{}$ & -0.008$^{}$ & -0.014$^{}$  \\
 &  (0.395) & (0.406) & (0.047) & (0.046) & (0.025) & (0.025)  \\
Constant  &  4.164$^{**}$ & 3.261$^{+}$ & 0.698$^{***}$ & 0.223$^{}$ & 0.501$^{***}$ & 0.257$^{*}$  \\
 &  (1.272) & (1.693) & (0.125) & (0.206) & (0.064) & (0.107)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,656 & 1,656 & 1,656 & 1,656 & 1,656 & 1,656  \\
Adjusted $R^2$ &  0.008 & 0.006 & 0.013 & 0.019 & 0.020 & 0.024  \\
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
Treatment  &  0.180$^{}$ & -0.572$^{}$ & -0.159$^{}$ & -0.219$^{}$ & 0.028$^{}$ & 0.014$^{}$  \\
 &  (1.198) & (1.161) & (0.171) & (0.170) & (0.052) & (0.055)  \\
Constant  &  5.747$^{*}$ & -1.719$^{}$ & 0.851$^{*}$ & -0.678$^{}$ & 0.146$^{}$ & -0.233$^{}$  \\
 &  (2.675) & (5.690) & (0.418) & (0.780) & (0.119) & (0.255)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  271 & 271 & 271 & 271 & 271 & 271  \\
Adjusted $R^2$ &  -0.025 & -0.017 & 0.109 & 0.108 & 0.097 & 0.095  \\
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
Treatment  &  0.421$^{}$ & 0.087$^{}$ & -0.036$^{}$ & -0.039$^{}$ & 0.065$^{}$ & 0.030$^{}$  \\
 &  (1.082) & (0.876) & (0.126) & (0.106) & (0.067) & (0.063)  \\
Constant  &  2.569$^{}$ & -7.917$^{*}$ & 0.386$^{}$ & -1.361$^{*}$ & 0.148$^{}$ & -0.776$^{*}$  \\
 &  (2.588) & (3.833) & (0.248) & (0.555) & (0.157) & (0.314)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  271 & 271 & 271 & 271 & 271 & 271  \\
Adjusted $R^2$ &  -0.031 & -0.003 & 0.053 & 0.092 & 0.064 & 0.111  \\
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
Treatment  &  -0.173$^{}$ & -0.613$^{}$ & -0.135$^{}$ & -0.200$^{}$ & -0.083$^{}$ & -0.102$^{}$  \\
 &  (1.016) & (1.040) & (0.123) & (0.138) & (0.062) & (0.062)  \\
Constant  &  2.343$^{}$ & 3.987$^{}$ & 0.433$^{}$ & 0.423$^{}$ & 0.147$^{}$ & 0.194$^{}$  \\
 &  (1.857) & (4.983) & (0.367) & (0.548) & (0.154) & (0.298)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  271 & 271 & 271 & 271 & 271 & 271  \\
Adjusted $R^2$ &  -0.019 & -0.021 & 0.053 & 0.073 & 0.035 & 0.049  \\
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
Treatment  &  1.153$^{}$ & 1.410$^{+}$ & 0.148$^{}$ & 0.138$^{}$ & 0.023$^{}$ & 0.012$^{}$  \\
 &  (0.711) & (0.827) & (0.097) & (0.109) & (0.032) & (0.031)  \\
Constant  &  5.745$^{***}$ & 3.912$^{}$ & 0.948$^{***}$ & 0.131$^{}$ & 0.524$^{***}$ & 0.193$^{}$  \\
 &  (1.291) & (4.517) & (0.149) & (0.591) & (0.058) & (0.180)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  811 & 811 & 811 & 811 & 811 & 811  \\
Adjusted $R^2$ &  0.004 & 0.001 & -0.000 & -0.001 & -0.006 & 0.002  \\
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
Treatment  &  0.269$^{}$ & 0.509$^{}$ & 0.066$^{}$ & 0.098$^{+}$ & 0.009$^{}$ & 0.015$^{}$  \\
 &  (0.373) & (0.414) & (0.051) & (0.055) & (0.030) & (0.026)  \\
Constant  &  0.459$^{}$ & 0.810$^{}$ & 0.182$^{*}$ & 0.355$^{}$ & 0.146$^{**}$ & 0.045$^{}$  \\
 &  (0.492) & (2.368) & (0.071) & (0.268) & (0.051) & (0.151)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  811 & 811 & 811 & 811 & 811 & 811  \\
Adjusted $R^2$ &  0.024 & 0.037 & 0.011 & 0.027 & 0.008 & 0.029  \\
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
Treatment  &  0.903$^{}$ & 0.905$^{}$ & 0.086$^{}$ & 0.040$^{}$ & 0.042$^{}$ & 0.030$^{}$  \\
 &  (0.637) & (0.696) & (0.078) & (0.077) & (0.033) & (0.035)  \\
Constant  &  5.210$^{***}$ & 2.949$^{}$ & 0.747$^{***}$ & -0.261$^{}$ & 0.459$^{***}$ & 0.233$^{}$  \\
 &  (1.249) & (3.426) & (0.133) & (0.469) & (0.065) & (0.197)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  811 & 811 & 811 & 811 & 811 & 811  \\
Adjusted $R^2$ &  -0.005 & -0.006 & -0.003 & 0.001 & -0.002 & -0.003  \\
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
Treatment  &  0.116$^{}$ & 0.096$^{}$ & 0.206$^{}$ & 0.171$^{}$ & -0.013$^{}$ & -0.009$^{}$  \\
 &  (1.279) & (1.219) & (0.140) & (0.138) & (0.061) & (0.056)  \\
Constant  &  14.461$^{***}$ & 10.541$^{}$ & 1.405$^{***}$ & 1.980$^{}$ & 0.540$^{***}$ & 0.898$^{}$  \\
 &  (2.251) & (13.635) & (0.160) & (1.460) & (0.061) & (0.591)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  350 & 350 & 350 & 350 & 350 & 350  \\
Adjusted $R^2$ &  -0.002 & -0.011 & -0.002 & 0.010 & 0.003 & 0.038  \\
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
Treatment  &  1.251$^{*}$ & 1.452$^{*}$ & 0.162$^{*}$ & 0.180$^{*}$ & 0.117$^{*}$ & 0.131$^{*}$  \\
 &  (0.625) & (0.637) & (0.068) & (0.070) & (0.050) & (0.053)  \\
Constant  &  0.605$^{}$ & 1.987$^{}$ & 0.067$^{}$ & 0.596$^{}$ & 0.042$^{}$ & 0.396$^{}$  \\
 &  (0.688) & (4.267) & (0.085) & (0.563) & (0.058) & (0.401)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  350 & 350 & 350 & 350 & 350 & 350  \\
Adjusted $R^2$ &  0.006 & 0.004 & 0.019 & 0.013 & 0.005 & 0.011  \\
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
Treatment  &  -1.135$^{}$ & -1.356$^{}$ & 0.043$^{}$ & -0.009$^{}$ & -0.052$^{}$ & -0.058$^{}$  \\
 &  (1.265) & (1.244) & (0.130) & (0.131) & (0.065) & (0.062)  \\
Constant  &  13.855$^{***}$ & 8.554$^{}$ & 1.338$^{***}$ & 1.384$^{}$ & 0.534$^{***}$ & 0.709$^{}$  \\
 &  (2.284) & (12.671) & (0.144) & (1.315) & (0.072) & (0.602)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  350 & 350 & 350 & 350 & 350 & 350  \\
Adjusted $R^2$ &  -0.005 & -0.013 & -0.013 & 0.017 & -0.000 & 0.009  \\
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
Treatment  &  2.285$^{+}$ & 2.696$^{}$ & 0.124$^{}$ & 0.081$^{}$ & 0.108$^{}$ & 0.126$^{}$  \\
 &  (1.377) & (1.765) & (0.153) & (0.212) & (0.095) & (0.094)  \\
Constant  &  8.029$^{***}$ & 11.102$^{}$ & 1.463$^{***}$ & 3.887$^{*}$ & 0.807$^{***}$ & 2.656$^{***}$  \\
 &  (1.496) & (13.797) & (0.274) & (1.535) & (0.178) & (0.725)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  142 & 142 & 142 & 142 & 142 & 142  \\
Adjusted $R^2$ &  0.078 & 0.107 & 0.121 & 0.105 & 0.104 & 0.115  \\
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
Treatment  &  0.332$^{}$ & -0.106$^{}$ & -0.041$^{}$ & -0.063$^{}$ & -0.015$^{}$ & -0.045$^{}$  \\
 &  (0.671) & (0.645) & (0.067) & (0.071) & (0.056) & (0.065)  \\
Constant  &  3.892$^{**}$ & 1.140$^{}$ & 0.629$^{**}$ & 1.695$^{+}$ & 0.487$^{**}$ & 1.112$^{}$  \\
 &  (1.485) & (9.061) & (0.226) & (0.975) & (0.158) & (0.745)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  142 & 142 & 142 & 142 & 142 & 142  \\
Adjusted $R^2$ &  -0.018 & -0.052 & 0.026 & 0.011 & 0.029 & 0.009  \\
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
Treatment  &  1.953$^{}$ & 2.802$^{}$ & 0.165$^{}$ & 0.144$^{}$ & 0.144$^{}$ & 0.168$^{+}$  \\
 &  (1.426) & (1.700) & (0.141) & (0.184) & (0.098) & (0.090)  \\
Constant  &  4.138$^{*}$ & 9.962$^{}$ & 0.834$^{***}$ & 2.192$^{+}$ & 0.628$^{**}$ & 2.314$^{**}$  \\
 &  (1.791) & (11.088) & (0.244) & (1.142) & (0.207) & (0.752)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  142 & 142 & 142 & 142 & 142 & 142  \\
Adjusted $R^2$ &  0.076 & 0.140 & 0.075 & 0.065 & 0.092 & 0.115  \\
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
Treatment  &  3.049$^{}$ & 2.487$^{}$ & 0.715$^{*}$ & 0.801$^{*}$ & 0.037$^{}$ & 0.059$^{}$  \\
 &  (1.991) & (1.943) & (0.344) & (0.383) & (0.111) & (0.124)  \\
Constant  &  14.737$^{*}$ & 3.579$^{}$ & 2.044$^{*}$ & 1.452$^{}$ & 0.722$^{**}$ & 0.505$^{}$  \\
 &  (5.904) & (10.105) & (0.930) & (2.809) & (0.267) & (0.542)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  82 & 82 & 82 & 82 & 82 & 82  \\
Adjusted $R^2$ &  0.006 & 0.011 & -0.006 & 0.105 & 0.016 & 0.028  \\
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
Treatment  &  3.048$^{**}$ & 2.128$^{*}$ & 0.643$^{*}$ & 0.503$^{*}$ & 0.291$^{**}$ & 0.293$^{**}$  \\
 &  (1.148) & (0.970) & (0.254) & (0.226) & (0.100) & (0.102)  \\
Constant  &  7.745$^{**}$ & 7.572$^{}$ & 0.744$^{**}$ & -0.257$^{}$ & 0.657$^{**}$ & 0.941$^{*}$  \\
 &  (2.544) & (6.243) & (0.244) & (2.544) & (0.197) & (0.470)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  82 & 82 & 82 & 82 & 82 & 82  \\
Adjusted $R^2$ &  0.073 & 0.103 & 0.052 & 0.114 & 0.070 & 0.137  \\
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
Treatment  &  0.001$^{}$ & 0.359$^{}$ & 0.072$^{}$ & 0.298$^{}$ & -0.050$^{}$ & 0.004$^{}$  \\
 &  (1.872) & (1.898) & (0.227) & (0.248) & (0.122) & (0.132)  \\
Constant  &  6.992$^{}$ & -3.994$^{}$ & 1.300$^{}$ & 1.709$^{}$ & 0.495$^{+}$ & 0.086$^{}$  \\
 &  (4.310) & (10.321) & (0.839) & (1.473) & (0.274) & (0.613)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  82 & 82 & 82 & 82 & 82 & 82  \\
Adjusted $R^2$ &  -0.072 & -0.088 & -0.027 & 0.036 & -0.018 & -0.005  \\
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
Treatment  &  1.178$^{+}$ & 1.077$^{}$ & 0.103$^{*}$ & 0.070$^{}$ & 0.045$^{+}$ & 0.031$^{}$  \\
 &  (0.705) & (0.702) & (0.047) & (0.045) & (0.025) & (0.025)  \\
Constant  &  5.830$^{*}$ & -3.089$^{}$ & 0.517$^{***}$ & -0.327$^{}$ & 0.352$^{***}$ & -0.057$^{}$  \\
 &  (2.451) & (3.149) & (0.145) & (0.218) & (0.070) & (0.111)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,448 & 1,448 & 1,448 & 1,448 & 1,448 & 1,448  \\
Adjusted $R^2$ &  0.018 & 0.027 & 0.026 & 0.042 & 0.032 & 0.042  \\
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
Treatment  &  0.406$^{}$ & 0.380$^{}$ & 0.048$^{*}$ & 0.045$^{*}$ & 0.037$^{*}$ & 0.036$^{*}$  \\
 &  (0.336) & (0.336) & (0.021) & (0.021) & (0.017) & (0.017)  \\
Constant  &  2.704$^{**}$ & -1.590$^{}$ & 0.207$^{***}$ & -0.058$^{}$ & 0.155$^{***}$ & -0.050$^{}$  \\
 &  (0.983) & (1.411) & (0.060) & (0.096) & (0.046) & (0.080)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,448 & 1,448 & 1,448 & 1,448 & 1,448 & 1,448  \\
Adjusted $R^2$ &  0.024 & 0.037 & 0.037 & 0.048 & 0.035 & 0.042  \\
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
Treatment  &  0.754$^{}$ & 0.665$^{}$ & 0.054$^{}$ & 0.023$^{}$ & 0.028$^{}$ & 0.012$^{}$  \\
 &  (0.648) & (0.672) & (0.040) & (0.039) & (0.025) & (0.026)  \\
Constant  &  2.983$^{}$ & -1.741$^{}$ & 0.297$^{*}$ & -0.291$^{}$ & 0.225$^{**}$ & -0.081$^{}$  \\
 &  (2.370) & (3.037) & (0.134) & (0.195) & (0.074) & (0.113)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,448 & 1,448 & 1,448 & 1,448 & 1,448 & 1,448  \\
Adjusted $R^2$ &  0.012 & 0.011 & 0.021 & 0.032 & 0.023 & 0.029  \\
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
Treatment  &  0.278$^{}$ & 0.222$^{}$ & -0.018$^{}$ & -0.015$^{}$ & -0.027$^{}$ & -0.026$^{}$  \\
 &  (0.769) & (0.786) & (0.058) & (0.058) & (0.027) & (0.027)  \\
Constant  &  9.229$^{***}$ & 8.760$^{**}$ & 1.113$^{***}$ & 0.978$^{***}$ & 0.603$^{***}$ & 0.490$^{***}$  \\
 &  (1.907) & (3.264) & (0.166) & (0.265) & (0.063) & (0.114)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,397 & 1,397 & 1,397 & 1,397 & 1,397 & 1,397  \\
Adjusted $R^2$ &  0.001 & 0.001 & 0.020 & 0.017 & 0.024 & 0.025  \\
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
Treatment  &  0.679$^{}$ & 0.670$^{}$ & 0.024$^{}$ & 0.027$^{}$ & 0.012$^{}$ & 0.015$^{}$  \\
 &  (0.465) & (0.444) & (0.037) & (0.036) & (0.023) & (0.022)  \\
Constant  &  2.412$^{*}$ & 1.408$^{}$ & 0.370$^{***}$ & 0.305$^{+}$ & 0.264$^{***}$ & 0.195$^{+}$  \\
 &  (1.074) & (1.775) & (0.099) & (0.158) & (0.064) & (0.107)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,397 & 1,397 & 1,397 & 1,397 & 1,397 & 1,397  \\
Adjusted $R^2$ &  0.010 & 0.010 & 0.031 & 0.034 & 0.024 & 0.025  \\
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
Treatment  &  -0.379$^{}$ & -0.433$^{}$ & -0.041$^{}$ & -0.042$^{}$ & -0.035$^{}$ & -0.035$^{}$  \\
 &  (0.647) & (0.675) & (0.042) & (0.042) & (0.026) & (0.027)  \\
Constant  &  6.599$^{***}$ & 7.135$^{*}$ & 0.725$^{***}$ & 0.652$^{**}$ & 0.482$^{***}$ & 0.384$^{***}$  \\
 &  (1.670) & (2.989) & (0.127) & (0.207) & (0.066) & (0.109)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,397 & 1,397 & 1,397 & 1,397 & 1,397 & 1,397  \\
Adjusted $R^2$ &  -0.005 & -0.005 & 0.009 & 0.010 & 0.019 & 0.021  \\
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
Treatment  &  0.616$^{}$ & 0.604$^{}$ & 0.091$^{}$ & 0.053$^{}$ & 0.011$^{}$ & 0.002$^{}$  \\
 &  (0.532) & (0.531) & (0.069) & (0.066) & (0.025) & (0.023)  \\
Constant  &  9.582$^{***}$ & 5.433$^{**}$ & 1.189$^{***}$ & 0.324$^{}$ & 0.573$^{***}$ & 0.255$^{*}$  \\
 &  (1.618) & (2.016) & (0.186) & (0.271) & (0.069) & (0.105)  \\
Dept Ranking (centered)  &  0.015$^{}$ & 0.028$^{*}$ & -0.003$^{*}$ & -0.001$^{}$ & -0.001$^{*}$ & -0.000$^{}$  \\
 &  (0.013) & (0.014) & (0.001) & (0.002) & (0.001) & (0.001)  \\
Treatment $\times$ Dept Ranking (centered)  &  0.006$^{}$ & 0.005$^{}$ & 0.004$^{+}$ & 0.004$^{*}$ & 0.001$^{}$ & 0.001$^{}$  \\
 &  (0.017) & (0.017) & (0.002) & (0.002) & (0.001) & (0.001)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,656 & 1,656 & 1,656 & 1,656 & 1,656 & 1,656  \\
Adjusted $R^2$ &  0.011 & 0.015 & 0.028 & 0.037 & 0.035 & 0.046  \\
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
Treatment  &  0.827$^{}$ & 0.620$^{}$ & 0.066$^{}$ & 0.056$^{}$ & 0.000$^{}$ & 0.003$^{}$  \\
 &  (0.554) & (0.532) & (0.072) & (0.067) & (0.025) & (0.024)  \\
Constant  &  8.523$^{***}$ & 3.029$^{}$ & 1.237$^{***}$ & 0.319$^{}$ & 0.615$^{***}$ & 0.263$^{*}$  \\
 &  (1.528) & (2.184) & (0.185) & (0.308) & (0.064) & (0.108)  \\
Total Faculty (centered)  &  -0.032$^{}$ & -0.026$^{}$ & 0.004$^{}$ & 0.002$^{}$ & 0.001$^{}$ & -0.000$^{}$  \\
 &  (0.027) & (0.026) & (0.003) & (0.003) & (0.001) & (0.001)  \\
Treatment $\times$ Total Faculty (centered)  &  0.019$^{}$ & 0.007$^{}$ & -0.001$^{}$ & -0.003$^{}$ & 0.001$^{}$ & 0.000$^{}$  \\
 &  (0.031) & (0.030) & (0.004) & (0.004) & (0.001) & (0.001)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,656 & 1,656 & 1,656 & 1,656 & 1,656 & 1,656  \\
Adjusted $R^2$ &  0.010 & 0.015 & 0.026 & 0.034 & 0.033 & 0.046  \\
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
Treatment  &  0.663$^{}$ & 0.582$^{}$ & 0.094$^{}$ & 0.058$^{}$ & 0.011$^{}$ & 0.002$^{}$  \\
 &  (0.533) & (0.534) & (0.068) & (0.066) & (0.024) & (0.023)  \\
Constant  &  8.350$^{***}$ & 7.498$^{***}$ & 1.205$^{***}$ & 0.861$^{***}$ & 0.615$^{***}$ & 0.476$^{***}$  \\
 &  (1.505) & (1.804) & (0.173) & (0.245) & (0.060) & (0.091)  \\
Peer URM Faculty (centered)  &  0.077$^{}$ & 0.145$^{*}$ & 0.017$^{**}$ & 0.020$^{**}$ & 0.007$^{**}$ & 0.007$^{**}$  \\
 &  (0.055) & (0.056) & (0.006) & (0.007) & (0.002) & (0.002)  \\
Treatment $\times$ Peer URM Faculty (centered)  &  -0.075$^{}$ & -0.064$^{}$ & -0.003$^{}$ & -0.004$^{}$ & -0.001$^{}$ & -0.001$^{}$  \\
 &  (0.075) & (0.075) & (0.008) & (0.008) & (0.003) & (0.003)  \\
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
Computer Science & Any Hispanic & Treatment & Extended & 0.1681 & 0.0900 & 1.868 & 0.0643 & + \\
Mathematics & \% URM & Treatment & Extended & 1.4100 & 0.8269 & 1.705 & 0.0886 & + \\
Mathematics & Count Black & Treatment & Extended & 0.0982 & 0.0553 & 1.776 & 0.0761 & + \\
Mechanical Engineering & \% Black & Treatment & Simple & 3.0477 & 1.1484 & 2.654 & 0.0100 & ** \\
Mechanical Engineering & Any Black & Treatment & Simple & 0.2906 & 0.1002 & 2.902 & 0.0051 & ** \\
Mechanical Engineering & Count Black & Treatment & Simple & 0.6433 & 0.2540 & 2.533 & 0.0137 & * \\
Mechanical Engineering & Count URM & Treatment & Extended & 0.8010 & 0.3832 & 2.090 & 0.0411 & * \\
Physics & \% Black & Treatment & Extended & 1.4520 & 0.6373 & 2.278 & 0.0234 & * \\
Physics & Any Black & Treatment & Extended & 0.1306 & 0.0529 & 2.469 & 0.0140 & * \\
Physics & Count Black & Treatment & Extended & 0.1801 & 0.0703 & 2.560 & 0.0109 & * \\
\addlinespace[0.5em]
\multicolumn{9}{l}{\textbf{Identity Analysis}} \\
\midrule
Demographic Subgroup & \% Black & Treatment & Extended & 0.5494 & 0.2927 & 1.877 & 0.0607 & + \\
Demographic Subgroup & \% Black Male & Treatment & Extended & 0.4380 & 0.2480 & 1.766 & 0.0776 & + \\
Demographic Subgroup & Any Black & Treatment & Extended & 0.0444 & 0.0227 & 1.957 & 0.0505 & + \\
Demographic Subgroup & Any Black Male & Treatment & Extended & 0.0498 & 0.0224 & 2.222 & 0.0264 & * \\
Demographic Subgroup & Count Black & Treatment & Extended & 0.0671 & 0.0389 & 1.726 & 0.0845 & + \\
Demographic Subgroup & Count Black Male & Treatment & Extended & 0.0635 & 0.0333 & 1.906 & 0.0569 & + \\
\addlinespace[0.5em]
\multicolumn{9}{l}{\textbf{Moderation Analysis}} \\
\midrule
Department Rank & Count URM & Treatment $\times$ Dept Ranking & Extended & 0.0043 & 0.0020 & 2.165 & 0.0305 & * \\
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
