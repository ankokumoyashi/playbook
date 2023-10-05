docker exec -it hydra python3 -c "
import pandas as pd;
result=pd.read_csv(\"${RESULT_CSV}\")
[(print(f'=={id}=='), print(r)) for id,r in zip(result['識別子'], result.filter(regex='assistant').iloc[:,-1])]
"
