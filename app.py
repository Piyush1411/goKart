import asyncio
from flask import Flask, request, jsonify, render_template
import time

app = Flask(__name__)

class InventoryManager:
    def __init__(self):
        self.products = {}
        self.warehouses = {}
        self.states = {}
        self.orders = []
        self.command_history = []
        self.batch_size = 2

    # Implement the rest of the methods for inventory management

    def add_product(self, product_name, sku, category, sub_category, image_link=None):
        # Implement the logic to add a product to the product catalog
        pass

    def add_warehouse(self, warehouse_num, warehouse_name, state, location, stock_limit=None):
        # Implement the logic to add a warehouse to the inventory
        pass

    def add_stock(self, sku, warehouse_num, qty):
        # Implement the logic to add stock to a warehouse
        pass

    def add_state(self, state):
        # Implement the logic to add a state to the active states list
        pass

    def view_state(self):
        # Implement the logic to view the list of states along with warehouse information
        pass

    def process_order(self, cust_id, sku, order_qty, cust_loc):
        # Implement the logic to process an order
        pass

    def view_orders(self):
        # Implement the logic to view the list of orders
        pass

    def list_products(self):
        # Implement the logic to list all products in the product catalog
        pass

    def list_warehouses(self):
        # Implement the logic to list all warehouses
        pass

    def warehouse_info(self, warehouse_num):
        # Implement the logic to retrieve information about a warehouse
        pass

    def process_command(self, command):
        command_parts = command.split(' ', 1)
        command_name = command_parts[0].strip().lower()
        command_args = command_parts[1].strip() if len(command_parts) > 1 else ''
        response = ''

        if command_name == 'add product':
            # Parse the command arguments and call the add_product method
            args = command_args.split(',')
            # Extract the product details from args
            self.add_product(*args)
            response = render_template('inventory.html', products=inventory_manager.list_products())


        elif command_name == 'add warehouse':
            # Parse the command arguments and call the add_warehouse method
            args = command_args.split(',')
            # Extract the warehouse details from args
            self.add_warehouse(*args)
            response = 'Warehouse added successfully.'

        elif command_name == 'add stock':
            # Parse the command arguments and call the add_stock method
            args = command_args.split(',')
            # Extract the stock details from args
            self.add_stock(*args)
            response = 'Stock added successfully.'

        elif command_name == 'add state':
            # Parse the command arguments and call the add_state method
            args = command_args.split(',')
            # Extract the state detailsSorry for the incomplete response. Here's the complete code for the `process_command` method:

        elif command_name == 'add state':
            # Parse the command arguments and call the add_state method
            state = command_args.strip('"')
            self.add_state(state)
            response = 'State added successfully.'

        elif command_name == 'view state':
            # Call the view_state method
            state_info = self.view_state()
            response = state_info

        elif command_name == 'add stock':
            # Parse the command arguments and call the add_stock method
            args = command_args.split(',')
            sku = args[0].strip()
            warehouse_num = args[1].strip()
            qty = int(args[2].strip())
            self.add_stock(sku, warehouse_num, qty)
            response = 'Stock added successfully.'

        elif command_name == 'process order':
            # Parse the command arguments and call the process_order method
            args = command_args.split(',')
            cust_id = args[0].strip()
            sku = args[1].strip()
            order_qty = int(args[2].strip())
            cust_loc = args[3].strip()
            self.process_order(cust_id, sku, order_qty, cust_loc)
            response = 'Order processed successfully.'

        elif command_name == 'view orders':
            # Call the view_orders method
            order_info = self.view_orders()
            response = order_info

        elif command_name == 'list products':
            # Call the list_products method
            product_info = self.list_products()
            response = product_info

        elif command_name == 'list warehouses':
            # Call the list_warehouses method
            warehouse_info = self.list_warehouses()
            response = warehouse_info

        elif command_name == 'warehouse info':
            # Parse the command arguments and call the warehouse_info method
            warehouse_num = command_args.strip()
            warehouse_info = self.warehouse_info(warehouse_num)
            response = warehouse_info

        self.log_command(command)  # Log the command in command history

        if len(self.command_history) % self.batch_size == 0:
            self.stream_command_history()  # Stream command history to a file in batches

        return response
    # Rest of the class implementation

    def log_command(self, command):
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
        self.command_history.append((timestamp, command))

        if len(self.command_history) % self.batch_size == 0:
            asyncio.ensure_future(self.stream_command_history())  # Start a new task to stream command history

    async def stream_command_history(self):
        with open('command_history.log', 'a') as file:
            for timestamp, command in self.command_history:
                file.write(f'{timestamp}: {command}\n')
            self.command_history = []

    def log_command(self, command):
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
        self.command_history.append((timestamp, command))

    def stream_command_history(self):
        with open('command_history.log', 'a') as file:
            for timestamp, command in self.command_history:
                file.write(f'{timestamp}: {command}\n')
            self.command_history = []

inventory_manager = InventoryManager()

@app.route('/', methods=['GET'])
def index():
    return "Welcome to the inventory management interface"


@app.route('/command', methods=['GET', 'POST'])
def process_command():
    if request.method == 'POST':
        command = request.form.get('command')
        response = inventory_manager.process_command(command)
        return response
    else:
        return render_template('inventory.html')  # Return a template for the GET method


if __name__ == '__main__':
    asyncio.run(app.run(debug=True))


