// "Replace IntStream.range().mapToLong() with collection.stream()" "false"

import java.util.ArrayList;
import java.util.List;
import java.util.stream.IntStream;

public class Test extends ArrayList<String> {
  public void test(List<Integer> list) {
    long[] arr = IntStream.range(0, list.size()).map<caret>ToLong(idx -> 5).toArray();
  }
}
