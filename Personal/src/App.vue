<template>
    <div class="header">
        <header>
            <h1>欢迎来到我的网站</h1>
        </header>
    </div>
    <div class="nav">
        <nav>
            <ul>
                <li><router-link to="/home" class="nav-link">主页</router-link></li>
                <li><router-link to="" class="nav-link">文章浏览</router-link></li>
                <li><router-link to="" class="nav-link">文章发布</router-link></li>
                <li><router-link to="" class="nav-link">文章管理</router-link></li>
                <li><router-link to="" class="nav-link">用户管理</router-link></li>
                <li><router-link to="" class="nav-link">评论管理</router-link></li>
                <li><router-link to="" class="nav-link">标签管理</router-link></li>
                <li><router-link to="" class="nav-link">关于我们</router-link></li>
                <li><router-link to="/Login" class="nav-link">Login</router-link></li>
            </ul>
        </nav>
    </div>
    <div class="content">
        <router-view></router-view>
        <!-- <el-empty description="description" /> -->
    </div>
    <div class="footer">
        <footer>底部</footer>
    </div>
</template>

<style>
.header {
  position: fixed; 
  top: 0;  left: 0; right: 0;
  height: 60px;
  text-align: center; 
  background-color: #333;
    
}
.header h1 {
  color: white;
  font-size: 30px;
}
.footer {
  position: fixed; 
  bottom: 0; left: 0; right: 0;
  height: 30px;
  text-align: center; 
  background-color: #333;
  color: white;
}
nav {
  position: fixed;
  top: 60px; left: 0; right: 0;
  height: 30px;
  background-color: #f5f5f5;
  z-index: 1000;
}
nav ul {
  list-style-type: none;
  margin: 0;
  padding: 0;
  overflow: hidden;
  display: flex;
  justify-content: flex-end;
}
.nav-link {
  display: inline;
  margin-right: 70px;
  margin-left:70px;
  font-size: 20px;
  font-weight: bold;
  cursor: pointer;
  color: #0f0101;
}
.nav-link:hover {
  color: #07d5f5;
}
.nav-link:active {
  color: #011214;
}
</style>