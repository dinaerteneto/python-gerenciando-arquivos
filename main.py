import utils
import operations


def main():
    utils.header()
    account = operations.auth_account()
    if account :
        print('Olá ' + account['customer_name'])
        option_typed = operations.get_menu_options_typed(account)
        operations.do_operation(account, option_typed)            
    else:
        print('Conta inválida')

while True:
    main()
    utils.pause()
    utils.clear()    
