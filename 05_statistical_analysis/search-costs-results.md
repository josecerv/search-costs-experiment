---
title: "Search Costs Field Experiment"
date: "2025-06-04"
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
URM & 8.00 & 11.50 & 1.09 & 1.36 & 56.5 \\
Black & 2.27 & 5.97 & 0.32 & 0.69 & 24.1 \\
Hispanic & 5.70 & 9.84 & 0.77 & 1.10 & 45.8 \\
Female & 16.92 & 16.18 & 2.40 & 2.49 & 76.1 \\
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
Chemistry & 271 & 9.38 & 10.58 & 1.34 & 66.1 \\
Computer Science & 142 & 4.86 & 9.01 & 0.61 & 38.0 \\
Mathematics & 811 & 7.58 & 11.22 & 1.02 & 52.3 \\
Mechanical Engineering & 82 & 8.44 & 9.16 & 1.15 & 63.4 \\
Physics & 350 & 9.06 & 13.73 & 1.26 & 64.6 \\
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
Chemistry & 4.33 & 40.6 & 4.94 & 48.0 & 23.44 & 86.3 \\
Computer Science & 1.46 & 16.9 & 3.40 & 27.5 & 19.21 & 79.6 \\
Mathematics & 1.74 & 19.7 & 5.82 & 44.4 & 14.00 & 70.5 \\
Mechanical Engineering & 3.34 & 32.9 & 5.10 & 46.3 & 19.30 & 75.6 \\
Physics & 1.98 & 22.3 & 7.08 & 54.9 & 17.16 & 79.7 \\
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
Fall (1448) & 7.57 & 0.58 & 39.0 & 1.77 & 12.2 & 5.78 & 31.4 \\
Spring (1397) & 8.14 & 0.70 & 43.7 & 2.71 & 18.6 & 5.40 & 32.4 \\
\midrule
 & \multicolumn{3}{c}{Female} & \multicolumn{2}{c}{Total Speakers} & & \\
Semester & Mean \% & Mean Count & Pct. Any & Mean & SD & & \\
\midrule
Fall & 16.10 & 1.27 & 61.9 & 7.75 & 5.50 & & \\
Spring & 17.77 & 1.52 & 64.3 & 8.56 & 6.92 & & \\
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
Treatment  &  0.551$^{}$ & 0.489$^{}$ & 0.083$^{}$ & 0.052$^{}$ & 0.006$^{}$ & 0.000$^{}$  \\
 &  (0.540) & (0.533) & (0.070) & (0.067) & (0.025) & (0.023)  \\
Constant  &  8.846$^{***}$ & 4.199$^{+}$ & 1.286$^{***}$ & 0.306$^{}$ & 0.643$^{***}$ & 0.286$^{**}$  \\
 &  (1.589) & (2.167) & (0.178) & (0.298) & (0.063) & (0.110)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,656 & 1,656 & 1,656 & 1,656 & 1,656 & 1,656  \\
Adjusted $R^2$ &  0.010 & 0.015 & 0.026 & 0.034 & 0.030 & 0.044  \\
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
Treatment  &  -0.461$^{}$ & -0.427$^{}$ & 0.083$^{}$ & 0.052$^{}$ & -0.544$^{}$ & -0.479$^{}$  \\
 &  (0.554) & (0.546) & (0.070) & (0.067) & (0.525) & (0.518)  \\
Constant  &  16.810$^{***}$ & 13.460$^{***}$ & 1.286$^{***}$ & 0.306$^{}$ & 15.524$^{***}$ & 13.154$^{***}$  \\
 &  (1.313) & (2.452) & (0.178) & (0.298) & (1.244) & (2.311)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,656 & 1,656 & 1,656 & 1,656 & 1,656 & 1,656  \\
Adjusted $R^2$ &  0.031 & 0.058 & 0.026 & 0.034 & 0.030 & 0.058  \\
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
URM Speakers & 0.0829 & (0.0670) \\
Non-URM Speakers & -0.5440 & (0.4589) \\
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
Treatment  &  0.553$^{+}$ & 0.541$^{+}$ & 0.067$^{}$ & 0.066$^{+}$ & 0.043$^{+}$ & 0.045$^{*}$  \\
 &  (0.311) & (0.291) & (0.041) & (0.038) & (0.023) & (0.023)  \\
Constant  &  2.859$^{***}$ & 0.763$^{}$ & 0.457$^{***}$ & 0.123$^{}$ & 0.292$^{***}$ & 0.079$^{}$  \\
 &  (0.825) & (1.347) & (0.112) & (0.174) & (0.066) & (0.110)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,656 & 1,656 & 1,656 & 1,656 & 1,656 & 1,656  \\
Adjusted $R^2$ &  0.029 & 0.034 & 0.049 & 0.058 & 0.042 & 0.050  \\
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
Treatment  &  0.013$^{}$ & -0.046$^{}$ & 0.016$^{}$ & -0.016$^{}$ & -0.011$^{}$ & -0.018$^{}$  \\
 &  (0.471) & (0.484) & (0.053) & (0.052) & (0.025) & (0.025)  \\
Constant  &  5.776$^{***}$ & 3.220$^{+}$ & 0.803$^{***}$ & 0.147$^{}$ & 0.512$^{***}$ & 0.257$^{*}$  \\
 &  (1.473) & (1.954) & (0.150) & (0.245) & (0.065) & (0.107)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,656 & 1,656 & 1,656 & 1,656 & 1,656 & 1,656  \\
Adjusted $R^2$ &  0.005 & 0.005 & 0.014 & 0.022 & 0.018 & 0.023  \\
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
Treatment  &  0.116$^{}$ & -0.402$^{}$ & -0.065$^{}$ & -0.131$^{}$ & -0.005$^{}$ & -0.011$^{}$  \\
 &  (0.833) & (0.824) & (0.129) & (0.128) & (0.022) & (0.021)  \\
Constant  &  21.582$^{***}$ & 13.460$^{***}$ & 3.630$^{***}$ & 2.248$^{***}$ & 0.859$^{***}$ & 0.670$^{***}$  \\
 &  (2.080) & (3.946) & (0.354) & (0.598) & (0.064) & (0.100)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,656 & 1,656 & 1,656 & 1,656 & 1,656 & 1,656  \\
Adjusted $R^2$ &  0.049 & 0.057 & 0.086 & 0.102 & 0.018 & 0.030  \\
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
Treatment  &  -0.058$^{}$ & -0.124$^{}$ & 0.024$^{}$ & 0.014$^{}$ & 0.016$^{}$ & 0.007$^{}$  \\
 &  (0.175) & (0.185) & (0.020) & (0.020) & (0.018) & (0.018)  \\
Constant  &  1.910$^{**}$ & -0.032$^{}$ & 0.214$^{***}$ & -0.046$^{}$ & 0.182$^{***}$ & -0.057$^{}$  \\
 &  (0.611) & (0.599) & (0.063) & (0.093) & (0.052) & (0.081)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,656 & 1,656 & 1,656 & 1,656 & 1,656 & 1,656  \\
Adjusted $R^2$ &  0.015 & 0.021 & 0.044 & 0.059 & 0.046 & 0.060  \\
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
Treatment  &  0.096$^{}$ & 0.109$^{}$ & 0.006$^{}$ & 0.006$^{}$ & 0.006$^{}$ & 0.007$^{}$  \\
 &  (0.073) & (0.074) & (0.010) & (0.010) & (0.009) & (0.009)  \\
Constant  &  0.589$^{***}$ & 0.169$^{}$ & 0.080$^{**}$ & 0.025$^{}$ & 0.066$^{**}$ & 0.026$^{}$  \\
 &  (0.176) & (0.285) & (0.025) & (0.043) & (0.022) & (0.037)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,656 & 1,656 & 1,656 & 1,656 & 1,656 & 1,656  \\
Adjusted $R^2$ &  0.033 & 0.038 & 0.021 & 0.026 & 0.018 & 0.022  \\
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
Treatment  &  0.457$^{+}$ & 0.432$^{+}$ & 0.062$^{+}$ & 0.061$^{+}$ & 0.049$^{*}$ & 0.051$^{*}$  \\
 &  (0.264) & (0.246) & (0.034) & (0.032) & (0.023) & (0.022)  \\
Constant  &  2.270$^{**}$ & 0.594$^{}$ & 0.371$^{***}$ & 0.094$^{}$ & 0.281$^{***}$ & 0.061$^{}$  \\
 &  (0.725) & (1.202) & (0.097) & (0.147) & (0.065) & (0.108)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,656 & 1,656 & 1,656 & 1,656 & 1,656 & 1,656  \\
Adjusted $R^2$ &  0.020 & 0.024 & 0.045 & 0.052 & 0.041 & 0.049  \\
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
Treatment  &  -0.158$^{}$ & -0.240$^{}$ & 0.010$^{}$ & -0.002$^{}$ & 0.005$^{}$ & -0.005$^{}$  \\
 &  (0.162) & (0.176) & (0.014) & (0.013) & (0.012) & (0.012)  \\
Constant  &  1.297$^{*}$ & -0.245$^{}$ & 0.066$^{}$ & -0.092$^{}$ & 0.058$^{}$ & -0.094$^{}$  \\
 &  (0.586) & (0.501) & (0.045) & (0.068) & (0.036) & (0.060)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,656 & 1,656 & 1,656 & 1,656 & 1,656 & 1,656  \\
Adjusted $R^2$ &  0.002 & 0.005 & 0.008 & 0.020 & 0.007 & 0.019  \\
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
Treatment  &  0.171$^{}$ & 0.194$^{}$ & 0.005$^{}$ & -0.014$^{}$ & -0.011$^{}$ & -0.017$^{}$  \\
 &  (0.401) & (0.411) & (0.047) & (0.046) & (0.025) & (0.025)  \\
Constant  &  4.479$^{***}$ & 3.465$^{*}$ & 0.736$^{***}$ & 0.249$^{}$ & 0.508$^{***}$ & 0.275$^{*}$  \\
 &  (1.296) & (1.719) & (0.130) & (0.212) & (0.064) & (0.107)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,656 & 1,656 & 1,656 & 1,656 & 1,656 & 1,656  \\
Adjusted $R^2$ &  0.008 & 0.007 & 0.014 & 0.021 & 0.019 & 0.023  \\
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
Treatment  &  0.201$^{}$ & -0.525$^{}$ & -0.155$^{}$ & -0.209$^{}$ & 0.028$^{}$ & 0.014$^{}$  \\
 &  (1.202) & (1.172) & (0.173) & (0.172) & (0.052) & (0.055)  \\
Constant  &  5.780$^{*}$ & -1.909$^{}$ & 0.863$^{*}$ & -0.725$^{}$ & 0.146$^{}$ & -0.233$^{}$  \\
 &  (2.678) & (5.712) & (0.421) & (0.783) & (0.119) & (0.255)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  271 & 271 & 271 & 271 & 271 & 271  \\
Adjusted $R^2$ &  -0.025 & -0.017 & 0.109 & 0.110 & 0.097 & 0.095  \\
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
Treatment  &  0.408$^{}$ & 0.070$^{}$ & -0.036$^{}$ & -0.039$^{}$ & 0.065$^{}$ & 0.030$^{}$  \\
 &  (1.081) & (0.874) & (0.126) & (0.106) & (0.067) & (0.063)  \\
Constant  &  2.574$^{}$ & -7.905$^{*}$ & 0.386$^{}$ & -1.361$^{*}$ & 0.148$^{}$ & -0.776$^{*}$  \\
 &  (2.585) & (3.829) & (0.248) & (0.555) & (0.157) & (0.314)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  271 & 271 & 271 & 271 & 271 & 271  \\
Adjusted $R^2$ &  -0.031 & -0.004 & 0.053 & 0.092 & 0.064 & 0.111  \\
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
Treatment  &  -0.140$^{}$ & -0.549$^{}$ & -0.131$^{}$ & -0.189$^{}$ & -0.083$^{}$ & -0.102$^{}$  \\
 &  (1.027) & (1.059) & (0.127) & (0.142) & (0.062) & (0.062)  \\
Constant  &  2.371$^{}$ & 3.785$^{}$ & 0.445$^{}$ & 0.376$^{}$ & 0.147$^{}$ & 0.194$^{}$  \\
 &  (1.865) & (5.014) & (0.370) & (0.554) & (0.154) & (0.298)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  271 & 271 & 271 & 271 & 271 & 271  \\
Adjusted $R^2$ &  -0.019 & -0.020 & 0.053 & 0.073 & 0.035 & 0.049  \\
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
Treatment  &  0.990$^{}$ & 1.204$^{}$ & 0.153$^{}$ & 0.140$^{}$ & 0.019$^{}$ & 0.007$^{}$  \\
 &  (0.724) & (0.832) & (0.099) & (0.111) & (0.031) & (0.031)  \\
Constant  &  6.446$^{***}$ & 5.107$^{}$ & 0.996$^{***}$ & 0.258$^{}$ & 0.546$^{***}$ & 0.284$^{}$  \\
 &  (1.399) & (4.528) & (0.153) & (0.611) & (0.057) & (0.177)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  811 & 811 & 811 & 811 & 811 & 811  \\
Adjusted $R^2$ &  0.002 & -0.001 & -0.001 & -0.003 & -0.008 & 0.000  \\
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
Treatment  &  0.277$^{}$ & 0.514$^{}$ & 0.071$^{}$ & 0.103$^{+}$ & 0.011$^{}$ & 0.017$^{}$  \\
 &  (0.372) & (0.412) & (0.051) & (0.055) & (0.030) & (0.026)  \\
Constant  &  0.440$^{}$ & 0.772$^{}$ & 0.176$^{*}$ & 0.333$^{}$ & 0.142$^{**}$ & 0.029$^{}$  \\
 &  (0.489) & (2.356) & (0.071) & (0.266) & (0.050) & (0.149)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  811 & 811 & 811 & 811 & 811 & 811  \\
Adjusted $R^2$ &  0.025 & 0.039 & 0.012 & 0.028 & 0.011 & 0.032  \\
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
Treatment  &  0.731$^{}$ & 0.694$^{}$ & 0.086$^{}$ & 0.039$^{}$ & 0.038$^{}$ & 0.026$^{}$  \\
 &  (0.654) & (0.706) & (0.079) & (0.079) & (0.033) & (0.035)  \\
Constant  &  5.931$^{***}$ & 4.182$^{}$ & 0.802$^{***}$ & -0.112$^{}$ & 0.481$^{***}$ & 0.324$^{+}$  \\
 &  (1.376) & (3.457) & (0.139) & (0.496) & (0.065) & (0.195)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  811 & 811 & 811 & 811 & 811 & 811  \\
Adjusted $R^2$ &  -0.006 & -0.005 & -0.003 & 0.000 & -0.004 & -0.004  \\
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
Treatment  &  -0.103$^{}$ & -0.114$^{}$ & 0.164$^{}$ & 0.128$^{}$ & -0.020$^{}$ & -0.015$^{}$  \\
 &  (1.281) & (1.227) & (0.142) & (0.142) & (0.062) & (0.056)  \\
Constant  &  14.377$^{***}$ & 10.257$^{}$ & 1.394$^{***}$ & 1.843$^{}$ & 0.534$^{***}$ & 0.919$^{}$  \\
 &  (2.280) & (13.749) & (0.169) & (1.488) & (0.063) & (0.592)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  350 & 350 & 350 & 350 & 350 & 350  \\
Adjusted $R^2$ &  -0.002 & -0.011 & -0.006 & 0.005 & 0.002 & 0.037  \\
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
Treatment  &  1.234$^{*}$ & 1.433$^{*}$ & 0.158$^{*}$ & 0.175$^{*}$ & 0.117$^{*}$ & 0.131$^{*}$  \\
 &  (0.623) & (0.634) & (0.067) & (0.069) & (0.050) & (0.053)  \\
Constant  &  0.637$^{}$ & 1.899$^{}$ & 0.072$^{}$ & 0.568$^{}$ & 0.042$^{}$ & 0.396$^{}$  \\
 &  (0.680) & (4.277) & (0.085) & (0.566) & (0.058) & (0.401)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  350 & 350 & 350 & 350 & 350 & 350  \\
Adjusted $R^2$ &  0.005 & 0.004 & 0.014 & 0.009 & 0.005 & 0.011  \\
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
Treatment  &  -1.337$^{}$ & -1.547$^{}$ & 0.006$^{}$ & -0.048$^{}$ & -0.058$^{}$ & -0.064$^{}$  \\
 &  (1.266) & (1.251) & (0.132) & (0.134) & (0.065) & (0.062)  \\
Constant  &  13.741$^{***}$ & 8.358$^{}$ & 1.321$^{***}$ & 1.275$^{}$ & 0.528$^{***}$ & 0.730$^{}$  \\
 &  (2.312) & (12.784) & (0.149) & (1.340) & (0.077) & (0.602)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  350 & 350 & 350 & 350 & 350 & 350  \\
Adjusted $R^2$ &  -0.004 & -0.013 & -0.015 & 0.012 & -0.001 & 0.007  \\
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
Treatment  &  2.294$^{+}$ & 2.702$^{}$ & 0.124$^{}$ & 0.081$^{}$ & 0.108$^{}$ & 0.126$^{}$  \\
 &  (1.377) & (1.764) & (0.153) & (0.212) & (0.095) & (0.094)  \\
Constant  &  8.046$^{***}$ & 11.043$^{}$ & 1.463$^{***}$ & 3.887$^{*}$ & 0.807$^{***}$ & 2.656$^{***}$  \\
 &  (1.495) & (13.793) & (0.274) & (1.535) & (0.178) & (0.725)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  142 & 142 & 142 & 142 & 142 & 142  \\
Adjusted $R^2$ &  0.078 & 0.108 & 0.121 & 0.105 & 0.104 & 0.115  \\
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
Treatment  &  1.962$^{}$ & 2.808$^{}$ & 0.165$^{}$ & 0.144$^{}$ & 0.144$^{}$ & 0.168$^{+}$  \\
 &  (1.426) & (1.699) & (0.141) & (0.184) & (0.098) & (0.090)  \\
Constant  &  4.154$^{*}$ & 9.903$^{}$ & 0.834$^{***}$ & 2.192$^{+}$ & 0.628$^{**}$ & 2.314$^{**}$  \\
 &  (1.790) & (11.083) & (0.244) & (1.142) & (0.207) & (0.752)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  142 & 142 & 142 & 142 & 142 & 142  \\
Adjusted $R^2$ &  0.077 & 0.141 & 0.075 & 0.065 & 0.092 & 0.115  \\
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
Treatment  &  2.911$^{}$ & 2.506$^{}$ & 0.657$^{*}$ & 0.809$^{*}$ & 0.037$^{}$ & 0.059$^{}$  \\
 &  (1.980) & (1.934) & (0.315) & (0.375) & (0.111) & (0.124)  \\
Constant  &  14.817$^{*}$ & 5.334$^{}$ & 2.077$^{*}$ & 2.189$^{}$ & 0.722$^{**}$ & 0.505$^{}$  \\
 &  (5.933) & (10.184) & (0.927) & (2.385) & (0.267) & (0.542)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  82 & 82 & 82 & 82 & 82 & 82  \\
Adjusted $R^2$ &  0.005 & -0.001 & -0.009 & 0.105 & 0.016 & 0.028  \\
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
Treatment  &  2.910$^{*}$ & 2.147$^{*}$ & 0.585$^{**}$ & 0.511$^{*}$ & 0.291$^{**}$ & 0.293$^{**}$  \\
 &  (1.106) & (0.940) & (0.206) & (0.207) & (0.100) & (0.102)  \\
Constant  &  7.825$^{**}$ & 9.327$^{+}$ & 0.777$^{**}$ & 0.480$^{}$ & 0.657$^{**}$ & 0.941$^{*}$  \\
 &  (2.564) & (5.491) & (0.229) & (1.987) & (0.197) & (0.470)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  82 & 82 & 82 & 82 & 82 & 82  \\
Adjusted $R^2$ &  0.070 & 0.095 & 0.067 & 0.121 & 0.070 & 0.137  \\
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
Treatment  &  1.016$^{}$ & 0.908$^{}$ & 0.094$^{*}$ & 0.063$^{}$ & 0.038$^{}$ & 0.025$^{}$  \\
 &  (0.703) & (0.699) & (0.047) & (0.046) & (0.025) & (0.026)  \\
Constant  &  6.031$^{*}$ & -2.836$^{}$ & 0.525$^{***}$ & -0.301$^{}$ & 0.368$^{***}$ & -0.034$^{}$  \\
 &  (2.452) & (3.146) & (0.146) & (0.219) & (0.071) & (0.112)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,448 & 1,448 & 1,448 & 1,448 & 1,448 & 1,448  \\
Adjusted $R^2$ &  0.018 & 0.026 & 0.026 & 0.041 & 0.031 & 0.040  \\
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
Treatment  &  0.407$^{}$ & 0.379$^{}$ & 0.048$^{*}$ & 0.045$^{*}$ & 0.035$^{*}$ & 0.034$^{+}$  \\
 &  (0.335) & (0.335) & (0.021) & (0.021) & (0.017) & (0.018)  \\
Constant  &  2.661$^{**}$ & -1.611$^{}$ & 0.207$^{***}$ & -0.058$^{}$ & 0.162$^{***}$ & -0.043$^{}$  \\
 &  (0.978) & (1.408) & (0.060) & (0.095) & (0.047) & (0.081)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,448 & 1,448 & 1,448 & 1,448 & 1,448 & 1,448  \\
Adjusted $R^2$ &  0.024 & 0.037 & 0.038 & 0.048 & 0.033 & 0.041  \\
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
Treatment  &  0.592$^{}$ & 0.497$^{}$ & 0.045$^{}$ & 0.015$^{}$ & 0.023$^{}$ & 0.008$^{}$  \\
 &  (0.649) & (0.672) & (0.041) & (0.040) & (0.025) & (0.026)  \\
Constant  &  3.227$^{}$ & -1.469$^{}$ & 0.306$^{*}$ & -0.266$^{}$ & 0.234$^{**}$ & -0.065$^{}$  \\
 &  (2.372) & (3.050) & (0.134) & (0.197) & (0.074) & (0.113)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,448 & 1,448 & 1,448 & 1,448 & 1,448 & 1,448  \\
Adjusted $R^2$ &  0.012 & 0.011 & 0.021 & 0.031 & 0.023 & 0.028  \\
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
Treatment  &  0.310$^{}$ & 0.238$^{}$ & -0.018$^{}$ & -0.017$^{}$ & -0.026$^{}$ & -0.026$^{}$  \\
 &  (0.769) & (0.783) & (0.058) & (0.058) & (0.027) & (0.027)  \\
Constant  &  9.432$^{***}$ & 8.842$^{**}$ & 1.148$^{***}$ & 0.985$^{***}$ & 0.611$^{***}$ & 0.488$^{***}$  \\
 &  (1.939) & (3.301) & (0.166) & (0.268) & (0.064) & (0.113)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,397 & 1,397 & 1,397 & 1,397 & 1,397 & 1,397  \\
Adjusted $R^2$ &  0.001 & 0.001 & 0.020 & 0.017 & 0.026 & 0.028  \\
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
Treatment  &  0.663$^{}$ & 0.655$^{}$ & 0.021$^{}$ & 0.025$^{}$ & 0.014$^{}$ & 0.017$^{}$  \\
 &  (0.462) & (0.439) & (0.036) & (0.035) & (0.023) & (0.022)  \\
Constant  &  2.382$^{*}$ & 1.354$^{}$ & 0.369$^{***}$ & 0.302$^{+}$ & 0.257$^{***}$ & 0.184$^{+}$  \\
 &  (1.067) & (1.768) & (0.097) & (0.156) & (0.064) & (0.106)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,397 & 1,397 & 1,397 & 1,397 & 1,397 & 1,397  \\
Adjusted $R^2$ &  0.010 & 0.010 & 0.031 & 0.034 & 0.023 & 0.024  \\
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
Treatment  &  -0.332$^{}$ & -0.401$^{}$ & -0.038$^{}$ & -0.041$^{}$ & -0.034$^{}$ & -0.035$^{}$  \\
 &  (0.649) & (0.675) & (0.043) & (0.043) & (0.026) & (0.026)  \\
Constant  &  6.832$^{***}$ & 7.270$^{*}$ & 0.762$^{***}$ & 0.661$^{**}$ & 0.490$^{***}$ & 0.382$^{***}$  \\
 &  (1.719) & (3.036) & (0.131) & (0.213) & (0.067) & (0.109)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,397 & 1,397 & 1,397 & 1,397 & 1,397 & 1,397  \\
Adjusted $R^2$ &  -0.005 & -0.004 & 0.010 & 0.012 & 0.021 & 0.023  \\
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
Treatment  &  0.506$^{}$ & 0.480$^{}$ & 0.084$^{}$ & 0.045$^{}$ & 0.009$^{}$ & -0.001$^{}$  \\
 &  (0.531) & (0.529) & (0.069) & (0.067) & (0.024) & (0.023)  \\
Constant  &  10.010$^{***}$ & 5.767$^{**}$ & 1.218$^{***}$ & 0.344$^{}$ & 0.578$^{***}$ & 0.267$^{*}$  \\
 &  (1.619) & (2.032) & (0.188) & (0.274) & (0.069) & (0.104)  \\
Dept Ranking (centered)  &  0.016$^{}$ & 0.029$^{*}$ & -0.003$^{*}$ & -0.001$^{}$ & -0.001$^{**}$ & -0.001$^{}$  \\
 &  (0.013) & (0.013) & (0.001) & (0.002) & (0.001) & (0.001)  \\
Treatment $\times$ Dept Ranking (centered)  &  0.006$^{}$ & 0.006$^{}$ & 0.004$^{*}$ & 0.005$^{*}$ & 0.001$^{}$ & 0.001$^{}$  \\
 &  (0.017) & (0.017) & (0.002) & (0.002) & (0.001) & (0.001)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,656 & 1,656 & 1,656 & 1,656 & 1,656 & 1,656  \\
Adjusted $R^2$ &  0.011 & 0.014 & 0.029 & 0.038 & 0.034 & 0.045  \\
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
Treatment  &  0.713$^{}$ & 0.495$^{}$ & 0.057$^{}$ & 0.048$^{}$ & -0.003$^{}$ & 0.000$^{}$  \\
 &  (0.555) & (0.530) & (0.072) & (0.067) & (0.025) & (0.023)  \\
Constant  &  8.860$^{***}$ & 3.392$^{}$ & 1.271$^{***}$ & 0.357$^{}$ & 0.625$^{***}$ & 0.283$^{**}$  \\
 &  (1.546) & (2.203) & (0.187) & (0.314) & (0.064) & (0.108)  \\
Total Faculty (centered)  &  -0.030$^{}$ & -0.022$^{}$ & 0.004$^{}$ & 0.003$^{}$ & 0.001$^{}$ & -0.000$^{}$  \\
 &  (0.026) & (0.025) & (0.003) & (0.003) & (0.001) & (0.001)  \\
Treatment $\times$ Total Faculty (centered)  &  0.017$^{}$ & 0.005$^{}$ & -0.002$^{}$ & -0.003$^{}$ & 0.000$^{}$ & 0.000$^{}$  \\
 &  (0.030) & (0.030) & (0.004) & (0.004) & (0.001) & (0.001)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,656 & 1,656 & 1,656 & 1,656 & 1,656 & 1,656  \\
Adjusted $R^2$ &  0.009 & 0.014 & 0.027 & 0.034 & 0.031 & 0.044  \\
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
Treatment  &  0.555$^{}$ & 0.457$^{}$ & 0.088$^{}$ & 0.050$^{}$ & 0.008$^{}$ & -0.000$^{}$  \\
 &  (0.534) & (0.533) & (0.068) & (0.067) & (0.024) & (0.023)  \\
Constant  &  8.679$^{***}$ & 7.735$^{***}$ & 1.238$^{***}$ & 0.881$^{***}$ & 0.622$^{***}$ & 0.485$^{***}$  \\
 &  (1.518) & (1.806) & (0.174) & (0.248) & (0.060) & (0.092)  \\
Peer URM Faculty (centered)  &  0.076$^{}$ & 0.148$^{**}$ & 0.018$^{**}$ & 0.021$^{**}$ & 0.007$^{**}$ & 0.007$^{**}$  \\
 &  (0.054) & (0.056) & (0.006) & (0.007) & (0.002) & (0.002)  \\
Treatment $\times$ Peer URM Faculty (centered)  &  -0.078$^{}$ & -0.069$^{}$ & -0.004$^{}$ & -0.005$^{}$ & -0.001$^{}$ & -0.002$^{}$  \\
 &  (0.075) & (0.074) & (0.008) & (0.008) & (0.003) & (0.003)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,656 & 1,656 & 1,656 & 1,656 & 1,656 & 1,656  \\
Adjusted $R^2$ &  0.010 & 0.015 & 0.032 & 0.034 & 0.039 & 0.044  \\
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
Computer Science & \% URM & Treatment & Simple & 2.2940 & 1.3771 & 1.666 & 0.0983 & + \\
Computer Science & Any Hispanic & Treatment & Extended & 0.1681 & 0.0900 & 1.868 & 0.0643 & + \\
Mathematics & Count Black & Treatment & Extended & 0.1025 & 0.0554 & 1.851 & 0.0646 & + \\
Mechanical Engineering & \% Black & Treatment & Simple & 2.9095 & 1.1062 & 2.630 & 0.0106 & * \\
Mechanical Engineering & Any Black & Treatment & Simple & 0.2906 & 0.1002 & 2.902 & 0.0051 & ** \\
Mechanical Engineering & Count Black & Treatment & Simple & 0.5852 & 0.2060 & 2.841 & 0.0060 & ** \\
Mechanical Engineering & Count URM & Treatment & Extended & 0.8090 & 0.3750 & 2.157 & 0.0352 & * \\
Physics & \% Black & Treatment & Extended & 1.4331 & 0.6338 & 2.261 & 0.0244 & * \\
Physics & Any Black & Treatment & Extended & 0.1306 & 0.0529 & 2.469 & 0.0140 & * \\
Physics & Count Black & Treatment & Extended & 0.1753 & 0.0691 & 2.538 & 0.0116 & * \\
\addlinespace[0.5em]
\multicolumn{9}{l}{\textbf{Identity Analysis}} \\
\midrule
Demographic Subgroup & \% Black & Treatment & Extended & 0.5413 & 0.2910 & 1.860 & 0.0631 & + \\
Demographic Subgroup & \% Black Male & Treatment & Extended & 0.4320 & 0.2461 & 1.755 & 0.0794 & + \\
Demographic Subgroup & Any Black & Treatment & Extended & 0.0453 & 0.0227 & 1.993 & 0.0464 & * \\
Demographic Subgroup & Any Black Male & Treatment & Extended & 0.0507 & 0.0224 & 2.258 & 0.0241 & * \\
Demographic Subgroup & Count Black & Treatment & Extended & 0.0657 & 0.0381 & 1.723 & 0.0850 & + \\
Demographic Subgroup & Count Black Male & Treatment & Extended & 0.0613 & 0.0324 & 1.889 & 0.0590 & + \\
\addlinespace[0.5em]
\multicolumn{9}{l}{\textbf{Moderation Analysis}} \\
\midrule
Department Rank & Count URM & Treatment $\times$ Dept Ranking & Extended & 0.0046 & 0.0019 & 2.394 & 0.0168 & * \\
\addlinespace[0.5em]
\multicolumn{9}{l}{\textbf{Semester Analysis}} \\
\midrule
Fall Semester & Any Black & Treatment & Simple & 0.0352 & 0.0172 & 2.051 & 0.0405 & * \\
Fall Semester & Count Black & Treatment & Simple & 0.0479 & 0.0213 & 2.252 & 0.0245 & * \\
Fall Semester & Count URM & Treatment & Simple & 0.0943 & 0.0472 & 1.998 & 0.0459 & * \\
\bottomrule
\end{tabular}
} % End group for scriptsize and tabcolsep
\parbox{\linewidth}{\footnotesize Note: Significance levels: + p<0.1; * p<0.05; ** p<0.01; *** p<0.001. SE = Clustered standard errors at department level. Constant terms are excluded from this summary.}
\end{table}
