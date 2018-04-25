import java.io.*;
import java.util.*;

class Main {
    static class CharTreeNode{
        int cnt = 0;
        CharTreeNode[] children = new CharTreeNode[26];
    }

    static class word_count {
        private String word;
        private int count;
        public int getCount() {
            return count;
        }
        public void setCount(int count) {
            this.count = count;
        }
        public String getWord() {
            return word;
        }
        public void setWord(String word) {
            this.word = word;
        }
    }

    static void geneCharTree(String text,CharTreeNode root){
        CharTreeNode p = root;
        char c = ' ';
        for(int i = 0; i < text.length(); ++i){
            c = text.charAt(i);
            if(c >= 'A' && c <= 'Z')
                c = (char)(c + 'a' - 'A');
            if(c >= 'a' && c <= 'z'){
                if(p.children[c-'a'] == null)
                    p.children[c-'a'] = new CharTreeNode();
                p = p.children[c-'a'];
            }
            else{
                p.cnt ++;
                p = root;
            }
        }
        if(c >= 'a' && c <= 'z')
            p.cnt ++;
    }

    static  void getWordCountFromCharTree(List<word_count> result,CharTreeNode p, char[] buffer, int length){
        for(int i = 0; i < 26; ++i){
            if(p.children[i] != null){
                buffer[length] = (char)(i + 'a');
                if(p.children[i].cnt > 0){
                    word_count wc = new word_count();
                    wc.setCount(p.children[i].cnt);
                    wc.setWord(String.valueOf(buffer, 0, length+1));
                    result.add(wc);
                }
                getWordCountFromCharTree(result,p.children[i],buffer,length+1);
            }
        }
    }

    static  void getWordCountFromCharTree(List<word_count> result,CharTreeNode p){
        getWordCountFromCharTree(result,p,new char[100],0);
    }

    static List<word_count> getWordCount(CharTreeNode root){
        List<word_count> result = new LinkedList<word_count>();
        getWordCountFromCharTree(result,root);
        Collections.sort(result, new Comparator(){
            public int compare(Object o1, Object o2) {
                word_count wc1 = (word_count)o1;
                word_count wc2 = (word_count)o2;
                return wc2.getCount() - wc1.getCount();
            }
        });
        return result;
    }

    static  void readTxtFile(String filePath,CharTreeNode root){
        try {
            String encoding="GBK";
            File file=new File(filePath);
            if(file.isFile() && file.exists()){
                InputStreamReader read = new InputStreamReader(
                        new FileInputStream(file),encoding);
                BufferedReader bufferedReader = new BufferedReader(read);
                String lineTxt = null;
                while((lineTxt = bufferedReader.readLine()) != null){
                    //System.out.println(lineTxt);
                    geneCharTree(lineTxt, root);
                }
                read.close();
            }else{
                System.out.println("找不到指定的文件"+filePath);
            }
        } catch (Exception e) {
            System.out.println("读取文件内容出错");
            e.printStackTrace();
        }
    }

    public static void main(String[] args) throws IOException{
        long startTime=System.currentTimeMillis();
        String filePath;
        CharTreeNode  root = new CharTreeNode();
        List<word_count> result = new LinkedList<word_count>();
        word_count wc;
        FileWriter  fw=null ;
        String str;
        int Count=10000;
        int i;
        for(i=1;i<=Count;i++)
        {
            filePath="D:\\workspace\\javaCode\\hadoop\\input\\Shakespeare"+i+".txt";
            readTxtFile(filePath,root);
        }
        result=getWordCount(root);
        Iterator<word_count> itr = result.iterator();
        fw=new FileWriter("D:\\workspace\\javaCode\\hadoop\\output\\5.txt");
        str=new String();

        while (itr.hasNext()) {
            wc=(word_count)itr.next();
       /*
       System.out.printf("%-20s            %d\n", wc.word,wc.count);
       */

            str=String.format("%-20s            %d\n", wc.word,wc.count);
            try {
                fw.write(str);
                fw.flush();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
        fw.close();
        long endTime=System.currentTimeMillis();
        System.out.println("程序运行时间： "+(endTime-startTime)+"ms");
    }
}

