/* 어떤 번호가 다른 번호의 접두어인 경우가 있으면 false
    * 그렇지 않으면 true를 리턴
*
*/
// 해결책 1) 2중  loop를 통해 서로가 서로의 접두어인지 전부 확인
// 해결책 2) 해시를 통해 접두어가 존재하는지를 확인하는 방법
import java.util.Arrays;

class Solution {
    public boolean solution(String[] phoneBook) {
        // 1. phoneBook을 sorting한다.
        Arrays.sort(phoneBook);

        // 2. 1중 Loop을 돌며 앞 번호가 뒷 번호의 접두어인지 확인한다.
        for (int i = 0; i < phoneBook.length - 1; i++)
            if (phoneBook[i + 1].startsWith(phoneBook[i]))
                return false;

        // 3. 여기까지 오면 접두어가 없다는 것이다.
        return true;
    }
}
/*
import java.util.HashMap;
import java.util.Map;

class Solution {
    public boolean solution(String[] phoneBook) {
        // 1. HashMap을 선언한다.
        Map<String, Integer> map = new HashMap<>();

        // 2. 모든 전화번호를 HashMap에 넣는다.
        for (int i = 0; i < phoneBook.length; i++)
            map.put(phoneBook[i], i);

        // 3. 모든 전화번호의 substring이 HashMap에 존재하는지 확인한다.
        for (int i = 0; i < phoneBook.length; i++)
            for (int j = 0; j < phoneBook[i].length(); j++)
                if (map.containsKey(phoneBook[i].substring(0, j)))
                    return false;

        return true;
    }
}
*/