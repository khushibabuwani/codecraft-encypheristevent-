def reverse_stack(stack):
    # Base case: if the stack is empty, return
    if not stack:
        return
    
    # Step 1: Pop the top element
    top = stack.pop()
    
    # Step 2: Reverse the remaining stack
    reverse_stack(stack)
    
    # Step 3: Insert the popped element at the bottom of the reversed stack
    insert_at_bottom(stack, top)

def insert_at_bottom(stack, item):
    # Base case: if the stack is empty, push the item
    if not stack:
        stack.append(item)
        return
    
    # Step 1: Pop the top element
    temp = stack.pop()
    
    # Step 2: Insert the item at the bottom
    insert_at_bottom(stack, item)
    
    # Step 3: Push the top element back
    stack.append(temp)

# Example usage:
stack = [1, 2, 3, 4, 5]
reverse_stack(stack)
print(stack)  # Output should be [5, 4, 3, 2, 1]
