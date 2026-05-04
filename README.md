# CS580B3-OSTRICH
### Instructions to run the LLM Model code
Instructions for running the OSTRICH_LLM_Model_no_think and OSTRICH_LLM_Model_think notebooks on the CSU CS lab machines:
1. Remote desktop connect to a CSU lab120 machine and open a terminal
2. Download the Scripts folder from the repository (CS580B3-OSTRICH)
3. Run the "setup.sh" script from the Scripts folder
4. Open the OSTRICH_LLM_Model_no_think jupyter notebook in VSCode
**NOTE:** VSCode will prompt you to select a environment kernel before running the jupyter notebook, choose the py313 kernel
5. In cell 2 of the OSTRICH_LLM_Model_no_think jupyter notebook, the filename for the "with open" command will be set to the zero-shot model categorization results from the training dataset.
- To view the zero-shot model categorization results from the validation dataset, change the filename to 'category_model_results_validate_zero.csv'
6. In cell 4 of the OSTRICH_LLM_Model_no_think jupyter notebook, the filename for the "plt.savefig" command will be set to save the confusion matrix as a png named for the zero-shot model categorization results from the training dataset.
- To save the png for the zero-shot model categorization results from the validation dataset, change the filename to 'validate_zero_shot_cm.png'
7. In cell 7 of the OSTRICH_LLM_Model_no_think jupyter notebook, the filenames for the "pd.read_csv" command and the "plt.savefig" command will be set to the zero-shot throughput results from the training dataset.
- To view the zero-shot model throughput results from the validation dataset, change the filename for the "pd.read_csv" command to 'time_model_results_validate_zero.csv' and change the filename for the "plt.savefig" command to 'validate_zero_token_throughput.png' 
8. Run each cell in order in the OSTRICH_LLM_Model_no_think jupyter notebook to view the confusion matrices, F-1 scores, McNemar's results, Hamming Loss scores, and throughput scatter plots for the zero-shot model and dummy stratified classifier
9. Open the OSTRICH_LLM_Model_think jupyter notebook in VSCode
10. In cell 2 of the OSTRICH_LLM_Model_think jupyter notebook, the filename for the "with open" command will be set to the zero-shot model categorization results from the training dataset.
- To view the zero-shot model categorization results from the validation dataset, change the filename to 'category_model_results_validate_zero.csv'
11. In cell 3 of the OSTRICH_LLM_Model_think jupyter notebook, the filename for the "with open" command will be set to the few-shot model categorization results from the training dataset.
- To view the few-shot model categorization results from the validation dataset, change the filename to 'category_model_results_validate_few.csv'
12. In cell 6 of the OSTRICH_LLM_Model_think jupyter notebook, the filename for the "plt.savefig" command will be set to save the confusion matrix as a png named for the zero-shot model categorization results from the training dataset.
- To save the png for the zero-shot model categorization results from the validation dataset, change the filename to 'validate_zero_shot_cm.png'
13. In cell 7 of the OSTRICH_LLM_Model_think jupyter notebook, the filename for the "plt.savefig" command will be set to save the confusion matrix as a png named for the few-shot model categorization results from the training dataset.
- To save the png for the few-shot model categorization results from the validation dataset, change the filename to 'validate_few_shot_cm.png'
14. In cell 9 of the OSTRICH_LLM_Model_think jupyter notebook, the filename for the "pd.read_csv" command and the "plt.savefig" command will be set to the zero-shot throughput results from the training dataset.
- To view the zero-shot model throughput results from the validation dataset, change the filename for the "pd.read_csv" command to 'time_model_results_validate_zero.csv' and change the filename for the "plt.savefig" command to 'validate_zero_token_throughput.png' 
15. In cell 10 of the OSTRICH_LLM_Model_think jupyter notebook, the filename for the "pd.read_csv" command and the "plt.savefig" command will be set to the few-shot throughput results from the training dataset.
- To view the few-shot model throughput results from the validation dataset, change the filename for the "pd.read_csv" command to 'time_model_results_validate_few.csv' and change the filename for the "plt.savefig" command to 'validate_few_token_throughput.png'
16. Run each cell in order in the OSTRICH_LLM_Model_think jupyter notebook to view the confusion matrices, F-1 scores, McNemar's results, Hamming Loss scores, and throughput scatter plots for the zero-shot model and few-shot model

### Instructions to run the Metrics and Stats code
Instructions for running the OSTRICH_Metrics_And_Stats_RQ1 and OSTRICH_Metrics_And_Stats_RQ1 notebooks on the CSU CS lab machines:
1. Remote desktop connect to a CSU lab120 machine and open a terminal
2. Download the Scripts folder from the repository (CS580B3-OSTRICH)
3. Run the "setup.sh" script from the Scripts folder
4. Open the OSTRICH_Metrics_and_Stats_RQ1 jupyter notebook in VSCode
**NOTE:** VSCode will prompt you to select a environment kernel before running the jupyter notebook, choose the py313 kernel
5. In cell 2 of the OSTRICH_Metrics_and_Stats_RQ1 jupyter notebook, the filename for the "with open" command will be set to the zero-shot model categorization results from the training dataset.
- To view the zero-shot model categorization results from the validation dataset, change the filename to 'category_model_results_validate_zero.csv'
6. In cell 4 of the OSTRICH_Metrics_and_Stats_RQ1 jupyter notebook, the filename for the "plt.savefig" command will be set to save the confusion matrix as a png named for the zero-shot model categorization results from the training dataset.
- To save the png for the zero-shot model categorization results from the validation dataset, change the filename to 'validate_zero_shot_cm.png'
7. In cell 7 of the OSTRICH_Metrics_and_Stats_RQ1 jupyter notebook, the filenames for the "pd.read_csv" command and the "plt.savefig" command will be set to the zero-shot throughput results from the training dataset.
- To view the zero-shot model throughput results from the validation dataset, change the filename for the "pd.read_csv" command to 'time_model_results_validate_zero.csv' and change the filename for the "plt.savefig" command to 'validate_zero_token_throughput.png' 
8. Run each cell in order in the OSTRICH_Metrics_and_Stats_RQ1 jupyter notebook to view the confusion matrices, F-1 scores, McNemar's results, Hamming Loss scores, and throughput scatter plots for the zero-shot model and dummy stratified classifier
9. Open the OSTRICH_Metrics_and_Stats_RQ2 jupyter notebook
10. In cell 2 of the OSTRICH_Metrics_and_Stats_RQ2 jupyter notebook, the filename for the "with open" command will be set to the zero-shot model categorization results from the training dataset.
- To view the zero-shot model categorization results from the validation dataset, change the filename to 'category_model_results_validate_zero.csv'
11. In cell 3 of the OSTRICH_Metrics_and_Stats_RQ2 jupyter notebook, the filename for the "with open" command will be set to the few-shot model categorization results from the training dataset.
- To view the few-shot model categorization results from the validation dataset, change the filename to 'category_model_results_validate_few.csv'
12. In cell 6 of the OSTRICH_Metrics_and_Stats_RQ2 jupyter notebook, the filename for the "plt.savefig" command will be set to save the confusion matrix as a png named for the zero-shot model categorization results from the training dataset.
- To save the png for the zero-shot model categorization results from the validation dataset, change the filename to 'validate_zero_shot_cm.png'
13. In cell 7 of the OSTRICH_Metrics_and_Stats_RQ2 jupyter notebook, the filename for the "plt.savefig" command will be set to save the confusion matrix as a png named for the few-shot model categorization results from the training dataset.
- To save the png for the few-shot model categorization results from the validation dataset, change the filename to 'validate_few_shot_cm.png'
14. In cell 9 of the OSTRICH_Metrics_and_Stats_RQ2 jupyter notebook, the filename for the "pd.read_csv" command and the "plt.savefig" command will be set to the zero-shot throughput results from the training dataset.
- To view the zero-shot model throughput results from the validation dataset, change the filename for the "pd.read_csv" command to 'time_model_results_validate_zero.csv' and change the filename for the "plt.savefig" command to 'validate_zero_token_throughput.png' 
15. In cell 10 of the OSTRICH_Metrics_and_Stats_RQ2 jupyter notebook, the filename for the "pd.read_csv" command and the "plt.savefig" command will be set to the few-shot throughput results from the training dataset.
- To view the few-shot model throughput results from the validation dataset, change the filename for the "pd.read_csv" command to 'time_model_results_validate_few.csv' and change the filename for the "plt.savefig" command to 'validate_few_token_throughput.png'
16. Run each cell in order in the OSTRICH_Metrics_and_Stats_RQ2 jupyter notebook to view the confusion matrices, F-1 scores, McNemar's results, Hamming Loss scores, and throughput scatter plots for the zero-shot model and few-shot model
