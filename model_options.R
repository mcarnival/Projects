# model options

##library 
library(tidyverse)
library(tidymodels)
library(brant)
library(boot)
library(janitor)
library(haven)
library(classpackage)
library(glmtoolbox)
library(ggthemes)
library(car)
library(skimr)
library(broom)


#_______________________________________________________________________________
# linear regression continuous gaussian
m <- glm([outcome] ~ [pred1] + [pred2] + [pred3] + ..., 
         data = [dataset],
         family = "gaussian")

## continuous predictor
m <- glm([outcome] ~ [pred1] + [pred2] + [pred3] + ..., 
         data = [dataset],
         family = "gaussian")

## categorical predictor
library(fastDummies)
data <- data %>% # overwrite data
  dummy_cols(select_columns = c("cols")) # create indicators for months
m <- glm([outcome] ~ [pred1] + [pred2] + [pred3] + ..., 
         data = [dataset],
         family = "gaussian")

##don't forget to anova check on the residuals as well as the histo plot
## make sure to use Anova(m, type =30) for c > 2
#_______________________________________________________________________________
## gamma distribution

m <- glm([outcome] ~ [pred_1] + [pred_2] + ... + [pred_k], 
         data = [dataset], 
         family = Gamma(link = "log"))

#positive AND right skewed histogram

#_______________________________________________________________________________
#binary logistic regression
m <- glm([outcome] ~ [pred_1] + [pred_2] + ... + [pred_k], 
         data = [dataset], 
         family = "binomial")



#_______________________________________________________________________________
#ordinal logistic regression: some kind of order in the groups
m <- MASS::polr(outcome ~ term1 + term2 + ... + termk,
                data = dataset_name, 
                Hess = TRUE)
#check for proportional odds brant's test


#_______________________________________________________________________________
#nominal logistic regression: random
library(nnet)
m <- multinom(outcome ~ var_1 + var_2 + ... + var_k, 
              data = dataset)

#_______________________________________________________________________________
# poisson distribution: count data modeling
m <- glm(outcome ~ var_1 + var_2 + ... + var_k, 
         family="poisson",
         data=dataset)
#check for var = mean for variable being model. if not, step to negative binomial
#IRR: incident rate ratio
#_______________________________________________________________________________
#negative binomial
m <- MASS:glm.nb(outcome ~ var_1 + var_2 + ... + var_k, 
                 data=dataset)


#_______________________________________________________________________________
#cross-validation
# contstruct training and validation datasets
m1v <- lm(body_mass_g ~ flipper_length_mm, data = training)
m2v <- lm(body_mass_g ~ flipper_length_mm + flipper2, data = training)


# validation set approach
validation <- validation %>% 
  mutate(yhat_m1 = predict(m1v, newdata = validation),
         yhat_m2 = predict(m2v, newdata = validation)) %>%
  mutate(sqerr_m1 = (yhat_m1 - body_mass_g)^2,
         sqerr_m2 = (yhat_m2 - body_mass_g)^2) %>%
  relocate(obs, body_mass_g, yhat_m1, sqerr_m1, yhat_m2, sqerr_m2)

mean(validation$sqerr_m1, na.rm = TRUE)
mean(validation$sqerr_m2, na.rm = TRUE)



#leave one cross
# leave-one-out cross-validation
set.seed(6714)
m1 <- glm(body_mass_g ~ flipper_length_mm, data = data)
cv.glm(data, m1)$delta

set.seed(19571)
m2 <- glm(body_mass_g ~ flipper_length_mm + flipper2, data = data)
cv.glm(data, m2)$delta


# k-fold cross
set.seed(75628)
m1 <- glm(body_mass_g ~ flipper_length_mm, data = data)
cv.glm(data, m1, K=10)$delta

set.seed(24681)
m2 <- glm(body_mass_g ~ flipper_length_mm + flipper2, data = data)
cv.glm(data, m2, K=10)$delta

