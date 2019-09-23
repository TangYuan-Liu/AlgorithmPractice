# C language Tools

### Find min in three numbers
<pre><code>
int min_func(int a, int b, int c)
{
    int min;
    return c < (min = a < b ? a:b) ? c:min;
}
</code></pre>

### Find max in three numbers
<pre><code>
int max_func(int a, int b, int c)
{
    int max;
    return c > (max = a > b ? a:b) ? c:max;
}
</code></pre>