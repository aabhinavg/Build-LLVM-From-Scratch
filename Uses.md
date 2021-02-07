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
  <p class="first">Run the program in both forms. To run the program, use:</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="gp">% </span>./hello
</pre></div>
</div>
<p>and</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="gp">% </span>lli hello.bc
</pre></div>
</div>
  
**The second examples shows how to invoke the LLVM JIT**   </br>
<p class="first">Use the <code class="docutils literal notranslate"><span class="pre">llvm-dis</span></code> utility to take a look at the LLVM assembly code:</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="gp">% </span>llvm-dis &lt; hello.bc <span class="p">|</span> less
</pre></div>
</div>
</li>

**Compile the program to native assembly using the LLC code generator** 
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="gp">% </span>llc hello.bc -o hello.s
</pre></div>
</div>
</li>
