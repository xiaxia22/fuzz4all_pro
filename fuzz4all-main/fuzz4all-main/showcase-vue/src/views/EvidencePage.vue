<script setup>
import { ref, nextTick } from 'vue'
import CodeBlock from '../components/CodeBlock.vue'
import Prism from 'prismjs'
import 'prismjs/components/prism-java'

const activeTab = ref('ev-code')

function switchTab (id) {
  activeTab.value = id
  nextTick(() => Prism.highlightAll())
}

const safeCode = `import java.net.URI;

public class UriManipulations {
  public static void main(String[] args) {
    test("http://user:pass@host:8080/p?t=1#s");
    testRelative("http://example.com", "path/to/res");
    testEdge("///localhost//path///");
  }
  static void test(String s) {
    try {
      URI u = new URI(s);
      System.out.println(u.normalize());
      System.out.println(u.getScheme() + "://" + u.getHost());
    } catch (Exception e) { e.printStackTrace(); }
  }
  static void testRelative(String base, String rel) {
    try {
      URI resolved = new URI(base).resolve(new URI(rel));
      System.out.println(resolved);
    } catch (Exception e) { e.printStackTrace(); }
  }
  static void testEdge(String s) {
    try { System.out.println(new URI(s).toASCIIString()); }
    catch (Exception e) { e.printStackTrace(); }
  }
}`

const failCode = `import javax.crypto.Cipher;
import javax.crypto.spec.SecretKeySpec;

public class CipherTest {
  public static void main(String[] args) {

    // ❌ 所有Cipher方法抛受检异常，但代码无 try-catch
    Cipher c = Cipher.getInstance("AES/ECB/PKCS5Padding");
    // ^ error: unreported exception NoSuchPaddingException

    SecretKeySpec ks = new SecretKeySpec(new byte[16], "AES");
    c.init(Cipher.ENCRYPT_MODE, ks);
    // ^ error: unreported exception InvalidKeyException

    byte[] out = c.doFinal("Hello".getBytes());
    // ^ error: unreported exception IllegalBlockSizeException
  }
}`

const seedCode = `import java.time.Duration;

public class DurationTest {
  public static void main(String[] args) {
    Duration d1 = Duration.ofMinutes(10);
    Duration d2 = Duration.ofSeconds(30);
    Duration total = d1.plus(d2);
    System.out.println(total.toSeconds()); // 630
    System.out.println(total.isNegative()); // false
    System.out.println(total.abs());
  }
}`

const mutCode = `import java.time.Duration;

public class DurationTest {
  public static void main(String[] args) {
    // ← 注入负值边界（time_duration_sign_mutation）
    Duration d1 = Duration.ofMinutes(-1L);
    // ← 极端边界（time_epoch_boundary_mutation）
    Duration d2 = Duration.ofSeconds(Long.MIN_VALUE);
    Duration total = d1.plus(d2);
    System.out.println(total.toSeconds());
    System.out.println(total.isNegative());
    // ← 额外epoch边界测试
    Duration epoch = Duration.ofSeconds(0L);
    System.out.println(epoch.isZero());
  }
}`
</script>

<template>
  <div class="page-inner">
    <div class="page-header">
      <div class="page-title">流程证据</div>
      <div class="page-subtitle">系统运行留下的完整痕迹：提示词生成 → 错误归类 → 规则学习 → 代码对比</div>
    </div>

    <div class="tabs">
      <button class="tab-btn" :class="{ active: activeTab === 'ev-code' }" @click="switchTab('ev-code')">代码对比</button>
      <button class="tab-btn" :class="{ active: activeTab === 'ev-rules' }" @click="switchTab('ev-rules')">规则学习</button>
      <button class="tab-btn" :class="{ active: activeTab === 'ev-prompt' }" @click="switchTab('ev-prompt')">提示词演化</button>
      <button class="tab-btn" :class="{ active: activeTab === 'ev-mut' }" @click="switchTab('ev-mut')">变异示例</button>
    </div>

    <!-- 代码对比 -->
    <div v-show="activeTab === 'ev-code'">
      <div class="g2">
        <div>
          <CodeBlock
            title="java.net.URI — 编译通过样本"
            badge-cls="b-safe"
            badge-text="SAFE"
            :code="safeCode"
          />
          <div class="info-box info-green" style="margin-top:10px">
            ✅ 所有 URI 操作正确包裹在 try-catch 中，符合API使用规范
          </div>
        </div>
        <div>
          <CodeBlock
            title="javax.crypto.Cipher — 典型失败（已修复）"
            badge-cls="b-fail"
            badge-text="FAILURE"
            :code="failCode"
          />
          <div class="info-box info-orange" style="margin-top:10px">
            ⚠️ 根本原因：旧版系统仅检测 IOException，无法识别 Cipher 的受检异常，
            反馈规则无法生成。整改后通用受检异常检测修复此问题。
          </div>
        </div>
      </div>
    </div>

    <!-- 规则学习 -->
    <div v-show="activeTab === 'ev-rules'">
      <div class="g2" style="margin-bottom:16px">
        <div class="card">
          <div class="card-title">URI 类别 — 自动学习规则</div>
          <ul class="rule-list">
            <li>Avoid ambiguous imports; keep imports minimal and consistent.</li>
            <li>Declare all variables before using them; do not reference helper objects not created in the same method.</li>
            <li>Use only documented public methods of URI.</li>
            <li>Keep return types consistent with documented API contracts.</li>
            <li>For URI, keep endpoint objects aligned with the documented lifecycle.</li>
          </ul>
        </div>
        <div class="card">
          <div class="card-title">ManagementFactory — 自动学习规则</div>
          <ul class="rule-list">
            <li>Call documented query methods on concrete MXBean interfaces; do not invent generic bean super-types.</li>
            <li>Prefer static factory methods that return standard MXBeans or MBeanServer handles.</li>
            <li>Handle checked exceptions for ObjectName construction with try/catch.</li>
            <li>Use only standard javax.management types; do not invent proxy class names.</li>
          </ul>
        </div>
      </div>
      <div class="card">
        <div class="card-title">规则生成管道</div>
        <div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(180px,1fr));gap:10px;font-size:12.5px">
          <div style="padding:10px;background:var(--primary-xl);border-radius:7px;border-left:3px solid var(--primary)">
            <div style="font-weight:600;color:var(--primary);margin-bottom:3px">① 捕获错误</div>
            <div style="color:var(--muted)">javac输出 → extract_javac_error_categories() → 识别25+种错误类别</div>
          </div>
          <div style="padding:10px;background:var(--primary-xl);border-radius:7px;border-left:3px solid var(--primary)">
            <div style="font-weight:600;color:var(--primary);margin-bottom:3px">② 生成规则</div>
            <div style="color:var(--muted)">map_error_categories_to_rules() → 结合API名称和领域标签生成自然语言规则</div>
          </div>
          <div style="padding:10px;background:var(--primary-xl);border-radius:7px;border-left:3px solid var(--primary)">
            <div style="font-weight:600;color:var(--primary);margin-bottom:3px">③ 频次排序</div>
            <div style="color:var(--muted)">_merge_failure_rules() → 按频次排序保留 Top-5 规则</div>
          </div>
          <div style="padding:10px;background:var(--primary-xl);border-radius:7px;border-left:3px solid var(--primary)">
            <div style="font-weight:600;color:var(--primary);margin-bottom:3px">④ 注入提示词</div>
            <div style="color:var(--muted)">"Avoid these known compiler mistakes" 注入下一轮提示词</div>
          </div>
        </div>
      </div>
    </div>

    <!-- 提示词演化 -->
    <div v-show="activeTab === 'ev-prompt'">
      <div class="g2">
        <div class="card">
          <div class="card-title">初始提示词（Auto-Prompting 生成）</div>
          <pre style="background:var(--surface2);border:1px solid var(--border);border-radius:7px;padding:12px;
            font-size:12px;color:var(--text);white-space:pre-wrap;max-height:280px;overflow:auto;font-family:monospace">/* Please create a very short Java program
   that uses java.net.URI in diverse and
   tricky ways.

   Focus on:
   - Parsing URIs with edge-case schemes
   - Normalizing relative/absolute URIs
   - Testing boundary conditions
   - Proper exception handling

   Use only standard JDK classes. */

import java.net.URI;</pre>
        </div>
        <div class="card">
          <div class="card-title">运行时刷新后提示词（含反馈规则）</div>
          <pre style="background:var(--surface2);border:1px solid var(--border);border-radius:7px;padding:12px;
            font-size:12px;color:var(--text);white-space:pre-wrap;max-height:280px;overflow:auto;font-family:monospace">/* [Base Prompt] Please create a short Java
   program using java.net.URI. */

/* Avoid these known compiler mistakes:
   - Do not call undocumented methods on URI
   - Avoid ambiguous imports
   - Declare all variables before use
   - Use only documented public methods
   - Keep return types consistent */

/* Recent valid examples to imitate:
   Example 1:
   ```java
   try {
     URI u = new URI("http://example.com");
     System.out.println(u.normalize());
   } catch (Exception e) { e.printStackTrace(); }
   ``` */

import java.net.URI;</pre>
        </div>
      </div>
      <div class="info-box info-green" style="margin-top:12px">
        URI 类别提示词评分：初始 <strong>8 分</strong> → 两轮刷新后 <strong>12 分</strong>，编译通过率达 <strong>72.7%</strong>（10 类最高）
      </div>
    </div>

    <!-- 变异示例 -->
    <div v-show="activeTab === 'ev-mut'">
      <div class="g2">
        <div class="card">
          <div class="card-title">原始 Seed（LLM 生成）</div>
          <CodeBlock :code="seedCode" />
        </div>
        <div class="card">
          <div class="card-title">变异后（time_duration_sign_mutation 算子）</div>
          <CodeBlock :code="mutCode" />
          <div style="color:var(--muted);font-size:12px;margin-top:8px">
            算子 <code>time_duration_sign_mutation</code> 注入了负值时长和 <code>Long.MIN_VALUE</code> 极端边界，测试 Duration
            对边界输入的处理
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
