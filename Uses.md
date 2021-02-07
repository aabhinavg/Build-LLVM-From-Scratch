**Create C Programs**</br>
<span style="color:red">first.c</span>
<div class="highlight-c notranslate"><div class="highlight"><pre><span></span><span class="cp">#include</span> <span class="cpf">&lt;stdio.h&gt;</span><span class="cp"></span>
<span class="kt">int</span> <span class="nf">main</span><span class="p">()</span> <span class="p">{</span>
  <span class="n">printf</span><span class="p">(</span><span class="s">&quot;hello world</span><span class="se">\n</span><span class="s">&quot;</span><span class="p">);</span>
  <span class="k">return</span> <span class="mi">0</span><span class="p">;</span>
<span class="p">}</span>
</pre>
  
**Compile C file using Clang**
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="gp">% </span>clang hello.c -o hello
</pre></div>

**Convert C file to LLVM Bitcode**
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="gp">% </span>clang -O3 -emit-llvm hello.c -c -o hello.bc
</pre></div>
  <p>The -emit-llvm option can be used with the -S or -c options to emit an LLVM
