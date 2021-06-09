import hydra 

@hydra.main(config_name='config.yml')
def main(config):
    print(f'Process {config.data}')
    print(f'Drop features: {config.variables.drop_features}')

if __name__ == '__main__':
    main()

""" 
Process data1
Drop features: ['iid', 'id', 'idg', 'wave']
"""