# Annotation Type FunctionalInterface

**Source:** `java.base\java\lang\FunctionalInterface.html`

### Class Description

```java
@Documented

@Retention
(
RUNTIME
)

@Target
(
TYPE
)
public @interface
FunctionalInterface
```

An informative annotation type used to indicate that an interface
type declaration is intended to be a

functional interface

as
defined by the Java Language Specification.

Conceptually, a functional interface has exactly one abstract
method. Since

default methods

have an implementation, they are not abstract. If
an interface declares an abstract method overriding one of the
public methods of

java.lang.Object

, that also does

not

count toward the interface's abstract method count
since any implementation of the interface will have an
implementation from

java.lang.Object

or elsewhere.

Note that instances of functional interfaces can be created with
lambda expressions, method references, or constructor references.

If a type is annotated with this annotation type, compilers are
required to generate an error message unless:

- The type is an interface type and not an annotation type, enum, or class.

The annotated type satisfies the requirements of a functional interface.

However, the compiler will treat any interface meeting the
definition of a functional interface as a functional interface
regardless of whether or not a

FunctionalInterface

annotation is present on the interface declaration.

**Since:** 1.8
**See The Java™ Language Specification :** 4.3.2. The Class Object, 9.8 Functional Interfaces, 9.4.3 Interface Method Body, 9.6.4.9 @FunctionalInterface

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

*No entries found.*

### Additional Sections

#### Annotation Type FunctionalInterface

```java
@Documented

@Retention
(
RUNTIME
)

@Target
(
TYPE
)
public @interface
FunctionalInterface
```

An informative annotation type used to indicate that an interface
type declaration is intended to be a

functional interface

as
defined by the Java Language Specification.

Conceptually, a functional interface has exactly one abstract
method. Since

default methods

have an implementation, they are not abstract. If
an interface declares an abstract method overriding one of the
public methods of

java.lang.Object

, that also does

not

count toward the interface's abstract method count
since any implementation of the interface will have an
implementation from

java.lang.Object

or elsewhere.

Note that instances of functional interfaces can be created with
lambda expressions, method references, or constructor references.

If a type is annotated with this annotation type, compilers are
required to generate an error message unless:

- The type is an interface type and not an annotation type, enum, or class.

The annotated type satisfies the requirements of a functional interface.

However, the compiler will treat any interface meeting the
definition of a functional interface as a functional interface
regardless of whether or not a

FunctionalInterface

annotation is present on the interface declaration.

**Since:** 1.8
**See The Java™ Language Specification :** 4.3.2. The Class Object, 9.8 Functional Interfaces, 9.4.3 Interface Method Body, 9.6.4.9 @FunctionalInterface

@Documented

@Retention

(

RUNTIME

)

@Target

(

TYPE

)
public @interface

FunctionalInterface

An informative annotation type used to indicate that an interface
type declaration is intended to be a

functional interface

as
defined by the Java Language Specification.

Conceptually, a functional interface has exactly one abstract
method. Since

default methods

have an implementation, they are not abstract. If
an interface declares an abstract method overriding one of the
public methods of

java.lang.Object

, that also does

not

count toward the interface's abstract method count
since any implementation of the interface will have an
implementation from

java.lang.Object

or elsewhere.

Note that instances of functional interfaces can be created with
lambda expressions, method references, or constructor references.

If a type is annotated with this annotation type, compilers are
required to generate an error message unless:

- The type is an interface type and not an annotation type, enum, or class.

The annotated type satisfies the requirements of a functional interface.

However, the compiler will treat any interface meeting the
definition of a functional interface as a functional interface
regardless of whether or not a

FunctionalInterface

annotation is present on the interface declaration.

Note that instances of functional interfaces can be created with
lambda expressions, method references, or constructor references.

If a type is annotated with this annotation type, compilers are
required to generate an error message unless:

- The type is an interface type and not an annotation type, enum, or class.

The annotated type satisfies the requirements of a functional interface.

However, the compiler will treat any interface meeting the
definition of a functional interface as a functional interface
regardless of whether or not a

FunctionalInterface

annotation is present on the interface declaration.

If a type is annotated with this annotation type, compilers are
required to generate an error message unless:

- The type is an interface type and not an annotation type, enum, or class.

The annotated type satisfies the requirements of a functional interface.

However, the compiler will treat any interface meeting the
definition of a functional interface as a functional interface
regardless of whether or not a

FunctionalInterface

annotation is present on the interface declaration.

The type is an interface type and not an annotation type, enum, or class.

The annotated type satisfies the requirements of a functional interface.

However, the compiler will treat any interface meeting the
definition of a functional interface as a functional interface
regardless of whether or not a

FunctionalInterface

annotation is present on the interface declaration.

---

