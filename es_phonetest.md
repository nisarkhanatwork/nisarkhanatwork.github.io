## Expert Systems for hyperparameter tuning and “telephone test”
![](es/expert_sys1.png)
Expert systems[ESs] are developed and used in medical diagnosis which involves taking patient’s symptoms and laboratory tests as inputs. These systems are used when the expertise required is “highly valued and complex”[![2](https://en.wikipedia.org/wiki/Expert_system)]. Currently, using Deep Learning to solve problems is also a “highly valued and complex” task. Also [![5](https://engineering.purdue.edu/~engelb/abe565/es.htm)] says: “Incompleteness of information is characteristic of problems suitable for solution with ESs.”

The following points encouraged the study to build ESs for Deep Learning model tuning:

1. Medical diagnosis sounds analogous to Deep  Learning model tuning and also there are statements comparing Deep Learning to alchemy.
2. A knowledge base needs to be created having facts about deep learning algorithms and other rules which are consistent, properly prioritized and unambiguous:

   eg: From the methods mentioned in [![1]((www.deeplearningbook.org)), ![4](https://see.stanford.edu/materials/aimlcs229/ML-advice.pdf)] about the practical tips to tune hyperparameters, a sample set of rules (though not exhaustive) is:
           
            
            if (the training error is not good {
              increase the model size
                or
              change the learning rate
                or
              collect more data or richer set of features
            } else {
                measure performance of the test set
                if test perf. is also good {
                  Done.
                } else {
                  gather more data
                    or
                  reduce the size of the model
                    or
                  improve regularization ( eg: by adjusting weight decay )
                    or 
                  use regularization
                  
                  if all of the above fail {
                    gather more data
                  }
                }
            }
 
 3. Once a target performance is reached using an ES, explanation abilities of the ES can be used to figure out the best tuning steps also.

But, the appropriateness of using ES can be evaluated with a “telephone test”[![5](https://engineering.purdue.edu/~engelb/abe565/es.htm)] which states that in a telephone conversation if a domain expert can communicate with the user to solve a problem successfully, then ES can be used. The domain expert should be able to solve it consistently and also the information exchanged should be only verbal.  The “telephone test” also implies that we should be able to construct fixed-response questions, and they should be properly structured in a sequence for each decision[![6](http://dssresources.com/faq/index.php?action=artikel&id=230)].

Observations:  
On the choice of optimization algorithms, we were able to tabularize(verbalize) these only to this point until now:
![](es/optimization_algorithm_v2.png)

When it comes to model, we can get graphical output about the current status of the model with the help of training error/test error/number of epoch graph, visualizing gradients etc.,
After coming to know about the telephone test, and about the resolution with which we can look at the optimizations algorithms, and the questions about articulating about the status of the model,  concluded not to pursue this further.  

Remember that the latest in research related to meta-learning is called bilevel optimization[![3](https://www.cs.toronto.edu/~rgrosse/courses/csc2541_2021/)]. Until we get fruitful results from meta-learning,  we can depend on guides like “XYZ's Principles and Practice of Deep Learning” along with the help of institutions that give a stint on this so that Deep Learning enthusiasts can get up to speed just like they do in the field of medicine.

References: 
1) ![www.deeplearningbook.org](www.deeplearningbook.org)
2) ![https://en.wikipedia.org/wiki/Expert_system](https://en.wikipedia.org/wiki/Expert_system)
3) ![https://www.cs.toronto.edu/~rgrosse/courses/csc2541_2021/](https://www.cs.toronto.edu/~rgrosse/courses/csc241_2021/)
4) ![https://see.stanford.edu/materials/aimlcs229/ML-advice.pdf](https://see.stanford.edu/materials/aimlcs229/ML-advice.pdf)
5) ![https://engineering.purdue.edu/~engelb/abe565/es.htm](https://engineering.purdue.edu/~engelb/abe565/es.htm)
6) ![http://dssresources.com/faq/index.php?action=artikel&id=230](http://dssresources.com/faq/index.php?action=artikel&id=230)
