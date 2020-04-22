service test

{

string GetSysVer()

#一个获取系统版本的方法，返回给socket一个字符串

string FileTransfer(1:string filename, 2:binary content )

#传送文件的方法，入口参数为string类型的文件名和二进制流类型的文件内容，方法将给socket一个字符串类型的返回值，如果你需要传送结构体，可以在Service外面定义struct File{1:string filename,2:binary content,3:i64:filelen...}等等，然后用list类型赋值给入口参数，例如string FileTransfer(1:list transfer)

bool FileExists(1:string filename)

#检查server端指定文件是否存在，返回布尔
}

