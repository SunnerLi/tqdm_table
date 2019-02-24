from tqdm import tqdm

# Define constant
SHORT  = 15
MIDDLE = 30
LARGE  = 50

def __clear__(times: int = 11):
    """
        Clear the previous table toward the terminal
    """
    print()
    for i in range(times + 1):
        if i != times:
            print("\033[F" + '     ' * 24 + '   ', end='')
        else:
            print("\033[F", end = '')
    print("\r")

def __getCutLine__(length: int = 50, width_cell: int = 10, equal_symbol: bool = True) -> str:
    """
        Obtain the cut line

        Arg:    length          - The maximun length of the terminal
                width_cell      - The width of the table cell
                equal_symbol    - If use '=' as the symbol or not
        Ret:    The custom cut line string
    """
    cut_string = "+"
    acc_length = 0
    while True:
        if acc_length == 0:
            if equal_symbol:
                cut_string = cut_string + '=' * (width_cell) + '+'
            else:
                cut_string = cut_string + '-' * (width_cell) + '+'
            acc_length += width_cell
        else:
            if equal_symbol:
                cut_string = cut_string + '=' * (width_cell + 2) + '+'
            else:
                cut_string = cut_string + '-' * (width_cell + 2) + '+'
            acc_length += (width_cell + 2)
        if acc_length >= length - width_cell:
            break
    return cut_string

class tqdm_table(tqdm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.max_length = 100 
        self.prev_lines = -1

    def set_table_setting(self, max_length: int = 100):
        """
            Assign the setting of this object

            Arg:    max_length  - The maximun length of the terminal
        """
        self.max_length = max_length

    def set_table_info(self, mapping: dict):
        """
            Set the table information

            Arg:    mapping     - The key-value pair you want to form the table
        """
        key_string = ""
        val_string = ""
        table_string = []
        key_list = sorted(mapping.keys())

        # Clear the previous table information toward stdout
        if self.prev_lines > 0:
            __clear__(self.prev_lines)

        # Determine the width of cell
        if max([max(len(str(val)), len(key)) for key, val in mapping.items()]) <= 15:
            width_length = SHORT
        elif max([max(len(str(val)), len(key)) for key, val in mapping.items()]) <= 30:
            width_length = MIDDLE
        else:
            width_length = LARGE

        # Collect the lines of keys and values
        for key in key_list:
            val = mapping[key]
            single_max_length = max(len(key), len(str(val)))
            if len(key_string) + single_max_length + 2 < self.max_length:
                if width_length == SHORT:
                    key_string += '{:>15} | '.format(key)
                    val_string += '{:>15} | '.format(val)
                elif width_length == MIDDLE:
                    key_string += '{:>30} | '.format(key)
                    val_string += '{:>30} | '.format(val)
                else:
                    key_string += '{:>50} | '.format(key)
                    val_string += '{:>50} | '.format(val)
            else:
                table_string.append(key_string)
                table_string.append(val_string)
                if width_length == SHORT:
                    key_string = '{:>15} | '.format(key)
                    val_string = '{:>15} | '.format(val)
                elif width_length == MIDDLE:
                    key_string = '{:>30} | '.format(key)
                    val_string = '{:>30} | '.format(val)
                else:
                    key_string = '{:>50} | '.format(key)
                    val_string = '{:>50} | '.format(val)

        # Accumulate the rest information if there are some information rest
        if len(key_string) > 0 or len(val_string) > 0:
            table_string.append(key_string)
            table_string.append(val_string)

        # Transfer the containing of queue into string
        cut_string_small = __getCutLine__(length=max([len(_) for _ in table_string]), width_cell=width_length, equal_symbol=False)
        cut_string_large = __getCutLine__(length=max([len(_) for _ in table_string]), width_cell=width_length, equal_symbol=True)
        print_string = cut_string_large
        for i in range(len(table_string) // 2):
            print_string = print_string + '\n' + table_string[2*i] + '\n' + cut_string_small + '\n' + table_string[2*i+1] + '\n' + cut_string_large
        self.prev_lines = 2 * (len(table_string) + 1)

        # Write into tqdm
        self.write(print_string)