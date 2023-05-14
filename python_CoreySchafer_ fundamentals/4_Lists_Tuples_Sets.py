# //////////////////////////
# courses = ['History', 'Math', 'Physics', 'CompSci']
# print(courses)
# print(len(courses))
# print(courses[0])
# print(courses[-1])
# print(courses[0:2])
# print(courses[:2])
# print(courses[2:])

# # //////////////////////////
# courses = ['History', 'Math', 'Physics', 'CompSci']
# courses.append('Art')

# print(courses)

# # //////////////////////////
# courses = ['History', 'Math', 'Physics', 'CompSci']
# courses_2 = ['Art', 'Education']

# courses.insert(0, courses_2)

# print(courses)

# # //////////////////////////
# courses = ['History', 'Math', 'Physics', 'CompSci']
# courses_2 = ['Art', 'Education']

# courses.extend(courses_2)

# print(courses)

# # //////////////////////////
# courses = ['History', 'Math', 'Physics', 'CompSci']
# courses_2 = ['Art', 'Education']

# courses.append(courses_2)

# print(courses)

# # //////////////////////////
# courses = ['History', 'Math', 'Physics', 'CompSci']

# courses.remove('Math')

# print(courses)

# # //////////////////////////
# courses = ['History', 'Math', 'Physics', 'CompSci']

# # courses.pop()
# # print(courses)

# popped = courses.pop()
# print(popped)

# //////////////////////////
# courses = ['History', 'Math', 'Physics', 'CompSci']
# courses.sort()
# print(courses)

# nums = [5, 4, 2, 8, 3]
# nums.sort()
# print(nums)

# //////////////////////////
# courses = ['History', 'Math', 'Physics', 'CompSci']
# courses.sort(reverse=True)
# print(courses)

# nums = [5, 4, 2, 8, 3]
# nums.sort(reverse=True)
# print(nums)


# //////////////////////////
# courses = ['History', 'Math', 'Physics', 'CompSci']
# sorted_courses = sorted(courses)
# print(sorted_courses)

# nums = [5, 4, 2, 8, 3]

# print(min(nums))
# print(max(nums))
# print(sum(nums))

# # //////////////////////////
# courses = ['History', 'Math', 'Physics', 'CompSci']

# # print(courses.index('CompSci'))
# # print('Art' in courses)
# # print('Math' in courses)

# # for course in courses:
# #     print(course)

# # for index, course in enumerate(courses):
# #     print(index, course)
    
# for index, course in enumerate(courses, start=1):
#     print(index, course)


# # # //////////////////////////
# courses = ['History', 'Math', 'Physics', 'CompSci']

# course_str = ' - '.join(courses)
# print(course_str)

# new_list = course_str.split(' - ')
# print(new_list)

# # //////////// Mutable  //////////////
# list_1 = ['History', 'Math', 'Physics', 'CompSci']

# list_2 = list_1

# print(list_1)
# print(list_2)

# list_1[0] = 'Art'

# print(list_1)
# print(list_2)


#  # //////////// Immutable Tuple //////////////
# tuple_1 = ('History', 'Math', 'Physics', 'CompSci')

# tuple_2 = tuple_1

# print(tuple_1)
# print(tuple_2)

# tuple_1[0] = 'Art'

# print(tuple_2)
# print(tuple_1)

#  # ////////////  Sets //////////////
# cs_courses = {'History', 'Math', 'Physics', 'CompSci'}

# print(cs_courses)


# # ////////////  Sets //////////////
# cs_courses = {'History', 'Math', 'Physics', 'CompSci', 'Math'}

# print(cs_courses)

# print('Math' in cs_courses)

# ////////////  Sets //////////////
# cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
# art_courses = {'History', 'Math', 'Art', 'Design'}

# print(cs_courses.intersection(art_courses))
# print(cs_courses.difference(art_courses))
# print(cs_courses.union(art_courses))







