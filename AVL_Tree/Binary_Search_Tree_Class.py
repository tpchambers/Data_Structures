class Binary_Search_Tree:

  ##BST

  class __BST_Node:
    #defines the node atrributes and initializes the node
    def __init__(self, value):
      self.height = 1
      self.value = value
      self.left = None
      self.right = None

   ###
    
    def update_height(self, t):

    # if self == None: height -- > 0 
      if self is None:
        self.height = 0
      # if none then height same 
      elif self.left is None and self.right is None:
          self.height = 1
      #left child then self.right.height + 1 
      elif self.left is not None and self.right is None:
        self.height = self.left.height + 1
      #if children then update height 
      elif self.left is None and self.right is not None:
        self.height = self.right.height + 1
    #take height of greater value 
      elif self.left.height > self.right.height:
          self.height = self.left.height + 1
    #right.height > left
      elif self.right.height > self.left.height:
          self.height = self.right.height + 1


  def __init__(self):
    #complete initiliziation 
    #root --> None
    self.__root = None
   
    
  def __find_balance(self, t):
    
      #if t.left child is None and t.right return 0
      if t.left is None and t.right is None:
          return 0
      #unless t's right child is 1 and t.left is none
      elif t.left is None and t.right.height is 1:
          #return 1
          return 1 
      #t's left child none t.right child 2
      elif t.left is None and t.right.height is 2:
        #return 2 
          return 2
    # t's left child height one and t's right is None
      elif t.left.height is 1 and t.right is None:
        # return -1 
          return -1
      #t's left child height 2 and t's right is none
      elif t.left.height is 2 and t.right is None:
          #return -2 
          return -2
      #otherwise return the balance of t.right - t.left 
      else:
          return t.right.height - t.left.height

     ## insert element ## 
  
  def insert_element(self, value):
    #self.__root = ___ (value, self.__root) update root in public
    self.__root = self.__recursive_insert(value, self.__root)

  def __rotate_right(self, t):
      # set temporary node --> t's left child right child
      temp_node = t.left.right
      #set new to t's left
      new_node = t.left
      #t.left.right --> t
      t.left.right = t
      #t.left = temp_node 
      t.left = temp_node
      #now return to new node 
      return new_node

  def __rotate_left(self, t):
      #opposite of right 
      temp_node = t.right.left
      new_node = t.right
      t.right.left = t
      t.right = temp_node
      #return new
      return new_node

  def __balance(self, t):
      #if t is not None then we proceed 
      if t is not None:
          # balance is 0, then fine return t as balance
          if self.__find_balance(t) is 0:
              return t
          #if balance is 1 or -1 then return balance cause allowed
          elif self.__find_balance(t) is 1 or self.__find_balance(t) is -1:
              return t
          #otherwise, four cases
          else:
              #balance is -2 so left heavy
              if self.__find_balance(t) is -2:
                #cases:
                #-1, then single rotation, right 
                if self.__find_balance(t.left) is -1:
                    t.height = t.height - 2
                    return self.__rotate_right(t)
                #0, then single rotation right 
                #child height 0
                elif self.__find_balance(t.left) is 0:
                  t.height = t.height - 1
                  t.left.height += + 1
                  #rotate right 
                  return self.__rotate_right(t)
                #double rotation now
                #elif find balance (t.left )== 1
                elif self.__find_balance(t.left) is 1:
                   #t's left child height is t.left.height -1
                    t.left.height = t.left.height - 1
                    #t.left.right.height +=1
                    t.left.right.height += 1
                    #rotate left 
                    t.left = self.__rotate_left(t.left)
                    t.height = t.height - 1
                    #rertun right rotation
                    return self.__rotate_right(t)
              #right heavy rotations
              #find balance == 2 
              elif self.__find_balance(t) is 2:
                  #child is 1 
                  if self.__find_balance(t.right) == 1:
                      #subtract 2 
                      t.height -= 2
                      #return left rotation 
                      return self.__rotate_left(t)
                  #double rotation
                  elif self.__find_balance(t.right) is -1:
                      t.right.height -= 1
                      t.right.left.height += 1
                      #right rotation
                      t.right = self.__rotate_right(t.right)
                      t.height -= 2
                      #return left rotation
                      return self.__rotate_left(t)

  def __recursive_insert(self, value, t):
    # Insert the value specified into the tree at the correct
    # location based on "less is left; greater is right" binary
    # search tree ordering. If the value is already contained in
    # the tree, raise a ValueError. 
    
    # if t is none then t.height = 1 and return 
    if t is None:
      t = self.__BST_Node(value)
      t.height = 1
      return self.__balance(t)
    
    #value error case
    if value is t.value:
      raise ValueError
    
    #unless the value is less (less is left)
    elif value < t.value:
      t.left = self.__recursive_insert(value, t.left)
      t.update_height(t)
      #return

      return self.__balance(t)
    
    #unless the values is greater than (greater is right)
    elif value > t.value:
      t.right = self.__recursive_insert(value, t.right)
      t.update_height(t)
      #return

      return self.__balance(t)
  
    ## remove element ##

  def __right_minimum(self, cell):
    #find the right minimum 
    # cell --> right
    cell = cell.right
    #enter while loop, while cell.left is not none keeps going through left until breaks
    while cell.left is not None:
      cell = cell.left
    #breaks and finds minimum, return
    return cell
  
  def remove_element(self, value): 
    #self.__root --> (value, self.__root)
    #update root in public
    self.__root = self.__recursive_remove(value, self.__root)

  def __recursive_remove(self, value, t):
    # Remove the value specified from the tree, raising a ValueError
    # if the value isn't found. When a replacement value is necessary,
    # select the minimum value to the from the right as this element's
    # replacement. Take note of when to move a node reference and when
    #value error case 
    if t is None:
      raise ValueError
    #if t.value is x 
    if t.value is value:
      #if t.left is not equal to none and t right not none, so they have children then
      if t.left is not None and t.right is not None:
        #mright minimum
        Minimum = self.__right_minimum(t)
        #remove minimum value
        self.__recursive_remove(Minimum.value, t)
        #t.value --> minimum value
        t.value = Minimum.value
        #update height function to track new height 
        t.update_height(t)
      
      #unless there are zero children, return none
      elif t.right is None and t.left is None:
        t.height = 0
        t = None
        return
      
      else:
        if t.right is None:
          t = t.left
        if t.left is None:
          t = t.right 
      #update the height 
      t.update_height(t)
      #RETURN 
      return self.__balance(t)
    # if x < t's value
    elif value < t.value:
      #update t's left child to be the return value of remove x from t.left
      t.left = self.__recursive_remove(value, t.left)
      #update height
      t.update_height(t)

      return self.__balance(t)
  
    #if x > t's value 
    elif value > t.value:
      # update t's right child to be the return value of removing x from t.right 
      t.right = self.__recursive_remove(value, t.right)
      
      #update height 
      t.update_height(t)
      #return t 
      return self.__balance(t)

  ## in order, pre order, post order functions ##
   
  def __recursive_in_order(self, t):
    #initialize value
    value = ''
    if t is not None:
      #parse the tree all the way through to fullest left side of tree
      value = value + str(self.__recursive_in_order(t.left))
      #add value of node to original 
      value = value + ' ' + str(t.value) + ',' 
      #check right side to print out everything in order
      value = value + str(self.__recursive_in_order(t.right))
    #return
    return value

  def in_order(self):
    #helper function calling recurisve in order function with the node to begin the method from
    #continously lower function until it returns to the first node
    value = '[' + self.__recursive_in_order(self.__root)[:-1] + ' ]'
    return value
  
  def __recursive_pre_order(self, t):
    #initiliaze value 
    value = ''
    if t is not None:
      # goes from entire left subtree, goes to root node, then goes to right subtree
      value = value + ' ' + str(t.value) + ','
      #left
      value = value + str(self.__recursive_pre_order(t.left))
      #right
      value = value + str(self.__recursive_pre_order(t.right))
  #return value 
    return value

  def pre_order(self):
    #helper
    value = '[' + self.__recursive_pre_order(self.__root)[:-1] + ' ]'
    return value

  def __recursive_post_order(self, t):
    #initiliaze
    value = ''
    if t is not None:
      #goes through entire left subtree, entire right subtree, then visits node last
      value = value + str(self.__recursive_post_order(t.left))
      #right
      value = value + str(self.__recursive_post_order(t.right)) 
      value = value + ' ' + str(t.value) + ','
    #return value 
    return value 

  def post_order(self):
    #helper 
    value = '[' + self.__recursive_post_order(self.__root)[:-1] + ' ]'
    #return
    return value


  def get_height(self):
    # return an integer that represents the height of the tree.
    # assume that an empty tree has height 0 and a tree with one
    # node has height 1. This method must operate in constant time
    if self.__root is None:
      return 0
      #else return 
    else:
      return self.__root.height

  def __str__(self):
    return self.in_order()


## to list for fraction ## 

  def to_list(self):
    # if the root is None then return []
      if self.__root is None:
          return []
          #recursively return
      return self.__r_to_list(self.__root)

  def __r_to_list(self, t):
    #if t None
      if t is None:
        #return
          return []
          #self.__r_to_list(t.left) + t.value + right (order of appearance in to_list fraction )
      return self.__r_to_list(t.left)+[t.value]+self.__r_to_list(t.right)


if __name__ == '__main__':
    test = Binary_Search_Tree()
    test.insert_element(10)
    test.insert_element(5)
    test.insert_element(15)
    test.insert_element(23)
    test.insert_element(40) 
    test.insert_element(50)
    print(test)
    print(test.post_order()) #checking double rotation
    print(test.pre_order())
    print(test.get_height()) #should be 3 





