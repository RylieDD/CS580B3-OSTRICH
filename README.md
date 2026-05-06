# CS580B3-OSTRICH
### Instructions to download the Replication Package and setup the environment to run the scripts
1. Remote desktop connect to a university lab120 machine.
2. Download the Replication Package as the provided zip or download the code from the GitHub repository.
3. Open a terminal and navigate to the Downloads folder or wherever the Replication Package folder was saved to.
4. Navigate into the Scripts folder
5. Run this command: "chmod +x setup.sh"
6. Run this command to setup the environment: "setup.sh"
7. After all the required libraries finish installing, open VSCode by running the command "code" in the terminal.
8. Open the Replication Package folder in VSCode

### Instructions to run the Sampling Script code
Instructions for running the 1.Community_Mining, 2.DataMiningDataCleaning, 3.Community_Cleaner, and 4.sampling notebooks on the university lab machines:
1. Select the Sampling Scripts folder in VSCode.
2. Select and open the 1.Community_Mining notebook.
    1. In cell 2, line 1 of the 1.Community_Mining notebook, add a valid GitHub PAT to the empty string "".
    2. Select Run All in the toolbar of the notebook to execute all the cells.
3. Select and open the 2.DataMiningDataCleaning notebook.
    1. Select Run All in the toolbar of the notebook to execute all the cells.
4. Select the 3.Community_Cleaner notebook.
    1. In cell 2, line 2 of the 3.Community_Cleaner notebook, add a valid GitHub PAT to the empty string "".
    2. Select Run All in the toolbar of the notebook to execute all the cells.
5. Select the 4.sampling notebook.
    1. Select Run All in the toolbar of the notebook to execute all the cells.

### Instructions to run the LLM Model code
Instructions for running the OSTRICH_LLM_Model_no_think and OSTRICH_LLM_Model_think notebooks on the university lab machines:
1. Follow these instructions to ssh into one of the university lab325 machines: https://infospaces.cs.colostate.edu/watch.php?id=272
2. Select the Scripts folder.
3. Open the OSTRICH_LLM_Model_no_think jupyter notebook.
   
**NOTE:** VSCode will prompt you to select a environment kernel before running the jupyter notebook, choose the py313 kernel from the available options.

5. In cell 3, line 10 of the OSTRICH_LLM_Model_no_think jupyter notebook, update the Hugging Face token with a valid token to access the Hugging Face models here: "token = """.
6. In cell 6, line 3 of the OSTRICH_LLM_Model_no_think jupyter notebook, update the GitHub PAT with a valid token to access the TalonHub/Community repository here: "token = """.
7. Select Run All from the notebook toolbar to run each cell in order in the OSTRICH_LLM_Model_no_think jupyter notebook and view the output from the training and validate datasets run on the zero-shot and few-shot models with Non-Thinking mode.

**NOTE:** Each cell at the bottom of the notebook that calls the model_output function will take around 10 minutes to run and output 3 files per cell.

13. Open the OSTRICH_LLM_Model_think jupyter notebook.
14. In cell 3, line 10 of the OSTRICH_LLM_Model_think jupyter notebook, update the Hugging Face token with a valid token to access the Hugging Face models here: "token = """.
15. In cell 6, line 3 of the OSTRICH_LLM_Model_think jupyter notebook, update the GitHub PAT with a valid token to access the TalonHub/Community repository here: "token = """.
16. Select Run All from the notebook toolbar to run each cell in order in the OSTRICH_LLM_Model_think jupyter notebook and view the output from the training and validate datasets run on the zero-shot and few-shot models with Thinking mode.
    
**NOTE:** Each cell at the bottom of the notebook that calls the model_output function will take around 6 and a half hours to run and output 3 files per cell.

### Instructions to run the Metrics and Stats code
Instructions for running the OSTRICH_Metrics_And_Stats_RQ1 and OSTRICH_Metrics_And_Stats_RQ1 notebooks on the university lab machines:
1. Select the Scripts folder.
2. Open the OSTRICH_Metrics_and_Stats_RQ1 jupyter notebook.
   
**NOTE:** VSCode will prompt you to select a environment kernel before running the jupyter notebook, choose the py313 kernel

**NOTE:** If you would like to run the Metrics_And_Stats notebooks without running the LLM_Model notebooks, then add '../Results/' in front of the filenames listed below to utilize the Results folder that is included in the Replication Package.

4. In cell 2 of the OSTRICH_Metrics_and_Stats_RQ1 jupyter notebook, the filename for the "with open" command will be set to the zero-shot model categorization results with thinking mode enabled from the training dataset.
    1. To view the zero-shot model categorization results with thinking mode disabled from the training dataset, change the filename to 'category_model_results_train_zero_no_think.csv'
    2. To view the zero-shot model categorization results with thinking mode enabled from the validation dataset, change the filename to 'category_model_results_validate_zero_think.csv'
    3. To view the zero-shot model categorization results with thinking mode disabled from the validation dataset, change the filename to 'category_model_results_validate_zero_no_think.csv'
5. In cell 4 of the OSTRICH_Metrics_and_Stats_RQ1 jupyter notebook, the filename for the "plt.savefig" command will be set to save the confusion matrix as a png named for the zero-shot model categorization results with thinking mode enabled from the training dataset.
    1. To save the png for the zero-shot model categorization results with thinking mode disabled from the training dataset, change the filename to 'train_zero_shot_no_think_cm.png'
    2. To save the png for the zero-shot model categorization results with thinking mode enabled from the validation dataset, change the filename to 'validate_zero_shot_think_cm.png'
    3. To save the png for the zero-shot model categorization results with thinking mode disabled from the validation dataset, change the filename to 'validate_zero_shot_no_think_cm.png'
6. In cell 5 of the OSTRICH_Metrics_and_Stats_RQ1 jupyter notebook, the filename for the "plt.savefig" command will be set to save the confusion matrix as a png named for the dummy stratified baseline created with the zero-shot model categorization results with thinking mode enabled from the training dataset.
    1. To save the png for the dummy stratified baseline created with the zero-shot model categorization results with thinking mode disabled from the training dataset, change the filename to 'train_zero_shot_no_think_cm_baseline_stratified.png'
    2. To save the png for the dummy stratified baseline created with the  zero-shot model categorization results with thinking mode enabled from the validation dataset, change the filename to 'validate_zero_shot_think_cm_baseline_stratified.png'
    3. To save the png for the dummy stratified baseline created with the  zero-shot model categorization results with thinking mode disabled from the validation dataset, change the filename to 'validate_zero_shot_no_think_cm_baseline_stratified.png'
7. Select Run All from the notebook toolbar to run each cell in order in the OSTRICH_Metrics_and_Stats_RQ1 jupyter notebook and view the confusion matrices, F-1 scores, McNemar's results, and Hamming Loss scores for the zero-shot model and dummy stratified classifier
8. Open the OSTRICH_Metrics_and_Stats_RQ2 jupyter notebook
9. In cell 2 of the OSTRICH_Metrics_and_Stats_RQ1 jupyter notebook, the filename for the "with open" command will be set to the zero-shot model categorization results with thinking mode enabled from the training dataset.
    1. To view the zero-shot model categorization results with thinking mode disabled from the training dataset, change the filename to 'category_model_results_train_zero_no_think.csv'
    2. To view the zero-shot model categorization results with thinking mode enabled from the validation dataset, change the filename to 'category_model_results_validate_zero_think.csv'
    3. To view the zero-shot model categorization results with thinking mode disabled from the validation dataset, change the filename to 'category_model_results_validate_zero_no_think.csv'
    4. To view the zero-shot model categorization results with thinking mode enabled from the test dataset, change the filename to 'category_model_results_test_zero_think.csv'
10. In cell 3 of the OSTRICH_Metrics_and_Stats_RQ2 jupyter notebook, the filename for the "with open" command will be set to the few-shot model categorization results with thinking mode enabled from the training dataset.
    1. To view the few-shot model categorization results with thinking mode disabled from the training dataset, change the filename to 'category_model_results_train_few_no_think.csv'
    2. To view the few-shot model categorization results with thinking mode enabled from the validation dataset, change the filename to 'category_model_results_validate_few_think.csv'
    3. To view the few-shot model categorization results with thinking mode disabled from the validation dataset, change the filename to 'category_model_results_validate_few_no_think.csv'
    4. To view the few-shot model categorization results with thinking mode enabled from the test dataset, change the filename to 'category_model_results_test_few_think.csv' 
11. In cell 6 of the OSTRICH_Metrics_and_Stats_RQ2 jupyter notebook, the filename for the "plt.savefig" command will be set to save the confusion matrix as a png named for the zero-shot model categorization results with thinking mode enabled from the training dataset.
    1. To save the png for the zero-shot model categorization results with thinking mode disabled from the training dataset, change the filename to 'train_zero_shot_no_think_cm.png'
    2. To save the png for the zero-shot model categorization results with thinking mode enabled from the validation dataset, change the filename to 'validate_zero_shot_think_cm.png'
    3. To save the png for the zero-shot model categorization results with thinking mode disabled from the validation dataset, change the filename to 'validate_zero_shot_no_think_cm.png'
    4. To save the png for the zero-shot model categorization results with thinking mode enabled from the test dataset, change the filename to 'test_zero_shot_think_cm.png'
12. In cell 7 of the OSTRICH_Metrics_and_Stats_RQ2 jupyter notebook, the filename for the "plt.savefig" command will be set to save the confusion matrix as a png named for the few-shot model categorization results with thinking mode enabled from the training dataset.
    1. To save the png for the few-shot model categorization results with thinking mode disabled from the training dataset, change the filename to 'train_few_shot_no_think_cm.png'
    2. To save the png for the few-shot model categorization results with thinking mode enabled from the validation dataset, change the filename to 'validate_few_shot_think_cm.png'
    3. To save the png for the few-shot model categorization results with thinking mode disabled from the validation dataset, change the filename to 'validate_few_shot_no_think_cm.png'
    4. To save the png for the few-shot model categorization results with thinking mode enabled from the test dataset, change the filename to 'test_few_shot_think_cm.png'
13. Select Run All from the notebook toolbar to run each cell in order in the OSTRICH_Metrics_and_Stats_RQ2 jupyter notebook and view the confusion matrices, F-1 scores, McNemar's results, Hamming Loss scores, and thinking and non-thinking throughput line graphs for the zero-shot model and few-shot model

**NOTE** the LLM Model code is currently hardcoded to run on specific sets of PRs, so running our code to generate a new sample will not automatically cause the LLM code to run on the sample. Our hardcoded sets include PRs found outside of our initial sampling to improve category representation as explained in our paper, so you might not be able to generate those exact sets with our sampling code.
