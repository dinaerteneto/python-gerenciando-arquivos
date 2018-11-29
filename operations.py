from bank_account_variables import accounts, money_slips
import getpass


def do_operation(account, option) :
    if option == '1' :
        show_balance(account)
    elif option == '2' :
        withdraw(account)
    elif option == '10' and account['admin'] :
        insert_money_slips()


def show_balance(account) :
    print("Seu saldo atual é de R$ %s" % account['balance_value'])


def withdraw(account) :
    fCashOutValue_typed = input("Digite o valor que deseja sacar: ")
    fCashOutValue = float(fCashOutValue_typed)
    if(int(fCashOutValue) < account['balance_value']):
        money_slips_user = {}
        value_int = int(fCashOutValue_typed)
        
        for key, value in sorted(money_slips.items(), reverse=True) :
            iKey = int(key)
            if value_int // iKey > 0 and value_int // iKey <= money_slips[key] :
                money_slips_user[key] = value_int // iKey
                value_int = value_int - value_int // iKey * iKey

        if value_int != 0:
            print('O caixa não tem cédulas disponíveis para este valor')
        else:
            for money_bill in money_slips_user:
                money_slips[money_bill] -= money_slips_user[money_bill]

            account['balance_value'] -= fCashOutValue

            print('Valor sacado R$: %s' % fCashOutValue)
            print('Saldo após o saque R$: %s' % account['balance_value'])
            print('Pegue as notas:')
            print(money_slips_user)
    else : 
        print('O valor a ser sacado é maior que seu saldo atual.')


def insert_money_slips() :
    amount_typed = input('Digite a quantidade de cédulas: ')
    money_bill_typed = input('Escolha o valor da cédula a ser incluída: ')
    money_slips[int(money_bill_typed)] += int(amount_typed)
    print(money_slips)


def auth_account() :
    account_typed = input('Digite sua conta: ')
    password_typed = getpass.getpass('Digite sua senha: ')

    if account_typed in accounts and password_typed == accounts[account_typed]['password'] :
        return accounts[account_typed]
    else :
        return False


def get_menu_options_typed(account) :
    print("1 - Saldo")
    print("2 - Saque")
    if(account['admin']) :
        print("10 - Incluir cédulas")
    return input("Escolha uma das opções acima: ")