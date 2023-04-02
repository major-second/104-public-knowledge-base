distribution| density / mass | expectation| variance|link / remark
-|-|-|-|-
Point mass at $a$|$1_{n=a}$|$a$|$0$
Bernoulli($p$)|$p^{n}(1-p)^{1-n}$|$p$|$p(1-p)$|[[bernoulli-binom]]
Binomial($n$, $p$)|$\binom{n}{n}p^{n}(1-p)^{n-n}$|$np$|$np(1-p)$|[[bernoulli-binom]], [[可加性]]
Geometric($p$)|$(1-p)^{n-1}p$|$\frac{1}{p}$|$\frac{1-p}{p^2}$|[[nega-binom]]
Poisson($\lambda$)|$\frac{\lambda^{n}e^{-\lambda}}{n!}$|$\lambda$|$\lambda$|[[poisson]]
Uniform($a$, $b$)|$\frac{1}{b-a}$|$\frac{a+b}{2}$|$\frac{(b-a)^2}{12}$|[[variance]] = $E(X^2) -EX^2=1/3-1/4=1/12$
Normal($\mu$, $\sigma^2$)|$\frac {1}{\sqrt{2\pi} \sigma} e^{-\frac{(x-\mu)^2}{2\sigma^2}}$|$\mu$|$\sigma^2$
Exponential($\beta$)|$\frac{1}{\beta}e^{-\frac{x}{\beta}}$|$\beta$|$\beta^2$
Gamma($\alpha$, $\beta$)|$\frac{1}{\beta^{\alpha}\Gamma(\alpha)}x^{\alpha-1}e^{-\frac{x}{\beta}}$|$\alpha\beta$|$\alpha\beta^2$|[[distribution/gamma]]. [[可加性]], [[linear-transform]]用于求均值方差
Beta($\alpha$, $\beta$)|$\frac{\Gamma(\alpha+\beta)}{\Gamma(\alpha)\Gamma(\beta)}x^{\alpha-1}(1-x)^{\beta-1}$|$\frac{\alpha}{\alpha+\beta}$|$\frac{\alpha\beta}{(\alpha+\beta)^2(\alpha+\beta+1)}$
$t_\nu$|$\frac{\Gamma(\frac{\nu+1}{2})}{\sqrt{\nu\pi}\Gamma(\frac{\nu}{2})}(1+\frac{x^2}{\nu})^{-\frac{\nu+1}{2}}$ (if $\nu>1$)|$0$ (if $\nu>1$)|$\frac{\nu}{\nu-2}$ (if $\nu>2$)
$\chi^2_n$|$\frac{1}{2^{\frac{n}{2}}\Gamma(\frac{n}{2})}x^{\frac{n}{2}-1}e^{-\frac{x}{2}}$|$n$|$2n$
Multinomial($n$, $p$)|$\frac{n!}{x_1!x_2!...x_k!}p_1^{x_1}p_2^{x_2}...p_k^{x_k}$|$np$|see below|
Multivariate Normal($\mu$, $\Sigma$)|$\frac{1}{(2\pi)^{k/2}\|\Sigma\|^{1/2}}\exp\{-\frac{1}{2}(x-\mu)^T\Sigma^{-1}(x-\mu)\}$|$\mu$|$\Sigma$|[[multi-normal]]

本书看到这todo