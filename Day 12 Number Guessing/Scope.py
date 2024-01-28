# # Local Scope
# def variable_value():
#     abc=2
#     return abc

# print(abc)
# print(variable_value())

# Global Scope

xyz=10
def apple():
    xyz=2
    print(xyz)
print(xyz)
apple()