# There is a supermarket that is frequented by many customers.
# The products sold at the supermarket are represented as two parallel integer arrays
#  products and prices, where the ith product has an ID of products[i] and a price of prices[i].
# When a customer is paying, their bill is represented as two parallel integer arrays
#  product and amount, where the jth product they purchased has an ID of product[j],
#  and amount[j] is how much of the product they bought.
# Their subtotal is calculated as the sum of each amount[j] * (price of the jth product).
# The supermarket decided to have a sale. Every nth customer paying for their groceries
#  will be given a percentage discount.
# The discount amount is given by discount,
#  where they will be given discount percent off their subtotal.
# More formally, if their subtotal is bill,
#  then they would actually pay bill * ((100 - discount) / 100).
# Implement the Cashier class:
#  - Cashier(int n, int discount, int[] products, int[] prices)
#    Initializes the object with n, the discount, and the products and their prices.
#  - double getBill(int[] product, int[] amount)
#    Returns the final total of the bill with the discount applied (if any).
#    Answers within 10 ** -5 of the actual value will be accepted.
# ------------------------
# 1 <= n <= 10 ** 4
# 0 <= discount <= 100
# 1 <= products.length <= 200
# prices.length == products.length
# 1 <= products[i] <= 200
# 1 <= prices[i] <= 1000
# The elements in products are unique.
# 1 <= product.length <= products.length
# amount.length == product.length
# product[j] exists in products.
# 1 <= amount[j] <= 1000
# The elements of product are unique.
# At most 1000 calls will be made to getBill.
# Answers within 10 ** -5 of the actual value will be accepted. 


class Cashier:
    # working_sol (23.20%, 66.77%) -> (30ms, 30.85mb)

    def __init__(self, n: int, discount: int, products: list[int], prices: list[int]):
        # time: O(n) | space: O(n + k) <- n == len(products)
        self.n: int = n
        self.cust_count: int = 0
        self.discount: int = discount
        # { product: price }
        self.assort: dict[int, int] = {
            products[index]: prices[index] for index in range(len(products))
        }

    def getBill(self, product: list[int], amount: list[int]) -> float:
        # time: O(n) | space: O(1) <- n - len(product)
        item: int
        item_quantity: int
        bill: float = 0
        self.cust_count += 1
        for index in range(len(product)):
            item, item_quantity = product[index], amount[index]
            item_price: int | None = self.assort.get(item)
            if item_price is None:
                continue
            full_price: int = item_price * item_quantity
            bill += full_price
        if 0 == self.cust_count % self.n:
            bill *= ((100 - self.discount) / 100)

        return bill
        