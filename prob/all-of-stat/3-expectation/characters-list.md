distribution| density / mass | expectation| variance|link / remark|[[characteristic-function]]
-|-|-|-|-|-
Point mass at $a$|$1_{n=a}$|$a$|$0$||$e^{ita}$
Bernoulli($p$)|$p^{n}(1-p)^{1-n}$|$p$|$p(1-p)$|[[bernoulli-binom#bernoulli]]|$pe^{it}+(1-p)$
Binomial($m$, $p$)|$\binom{m}{n}p^{n}(1-p)^{m-n}$|$mp$|$mp(1-p)$|[[bernoulli-binom#binom]]|$(pe^{it}+(1-p))^m$
Geometric($p$)|$(1-p)^{n-1}p$|$\frac{1}{p}$|$\frac{1-p}{p^2}$|[[nega-binom#geometric]]|$\frac{p}{1-(1-p)e^{it}}$
Poisson($\lambda$)|$\frac{\lambda^{n}e^{-\lambda}}{n!}$|$\lambda$|$\lambda$|[[poisson]]|$e^{\lambda(e^{it}-1)}$
Uniform($a$, $b$)|$\frac{1}{b-a}$|$\frac{a+b}{2}$|$\frac{(b-a)^2}{12}$|[[uniform-distribution]]|$\frac{e^{itb}-e^{ita}}{it(b-a)}$
Normal($\mu$, $\sigma^2$)|$\frac {1}{\sqrt{2\pi} \sigma} e^{-\frac{(x-\mu)^2}{2\sigma^2}}$|$\mu$|$\sigma^2$|[[normal]]|$e^{i\mu t-\frac{1}{2}\sigma^2t^2}$
Exponential($\beta$)|$\frac{1}{\beta}e^{-\frac{x}{\beta}}$|$\beta$|$\beta^2$|[[gamma-distribution#指数分布]]|$\frac{1}{1-it\beta}$
Gamma($\alpha$, $\beta$)|$\frac{1}{\beta^{\alpha}\Gamma(\alpha)}x^{\alpha-1}e^{-\frac{x}{\beta}}$|$\alpha\beta$|$\alpha\beta^2$|[[gamma-distribution]]|$(\frac{1}{1-it\beta})^\alpha$
Beta($\alpha$, $\beta$)|$\frac{\Gamma(\alpha+\beta)}{\Gamma(\alpha)\Gamma(\beta)}x^{\alpha-1}(1-x)^{\beta-1}$|$\frac{\alpha}{\alpha+\beta}$|$\frac{\alpha\beta}{(\alpha+\beta)^2(\alpha+\beta+1)}$|[[beta-distribution]]|
$t_\nu$|$\frac{\Gamma(\frac{\nu+1}{2})}{\sqrt{\nu\pi}\Gamma(\frac{\nu}{2})}(1+\frac{x^2}{\nu})^{-\frac{\nu+1}{2}}$ (if $\nu>1$)|$0$ (if $\nu>1$)|$\frac{\nu}{\nu-2}$ (if $\nu>2$)|[[t-distribution]]|
$\chi^2_n$|$\frac{1}{2^{\frac{n}{2}}\Gamma(\frac{n}{2})}x^{\frac{n}{2}-1}e^{-\frac{x}{2}}$|$n$|$2n$|[[chi-square]]|$(1-2it)^{-\frac{n}{2}}$
Multinomial($n$, $p$)|$\frac{n!}{x_1!x_2!...x_k!}p_1^{x_1}p_2^{x_2}...p_k^{x_k}$|$np$|see below|[[bernoulli-binom#multi]]
Multivariate Normal($\mu$, $\Sigma$)|$\frac{1}{(2\pi)^{k/2}\|\Sigma\|^{1/2}}\exp\{-\frac{1}{2}(x-\mu)^T\Sigma^{-1}(x-\mu)\}$|$\mu$|$\Sigma$|[[multi-normal]]