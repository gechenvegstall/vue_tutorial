import models

# 添加
def info():
    user_info=models.UserInfo(
        name="cgx",
        age=18
    )
    models.session.add(user_info)
    models.session.commit()
    # 关闭链接，可使用session.remove()，它将回收该链接
    models.session.close()
# 批量添加
def info_all():
    user_info1=models.UserInfo(
        name="cgxx",
        age=18
    )
    user_info2=models.UserInfo(
        name="cgxxx",
        age=18
    )
    models.session.add_all(
        (user_info2,user_info2)
    )
    models.session.commit()
    models.session.close()
# 修改
"""# 正确写法1：直接设置新值（替换原有值）
models.session.query(models.UserInfo).filter_by(id=1).update({"name": "CGXXXX"})

# 正确写法2：基于原有值修改（如拼接）
models.session.query(models.UserInfo).filter_by(id=1).update({"name": models.UserInfo.name + "CGXXXX"})
在原值基础上做更改的操作，所以必须添加:synchronize_session=False"""
def updata():
    models.session.query(models.UserInfo).filter_by(id=1).update({"name":'CGXXXX'})
    models.session.commit()
    models.session.close()

# 删除
def delete():
    models.session.query(models.UserInfo).filter_by(name='cgxx').delete()
    models.session.commit()
    models.session.remove()

# 查询
"""
all()方法将返回一个列表，内部包裹着每一行的记录对象
result = models.session.query(
    models.UserInfo.id,
    models.UserInfo.name,
    models.UserInfo.age
).all()
print(result)
# [(1, 'Jackson', 19), (2, 'Tom', 19)]
只拿第一条记录，first()方法将返回单条记录对象
"""
def select():
    user=models.session.query(models.UserInfo).all()
    for u in user:
        print(u)
    models.session.remove()
select()

"""通过字段的label()方法，我们可以为它取一个别名"""