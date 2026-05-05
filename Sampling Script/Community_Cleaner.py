import requests
import pandas
import time

#INSERT Github PAT
token = ""

# Set headers to get PR diff media per GitHub REST API Documentation: https://docs.github.com/en/rest/pulls/pulls?apiVersion=2022-11-28#get-a-pull-request

headers = {
    'Authorization': f'token {token}',
    'Accept': 'application/vnd.github.v3.+json'
}

def main():
    # Read from sorted msr csv with only PRs with maintainer comments
    df = pandas.read_csv('sorted_msr_data.csv', usecols=['PR Number', 'Author', 'Created Time', 'Merged', 'Time to Merge (hours)', 'Maintainer Comments'])

    addsList = []
    delsList = []
    netList = []
    filenameList = []
    locList = []
    ratioList = []

    # Loop through PR numbers
    for prNum in df['PR Number']:
        try: 
            prNum = int(prNum)
            # Get the files for that PR
            response = requests.get(f"https://api.github.com/repos/talonhub/community/pulls/{prNum}/files", headers=headers)

            # For successful GET requests, perform the diff info gathering
            if response.status_code == 200:
                diffs = response.json()

                additions = []
                deletions = []
                nets = []
                filenames = []
                locs = []
                ratios = []

                # Loop through each of the files updated in the PR
                for diff in diffs:
                    add = diff.get('additions')
                    dele = diff.get('deletions')
                    net = add - dele
                    file = diff.get('filename')
                    fileURL = diff['raw_url']

                    # Use the file URL to get the LOCs per file
                    totalLoc = 0
                    resp = requests.get(fileURL, headers=headers)
                    if resp.status_code == 200:
                        # Get the file length from the file returned
                        totalLoc = len(resp.text.splitlines())
                    
                    # Get the ratio of the changes per LOC
                    changes = add + dele
                    if totalLoc > 0:
                        ratio = round(changes / totalLoc, 4)

                    # Handle deleted or empty files
                    else:
                        if changes > 0:
                            ratio = 1.0
                        else:
                            ratio = 0.0

                    # Store the file diff info
                    additions.append(add)
                    deletions.append(dele)
                    nets.append(net)
                    filenames.append(file)
                    locs.append(totalLoc)
                    ratios.append(ratio)

                # Append the addition, deletion, net change, filename, LOC, and ratio data per file in PR to the lists
                addsList.append(additions)
                delsList.append(deletions)
                netList.append(nets)
                filenameList.append(filenames)
                locList.append(locs)
                ratioList.append(ratios)

                print(f"Processed PR {prNum} ({len(file)} files)")

            
            # Handle the 6 instances where the PR has overridden into the next row and the PR Number is invalid
            else:
                addsList.append(None)
                delsList.append(None)
                netList.append(None)
                filenameList.append(None)
                locList.append(None)
                ratioList.append(None)
            
            # Time delay for API
            time.sleep(0.1)
    
    # Handle connection errors
        except requests.exceptions.RequestException as e:
            print(f"Connection error for PR {prNum}: {e}")
            addsList.append(None)
            delsList.append(None)
            netList.append(None)
            filenameList.append(None)
            locList.append(None)
            ratioList.append(None)

    '''
    print(f"Files Changed {filenameList}")  
    print(f"Line Additions Per File {addsList}")
    print(f"Line Deletions Per File {delsList}")
    print(f"Net Lines Changed Per File {netList}")
    print(f"LOC Per File {locList}")
    print(f"Total LOC Changed Per File {ratioList}") 
    '''
    # Add the filename, addition, deletion, net, LOC, and ratio lists per PR to the csv
    df['Files Changed'] = filenameList
    df['Line Additions Per File'] = addsList
    df['Line Deletions Per File'] = delsList
    df['Net Lines Changed Per File'] = netList
    df['LOC Per File'] = locList
    df['Changed Lines / LOC  Ratio Per File'] = ratioList
    

    # Save to new csv
    df.to_csv("diff_sorted_msr_data.csv", index=False)

if __name__ == "__main__":
    main()    