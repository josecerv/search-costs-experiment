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
Total faculty per department & 31.5 & 18.6 \\
\% URM faculty & 3.93 & 4.44 \\
\% Women faculty & 19.29 & 8.71 \\
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
Chemistry & 123 & 27.3 & 13.0 & 4.66 & 4.53 & 23.43 & 8.45 \\
Computer Science & 82 & 39.7 & 26.0 & 2.74 & 3.29 & 18.94 & 8.72 \\
Mathematics & 134 & 30.7 & 16.1 & 3.46 & 3.60 & 18.57 & 8.65 \\
Mechanical Engineering & 66 & 32.9 & 20.8 & 5.27 & 5.58 & 18.28 & 9.04 \\
Physics & 125 & 30.3 & 17.1 & 3.81 & 4.88 & 16.73 & 7.47 \\
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
Treatment  &  0.658$^{}$ & 0.668$^{}$ & 0.090$^{}$ & 0.078$^{}$ & 0.009$^{}$ & 0.007$^{}$  \\
 &  (0.539) & (0.524) & (0.070) & (0.067) & (0.025) & (0.023)  \\
Constant  &  8.523$^{***}$ & 4.550$^{*}$ & 1.251$^{***}$ & 0.403$^{}$ & 0.635$^{***}$ & 0.301$^{**}$  \\
 &  (1.580) & (2.056) & (0.176) & (0.279) & (0.063) & (0.104)  \\
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
Treatment  &  -0.461$^{}$ & -0.463$^{}$ & 0.090$^{}$ & 0.078$^{}$ & -0.542$^{}$ & -0.531$^{}$  \\
 &  (0.554) & (0.541) & (0.070) & (0.067) & (0.524) & (0.513)  \\
Constant  &  16.810$^{***}$ & 13.124$^{***}$ & 1.251$^{***}$ & 0.403$^{}$ & 15.529$^{***}$ & 12.679$^{***}$  \\
 &  (1.313) & (2.321) & (0.176) & (0.279) & (1.234) & (2.171)  \\
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
Treatment  &  0.561$^{+}$ & 0.480$^{}$ & 0.068$^{}$ & 0.054$^{}$ & 0.042$^{+}$ & 0.037$^{}$  \\
 &  (0.313) & (0.304) & (0.042) & (0.040) & (0.023) & (0.023)  \\
Constant  &  2.874$^{***}$ & 0.376$^{}$ & 0.459$^{***}$ & 0.057$^{}$ & 0.295$^{***}$ & 0.048$^{}$  \\
 &  (0.830) & (1.337) & (0.113) & (0.165) & (0.066) & (0.106)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,656 & 1,656 & 1,656 & 1,656 & 1,656 & 1,656  \\
Adjusted $R^2$ &  0.028 & 0.035 & 0.048 & 0.058 & 0.042 & 0.050  \\
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
Treatment  &  0.111$^{}$ & 0.204$^{}$ & 0.021$^{}$ & 0.023$^{}$ & -0.008$^{}$ & -0.006$^{}$  \\
 &  (0.468) & (0.462) & (0.052) & (0.052) & (0.025) & (0.025)  \\
Constant  &  5.437$^{***}$ & 4.028$^{*}$ & 0.766$^{***}$ & 0.323$^{}$ & 0.504$^{***}$ & 0.305$^{**}$  \\
 &  (1.458) & (1.812) & (0.146) & (0.221) & (0.065) & (0.104)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,656 & 1,656 & 1,656 & 1,656 & 1,656 & 1,656  \\
Adjusted $R^2$ &  0.005 & 0.005 & 0.013 & 0.018 & 0.019 & 0.023  \\
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
Treatment  &  0.087$^{}$ & -0.100$^{}$ & -0.061$^{}$ & -0.116$^{}$ & -0.007$^{}$ & -0.005$^{}$  \\
 &  (0.823) & (0.826) & (0.129) & (0.127) & (0.021) & (0.021)  \\
Constant  &  22.166$^{***}$ & 16.880$^{***}$ & 3.631$^{***}$ & 2.433$^{***}$ & 0.884$^{***}$ & 0.731$^{***}$  \\
 &  (2.010) & (3.617) & (0.342) & (0.594) & (0.061) & (0.093)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,656 & 1,656 & 1,656 & 1,656 & 1,656 & 1,656  \\
Adjusted $R^2$ &  0.050 & 0.055 & 0.087 & 0.103 & 0.017 & 0.028  \\
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
Treatment  &  -0.056$^{}$ & -0.025$^{}$ & 0.017$^{}$ & 0.008$^{}$ & 0.011$^{}$ & 0.004$^{}$  \\
 &  (0.174) & (0.143) & (0.019) & (0.019) & (0.017) & (0.017)  \\
Constant  &  1.883$^{**}$ & 0.475$^{}$ & 0.220$^{***}$ & -0.022$^{}$ & 0.190$^{***}$ & -0.031$^{}$  \\
 &  (0.611) & (0.736) & (0.062) & (0.089) & (0.052) & (0.076)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,656 & 1,656 & 1,656 & 1,656 & 1,656 & 1,656  \\
Adjusted $R^2$ &  0.015 & 0.022 & 0.043 & 0.058 & 0.046 & 0.060  \\
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
Treatment  &  0.098$^{}$ & 0.091$^{}$ & 0.003$^{}$ & -0.000$^{}$ & 0.005$^{}$ & 0.002$^{}$  \\
 &  (0.073) & (0.074) & (0.010) & (0.009) & (0.009) & (0.009)  \\
Constant  &  0.584$^{***}$ & 0.029$^{}$ & 0.079$^{**}$ & 0.004$^{}$ & 0.066$^{**}$ & 0.002$^{}$  \\
 &  (0.176) & (0.288) & (0.025) & (0.042) & (0.022) & (0.036)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,656 & 1,656 & 1,656 & 1,656 & 1,656 & 1,656  \\
Adjusted $R^2$ &  0.032 & 0.036 & 0.023 & 0.028 & 0.018 & 0.024  \\
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
Treatment  &  0.463$^{+}$ & 0.389$^{}$ & 0.065$^{+}$ & 0.054$^{}$ & 0.048$^{*}$ & 0.043$^{+}$  \\
 &  (0.267) & (0.259) & (0.036) & (0.034) & (0.023) & (0.022)  \\
Constant  &  2.290$^{**}$ & 0.347$^{}$ & 0.375$^{***}$ & 0.049$^{}$ & 0.284$^{***}$ & 0.033$^{}$  \\
 &  (0.730) & (1.209) & (0.098) & (0.139) & (0.066) & (0.104)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,656 & 1,656 & 1,656 & 1,656 & 1,656 & 1,656  \\
Adjusted $R^2$ &  0.020 & 0.025 & 0.044 & 0.052 & 0.041 & 0.049  \\
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
Treatment  &  -0.158$^{}$ & -0.121$^{}$ & 0.004$^{}$ & -0.000$^{}$ & 0.002$^{}$ & -0.001$^{}$  \\
 &  (0.162) & (0.132) & (0.013) & (0.013) & (0.012) & (0.012)  \\
Constant  &  1.274$^{*}$ & 0.421$^{}$ & 0.067$^{}$ & -0.038$^{}$ & 0.062$^{+}$ & -0.037$^{}$  \\
 &  (0.587) & (0.668) & (0.044) & (0.063) & (0.035) & (0.055)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,656 & 1,656 & 1,656 & 1,656 & 1,656 & 1,656  \\
Adjusted $R^2$ &  0.001 & 0.004 & 0.006 & 0.016 & 0.006 & 0.015  \\
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
Treatment  &  0.269$^{}$ & 0.325$^{}$ & 0.016$^{}$ & 0.023$^{}$ & -0.008$^{}$ & -0.006$^{}$  \\
 &  (0.395) & (0.398) & (0.047) & (0.046) & (0.025) & (0.025)  \\
Constant  &  4.164$^{**}$ & 3.606$^{*}$ & 0.698$^{***}$ & 0.369$^{+}$ & 0.501$^{***}$ & 0.313$^{**}$  \\
 &  (1.272) & (1.548) & (0.125) & (0.193) & (0.064) & (0.103)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,656 & 1,656 & 1,656 & 1,656 & 1,656 & 1,656  \\
Adjusted $R^2$ &  0.008 & 0.006 & 0.013 & 0.017 & 0.020 & 0.023  \\
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
Treatment  &  0.180$^{}$ & -0.677$^{}$ & -0.159$^{}$ & -0.246$^{}$ & 0.028$^{}$ & 0.005$^{}$  \\
 &  (1.198) & (1.229) & (0.171) & (0.176) & (0.052) & (0.060)  \\
Constant  &  5.747$^{*}$ & 0.104$^{}$ & 0.851$^{*}$ & -0.336$^{}$ & 0.146$^{}$ & -0.159$^{}$  \\
 &  (2.675) & (4.915) & (0.418) & (0.697) & (0.119) & (0.228)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  271 & 271 & 271 & 271 & 271 & 271  \\
Adjusted $R^2$ &  -0.025 & -0.016 & 0.109 & 0.109 & 0.097 & 0.097  \\
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
Treatment  &  0.421$^{}$ & 0.060$^{}$ & -0.036$^{}$ & -0.045$^{}$ & 0.065$^{}$ & 0.026$^{}$  \\
 &  (1.082) & (0.931) & (0.126) & (0.112) & (0.067) & (0.068)  \\
Constant  &  2.569$^{}$ & -5.725$^{}$ & 0.386$^{}$ & -1.008$^{*}$ & 0.148$^{}$ & -0.517$^{+}$  \\
 &  (2.588) & (3.760) & (0.248) & (0.500) & (0.157) & (0.298)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  271 & 271 & 271 & 271 & 271 & 271  \\
Adjusted $R^2$ &  -0.031 & -0.005 & 0.053 & 0.088 & 0.064 & 0.103  \\
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
Treatment  &  -0.173$^{}$ & -0.671$^{}$ & -0.135$^{}$ & -0.220$^{}$ & -0.083$^{}$ & -0.107$^{+}$  \\
 &  (1.016) & (1.042) & (0.123) & (0.139) & (0.062) & (0.065)  \\
Constant  &  2.343$^{}$ & 4.098$^{}$ & 0.433$^{}$ & 0.495$^{}$ & 0.147$^{}$ & 0.188$^{}$  \\
 &  (1.857) & (3.995) & (0.367) & (0.504) & (0.154) & (0.259)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  271 & 271 & 271 & 271 & 271 & 271  \\
Adjusted $R^2$ &  -0.019 & -0.020 & 0.053 & 0.076 & 0.035 & 0.050  \\
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
Treatment  &  1.153$^{}$ & 1.431$^{}$ & 0.148$^{}$ & 0.167$^{}$ & 0.023$^{}$ & 0.010$^{}$  \\
 &  (0.711) & (0.874) & (0.097) & (0.116) & (0.032) & (0.031)  \\
Constant  &  5.745$^{***}$ & 5.464$^{}$ & 0.948$^{***}$ & 0.389$^{}$ & 0.524$^{***}$ & 0.266$^{}$  \\
 &  (1.291) & (4.667) & (0.149) & (0.594) & (0.058) & (0.183)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  811 & 811 & 811 & 811 & 811 & 811  \\
Adjusted $R^2$ &  0.004 & 0.001 & -0.000 & 0.001 & -0.006 & 0.002  \\
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
Treatment  &  0.269$^{}$ & 0.476$^{}$ & 0.066$^{}$ & 0.095$^{+}$ & 0.009$^{}$ & 0.006$^{}$  \\
 &  (0.373) & (0.454) & (0.051) & (0.057) & (0.030) & (0.027)  \\
Constant  &  0.459$^{}$ & 2.107$^{}$ & 0.182$^{*}$ & 0.516$^{+}$ & 0.146$^{**}$ & 0.119$^{}$  \\
 &  (0.492) & (2.635) & (0.071) & (0.303) & (0.051) & (0.171)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  811 & 811 & 811 & 811 & 811 & 811  \\
Adjusted $R^2$ &  0.024 & 0.037 & 0.011 & 0.026 & 0.008 & 0.025  \\
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
Treatment  &  0.903$^{}$ & 0.963$^{}$ & 0.086$^{}$ & 0.074$^{}$ & 0.042$^{}$ & 0.041$^{}$  \\
 &  (0.637) & (0.711) & (0.078) & (0.082) & (0.033) & (0.034)  \\
Constant  &  5.210$^{***}$ & 3.202$^{}$ & 0.747$^{***}$ & -0.163$^{}$ & 0.459$^{***}$ & 0.327$^{+}$  \\
 &  (1.249) & (3.423) & (0.133) & (0.452) & (0.065) & (0.186)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  811 & 811 & 811 & 811 & 811 & 811  \\
Adjusted $R^2$ &  -0.005 & -0.006 & -0.003 & 0.002 & -0.002 & -0.000  \\
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
Treatment  &  0.116$^{}$ & 0.214$^{}$ & 0.206$^{}$ & 0.224$^{}$ & -0.013$^{}$ & 0.002$^{}$  \\
 &  (1.279) & (1.175) & (0.140) & (0.137) & (0.061) & (0.057)  \\
Constant  &  14.461$^{***}$ & 11.108$^{}$ & 1.405$^{***}$ & 2.488$^{+}$ & 0.540$^{***}$ & 0.969$^{+}$  \\
 &  (2.251) & (12.839) & (0.160) & (1.344) & (0.061) & (0.577)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  350 & 350 & 350 & 350 & 350 & 350  \\
Adjusted $R^2$ &  -0.002 & -0.003 & -0.002 & 0.000 & 0.003 & 0.033  \\
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
Treatment  &  1.251$^{*}$ & 1.306$^{*}$ & 0.162$^{*}$ & 0.166$^{*}$ & 0.117$^{*}$ & 0.121$^{*}$  \\
 &  (0.625) & (0.632) & (0.068) & (0.069) & (0.050) & (0.050)  \\
Constant  &  0.605$^{}$ & 1.329$^{}$ & 0.067$^{}$ & 0.464$^{}$ & 0.042$^{}$ & 0.299$^{}$  \\
 &  (0.688) & (4.245) & (0.085) & (0.560) & (0.058) & (0.383)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  350 & 350 & 350 & 350 & 350 & 350  \\
Adjusted $R^2$ &  0.006 & -0.000 & 0.019 & 0.011 & 0.005 & 0.011  \\
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
Treatment  &  -1.135$^{}$ & -1.091$^{}$ & 0.043$^{}$ & 0.057$^{}$ & -0.052$^{}$ & -0.042$^{}$  \\
 &  (1.265) & (1.211) & (0.130) & (0.129) & (0.065) & (0.063)  \\
Constant  &  13.855$^{***}$ & 9.779$^{}$ & 1.338$^{***}$ & 2.024$^{+}$ & 0.534$^{***}$ & 0.837$^{}$  \\
 &  (2.284) & (12.190) & (0.144) & (1.167) & (0.072) & (0.580)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  350 & 350 & 350 & 350 & 350 & 350  \\
Adjusted $R^2$ &  -0.005 & -0.008 & -0.013 & -0.002 & -0.000 & -0.001  \\
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
Treatment  &  2.285$^{+}$ & 2.623$^{}$ & 0.124$^{}$ & 0.103$^{}$ & 0.108$^{}$ & 0.111$^{}$  \\
 &  (1.377) & (1.742) & (0.153) & (0.158) & (0.095) & (0.085)  \\
Constant  &  8.029$^{***}$ & 11.178$^{}$ & 1.463$^{***}$ & 4.662$^{**}$ & 0.807$^{***}$ & 2.768$^{***}$  \\
 &  (1.496) & (14.001) & (0.274) & (1.477) & (0.178) & (0.719)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  142 & 142 & 142 & 142 & 142 & 142  \\
Adjusted $R^2$ &  0.078 & 0.108 & 0.121 & 0.144 & 0.104 & 0.135  \\
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
Treatment  &  0.332$^{}$ & -0.103$^{}$ & -0.041$^{}$ & -0.053$^{}$ & -0.015$^{}$ & -0.039$^{}$  \\
 &  (0.671) & (0.636) & (0.067) & (0.066) & (0.056) & (0.059)  \\
Constant  &  3.892$^{**}$ & -0.574$^{}$ & 0.629$^{**}$ & 1.645$^{+}$ & 0.487$^{**}$ & 1.072$^{}$  \\
 &  (1.485) & (8.787) & (0.226) & (0.952) & (0.158) & (0.717)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  142 & 142 & 142 & 142 & 142 & 142  \\
Adjusted $R^2$ &  -0.018 & -0.049 & 0.026 & 0.013 & 0.029 & 0.010  \\
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
Treatment  &  1.953$^{}$ & 2.726$^{}$ & 0.165$^{}$ & 0.156$^{}$ & 0.144$^{}$ & 0.153$^{+}$  \\
 &  (1.426) & (1.669) & (0.141) & (0.130) & (0.098) & (0.078)  \\
Constant  &  4.138$^{*}$ & 11.752$^{}$ & 0.834$^{***}$ & 3.017$^{**}$ & 0.628$^{**}$ & 2.528$^{***}$  \\
 &  (1.791) & (10.305) & (0.244) & (0.989) & (0.207) & (0.667)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  142 & 142 & 142 & 142 & 142 & 142  \\
Adjusted $R^2$ &  0.076 & 0.152 & 0.075 & 0.133 & 0.092 & 0.157  \\
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
Treatment  &  3.049$^{}$ & 2.961$^{}$ & 0.715$^{*}$ & 0.872$^{*}$ & 0.037$^{}$ & 0.058$^{}$  \\
 &  (1.991) & (1.871) & (0.344) & (0.381) & (0.111) & (0.125)  \\
Constant  &  14.737$^{*}$ & 4.570$^{}$ & 2.044$^{*}$ & 1.417$^{}$ & 0.722$^{**}$ & 0.319$^{}$  \\
 &  (5.904) & (8.725) & (0.930) & (2.377) & (0.267) & (0.485)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  82 & 82 & 82 & 82 & 82 & 82  \\
Adjusted $R^2$ &  0.006 & 0.019 & -0.006 & 0.093 & 0.016 & 0.033  \\
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
Treatment  &  3.048$^{**}$ & 2.417$^{*}$ & 0.643$^{*}$ & 0.584$^{**}$ & 0.291$^{**}$ & 0.294$^{**}$  \\
 &  (1.148) & (0.921) & (0.254) & (0.210) & (0.100) & (0.098)  \\
Constant  &  7.745$^{**}$ & 9.371$^{+}$ & 0.744$^{**}$ & -0.124$^{}$ & 0.657$^{**}$ & 0.847$^{*}$  \\
 &  (2.544) & (5.347) & (0.244) & (2.074) & (0.197) & (0.375)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  82 & 82 & 82 & 82 & 82 & 82  \\
Adjusted $R^2$ &  0.073 & 0.113 & 0.052 & 0.122 & 0.070 & 0.138  \\
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
Treatment  &  0.001$^{}$ & 0.543$^{}$ & 0.072$^{}$ & 0.288$^{}$ & -0.050$^{}$ & -0.008$^{}$  \\
 &  (1.872) & (1.855) & (0.227) & (0.257) & (0.122) & (0.133)  \\
Constant  &  6.992$^{}$ & -4.801$^{}$ & 1.300$^{}$ & 1.542$^{}$ & 0.495$^{+}$ & -0.203$^{}$  \\
 &  (4.310) & (9.163) & (0.839) & (1.295) & (0.274) & (0.548)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  82 & 82 & 82 & 82 & 82 & 82  \\
Adjusted $R^2$ &  -0.072 & -0.082 & -0.027 & 0.012 & -0.018 & -0.008  \\
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
Treatment  &  1.178$^{+}$ & 0.937$^{}$ & 0.103$^{*}$ & 0.084$^{+}$ & 0.045$^{+}$ & 0.035$^{}$  \\
 &  (0.705) & (0.701) & (0.047) & (0.046) & (0.025) & (0.026)  \\
Constant  &  5.830$^{*}$ & -2.921$^{}$ & 0.517$^{***}$ & -0.192$^{}$ & 0.352$^{***}$ & -0.016$^{}$  \\
 &  (2.451) & (3.017) & (0.145) & (0.199) & (0.070) & (0.104)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,448 & 1,448 & 1,448 & 1,448 & 1,448 & 1,448  \\
Adjusted $R^2$ &  0.018 & 0.026 & 0.026 & 0.040 & 0.032 & 0.041  \\
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
Treatment  &  0.406$^{}$ & 0.308$^{}$ & 0.048$^{*}$ & 0.041$^{+}$ & 0.037$^{*}$ & 0.032$^{+}$  \\
 &  (0.336) & (0.344) & (0.021) & (0.021) & (0.017) & (0.017)  \\
Constant  &  2.704$^{**}$ & -1.910$^{}$ & 0.207$^{***}$ & -0.078$^{}$ & 0.155$^{***}$ & -0.072$^{}$  \\
 &  (0.983) & (1.332) & (0.060) & (0.090) & (0.046) & (0.076)  \\
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
Treatment  &  0.754$^{}$ & 0.607$^{}$ & 0.054$^{}$ & 0.041$^{}$ & 0.028$^{}$ & 0.021$^{}$  \\
 &  (0.648) & (0.662) & (0.040) & (0.040) & (0.025) & (0.025)  \\
Constant  &  2.983$^{}$ & -1.164$^{}$ & 0.297$^{*}$ & -0.129$^{}$ & 0.225$^{**}$ & -0.005$^{}$  \\
 &  (2.370) & (2.907) & (0.134) & (0.176) & (0.074) & (0.106)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,448 & 1,448 & 1,448 & 1,448 & 1,448 & 1,448  \\
Adjusted $R^2$ &  0.012 & 0.011 & 0.021 & 0.027 & 0.023 & 0.026  \\
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
Treatment  &  0.278$^{}$ & 0.445$^{}$ & -0.018$^{}$ & -0.007$^{}$ & -0.027$^{}$ & -0.024$^{}$  \\
 &  (0.769) & (0.774) & (0.058) & (0.057) & (0.027) & (0.026)  \\
Constant  &  9.229$^{***}$ & 9.688$^{**}$ & 1.113$^{***}$ & 1.007$^{***}$ & 0.603$^{***}$ & 0.499$^{***}$  \\
 &  (1.907) & (3.118) & (0.166) & (0.258) & (0.063) & (0.111)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,397 & 1,397 & 1,397 & 1,397 & 1,397 & 1,397  \\
Adjusted $R^2$ &  0.001 & 0.002 & 0.020 & 0.018 & 0.024 & 0.026  \\
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
Treatment  &  0.679$^{}$ & 0.610$^{}$ & 0.024$^{}$ & 0.018$^{}$ & 0.012$^{}$ & 0.010$^{}$  \\
 &  (0.465) & (0.454) & (0.037) & (0.036) & (0.023) & (0.022)  \\
Constant  &  2.412$^{*}$ & 1.043$^{}$ & 0.370$^{***}$ & 0.251$^{+}$ & 0.264$^{***}$ & 0.165$^{}$  \\
 &  (1.074) & (1.742) & (0.099) & (0.149) & (0.064) & (0.101)  \\
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
Treatment  &  -0.379$^{}$ & -0.141$^{}$ & -0.041$^{}$ & -0.024$^{}$ & -0.035$^{}$ & -0.028$^{}$  \\
 &  (0.647) & (0.653) & (0.042) & (0.042) & (0.026) & (0.026)  \\
Constant  &  6.599$^{***}$ & 8.497$^{**}$ & 0.725$^{***}$ & 0.742$^{***}$ & 0.482$^{***}$ & 0.420$^{***}$  \\
 &  (1.670) & (2.865) & (0.127) & (0.201) & (0.066) & (0.107)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,397 & 1,397 & 1,397 & 1,397 & 1,397 & 1,397  \\
Adjusted $R^2$ &  -0.005 & -0.003 & 0.009 & 0.010 & 0.019 & 0.022  \\
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
Treatment  &  0.616$^{}$ & 0.665$^{}$ & 0.091$^{}$ & 0.074$^{}$ & 0.011$^{}$ & 0.007$^{}$  \\
 &  (0.532) & (0.521) & (0.069) & (0.066) & (0.025) & (0.023)  \\
Constant  &  9.582$^{***}$ & 5.949$^{**}$ & 1.189$^{***}$ & 0.459$^{+}$ & 0.573$^{***}$ & 0.286$^{**}$  \\
 &  (1.618) & (1.909) & (0.186) & (0.252) & (0.069) & (0.097)  \\
Dept Ranking (centered)  &  0.015$^{}$ & 0.027$^{+}$ & -0.003$^{*}$ & -0.001$^{}$ & -0.001$^{*}$ & -0.001$^{}$  \\
 &  (0.013) & (0.014) & (0.001) & (0.002) & (0.001) & (0.001)  \\
Treatment $\times$ Dept Ranking (centered)  &  0.006$^{}$ & 0.003$^{}$ & 0.004$^{+}$ & 0.004$^{*}$ & 0.001$^{}$ & 0.001$^{}$  \\
 &  (0.017) & (0.016) & (0.002) & (0.002) & (0.001) & (0.001)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,656 & 1,656 & 1,656 & 1,656 & 1,656 & 1,656  \\
Adjusted $R^2$ &  0.011 & 0.015 & 0.028 & 0.036 & 0.035 & 0.047  \\
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
Treatment  &  0.862$^{}$ & 0.683$^{}$ & 0.094$^{}$ & 0.079$^{}$ & 0.011$^{}$ & 0.007$^{}$  \\
 &  (0.526) & (0.515) & (0.070) & (0.066) & (0.025) & (0.023)  \\
Constant  &  8.147$^{***}$ & 3.132$^{}$ & 1.242$^{***}$ & 0.324$^{}$ & 0.632$^{***}$ & 0.265$^{*}$  \\
 &  (1.433) & (2.071) & (0.177) & (0.296) & (0.063) & (0.104)  \\
Total Faculty (centered)  &  -0.057$^{**}$ & -0.065$^{**}$ & -0.002$^{}$ & -0.003$^{}$ & -0.000$^{}$ & -0.001$^{}$  \\
 &  (0.019) & (0.020) & (0.003) & (0.003) & (0.001) & (0.001)  \\
Treatment $\times$ Total Faculty (centered)  &  0.053$^{*}$ & 0.057$^{*}$ & 0.002$^{}$ & 0.003$^{}$ & 0.001$^{}$ & 0.001$^{}$  \\
 &  (0.024) & (0.024) & (0.003) & (0.003) & (0.001) & (0.001)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,656 & 1,656 & 1,656 & 1,656 & 1,656 & 1,656  \\
Adjusted $R^2$ &  0.013 & 0.017 & 0.025 & 0.033 & 0.031 & 0.047  \\
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
Treatment  &  0.663$^{}$ & 0.656$^{}$ & 0.094$^{}$ & 0.077$^{}$ & 0.011$^{}$ & 0.007$^{}$  \\
 &  (0.533) & (0.522) & (0.068) & (0.066) & (0.024) & (0.023)  \\
Constant  &  8.350$^{***}$ & 8.105$^{***}$ & 1.205$^{***}$ & 1.017$^{***}$ & 0.615$^{***}$ & 0.513$^{***}$  \\
 &  (1.505) & (1.698) & (0.173) & (0.216) & (0.060) & (0.078)  \\
Peer URM Faculty (centered)  &  0.077$^{}$ & 0.136$^{*}$ & 0.017$^{**}$ & 0.019$^{**}$ & 0.007$^{**}$ & 0.007$^{**}$  \\
 &  (0.055) & (0.055) & (0.006) & (0.006) & (0.002) & (0.002)  \\
Treatment $\times$ Peer URM Faculty (centered)  &  -0.075$^{}$ & -0.054$^{}$ & -0.003$^{}$ & -0.002$^{}$ & -0.001$^{}$ & -0.000$^{}$  \\
 &  (0.075) & (0.072) & (0.008) & (0.008) & (0.003) & (0.003)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,656 & 1,656 & 1,656 & 1,656 & 1,656 & 1,656  \\
Adjusted $R^2$ &  0.011 & 0.015 & 0.032 & 0.033 & 0.041 & 0.046  \\
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
Chemistry & Any Hispanic & Treatment & Extended & -0.1069 & 0.0647 & -1.652 & 0.0999 & + \\
Computer Science & \% URM & Treatment & Simple & 2.2852 & 1.3775 & 1.659 & 0.0996 & + \\
Computer Science & Any Hispanic & Treatment & Extended & 0.1532 & 0.0780 & 1.964 & 0.0520 & + \\
Mathematics & Count Black & Treatment & Extended & 0.0955 & 0.0573 & 1.666 & 0.0961 & + \\
Mechanical Engineering & \% Black & Treatment & Simple & 3.0477 & 1.1484 & 2.654 & 0.0100 & ** \\
Mechanical Engineering & Any Black & Treatment & Extended & 0.2940 & 0.0975 & 3.015 & 0.0038 & ** \\
Mechanical Engineering & Count Black & Treatment & Extended & 0.5838 & 0.2101 & 2.778 & 0.0074 & ** \\
Mechanical Engineering & Count URM & Treatment & Extended & 0.8722 & 0.3807 & 2.291 & 0.0257 & * \\
Physics & \% Black & Treatment & Extended & 1.3056 & 0.6321 & 2.065 & 0.0397 & * \\
Physics & Any Black & Treatment & Extended & 0.1210 & 0.0504 & 2.398 & 0.0170 & * \\
Physics & Count Black & Treatment & Extended & 0.1664 & 0.0686 & 2.424 & 0.0159 & * \\
\addlinespace[0.5em]
\multicolumn{9}{l}{\textbf{Identity Analysis}} \\
\midrule
Demographic Subgroup & \% Black & Treatment & Simple & 0.5612 & 0.3127 & 1.794 & 0.0729 & + \\
Demographic Subgroup & \% Black Male & Treatment & Simple & 0.4635 & 0.2665 & 1.739 & 0.0823 & + \\
Demographic Subgroup & Any Black & Treatment & Simple & 0.0422 & 0.0233 & 1.813 & 0.0700 & + \\
Demographic Subgroup & Any Black Male & Treatment & Simple & 0.0480 & 0.0229 & 2.095 & 0.0363 & * \\
Demographic Subgroup & Count Black Male & Treatment & Simple & 0.0647 & 0.0357 & 1.811 & 0.0703 & + \\
\addlinespace[0.5em]
\multicolumn{9}{l}{\textbf{Moderation Analysis}} \\
\midrule
Department Rank & Count URM & Treatment $\times$ Dept Ranking & Extended & 0.0039 & 0.0019 & 2.005 & 0.0451 & * \\
Faculty Size & \% URM & Treatment $\times$ Faculty Size & Extended & 0.0566 & 0.0237 & 2.389 & 0.0170 & * \\
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
