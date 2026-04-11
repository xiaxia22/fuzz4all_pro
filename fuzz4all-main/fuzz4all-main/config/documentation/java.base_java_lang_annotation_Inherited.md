# Annotation Type Inherited

**Source:** `java.base\java\lang\annotation\Inherited.html`

### Class Description

```java
@Documented

@Retention
(
RUNTIME
)

@Target
(
ANNOTATION_TYPE
)
public @interface
Inherited
```

Indicates that an annotation type is automatically inherited. If
an Inherited meta-annotation is present on an annotation type
declaration, and the user queries the annotation type on a class
declaration, and the class declaration has no annotation for this type,
then the class's superclass will automatically be queried for the
annotation type. This process will be repeated until an annotation for this
type is found, or the top of the class hierarchy (Object)
is reached. If no superclass has an annotation for this type, then
the query will indicate that the class in question has no such annotation.

Note that this meta-annotation type has no effect if the annotated
type is used to annotate anything other than a class. Note also
that this meta-annotation only causes annotations to be inherited
from superclasses; annotations on implemented interfaces have no
effect.

**Since:** 1.5
**See The Java™ Language Specification :** 9.6.4.3 @Inherited

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

*No entries found.*

### Additional Sections

#### Annotation Type Inherited

```java
@Documented

@Retention
(
RUNTIME
)

@Target
(
ANNOTATION_TYPE
)
public @interface
Inherited
```

Indicates that an annotation type is automatically inherited. If
an Inherited meta-annotation is present on an annotation type
declaration, and the user queries the annotation type on a class
declaration, and the class declaration has no annotation for this type,
then the class's superclass will automatically be queried for the
annotation type. This process will be repeated until an annotation for this
type is found, or the top of the class hierarchy (Object)
is reached. If no superclass has an annotation for this type, then
the query will indicate that the class in question has no such annotation.

Note that this meta-annotation type has no effect if the annotated
type is used to annotate anything other than a class. Note also
that this meta-annotation only causes annotations to be inherited
from superclasses; annotations on implemented interfaces have no
effect.

**Since:** 1.5
**See The Java™ Language Specification :** 9.6.4.3 @Inherited

@Documented

@Retention

(

RUNTIME

)

@Target

(

ANNOTATION_TYPE

)
public @interface

Inherited

Indicates that an annotation type is automatically inherited. If
an Inherited meta-annotation is present on an annotation type
declaration, and the user queries the annotation type on a class
declaration, and the class declaration has no annotation for this type,
then the class's superclass will automatically be queried for the
annotation type. This process will be repeated until an annotation for this
type is found, or the top of the class hierarchy (Object)
is reached. If no superclass has an annotation for this type, then
the query will indicate that the class in question has no such annotation.

Note that this meta-annotation type has no effect if the annotated
type is used to annotate anything other than a class. Note also
that this meta-annotation only causes annotations to be inherited
from superclasses; annotations on implemented interfaces have no
effect.

Note that this meta-annotation type has no effect if the annotated
type is used to annotate anything other than a class. Note also
that this meta-annotation only causes annotations to be inherited
from superclasses; annotations on implemented interfaces have no
effect.

---

