# Interface XPathExpression

**Source:** `java.xml\javax\xml\xpath\XPathExpression.html`

### Class Description

```java
public interface
XPathExpression
```

XPathExpression

provides access to compiled XPath expressions.
The XPath evaluation is affected by the factors described in the following table.

Evaluation of XPath Expressions

Factor

Behavior

context

The type of the context is implementation-dependent. If the value is
null, the operation must have no dependency on the context, otherwise
an XPathExpressionException will be thrown.

For the purposes of evaluating XPath expressions, a DocumentFragment
is treated like a Document node.

variables

If the expression contains a variable reference, its value will be found through the

XPathVariableResolver

.
An

XPathExpressionException

is raised if the variable resolver is undefined or
the resolver returns

null

for the variable.
The value of a variable must be immutable through the course of any single evaluation.

functions

If the expression contains a function reference, the function will be found through the

XPathFunctionResolver

.
An

XPathExpressionException

is raised if the function resolver is undefined or
the function resolver returns

null

for the function.

QNames

QNames in the expression are resolved against the XPath namespace context.

result

This result of evaluating an expression is converted to an instance of the desired return type.
Valid return types are defined in

XPathConstants

.
Conversion to the return type follows XPath conversion rules.

An XPath expression is not thread-safe and not reentrant.
In other words, it is the application's responsibility to make
sure that one

XPathExpression

object is not used from
more than one thread at any given time, and while the

evaluate

method is invoked, applications may not recursively call
the

evaluate

method.

**Since:** 1.5
**See Also:** XML Path Language (XPath) Version 1.0, Expressions

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### Object
evaluate​(
Object
item,

QName
returnType)
throws
XPathExpressionException

Evaluate the compiled XPath expression in the specified context and return the result as the specified type.

See

Evaluation of XPath Expressions

for context item evaluation,
variable, function and QName resolution and return type conversion.

The parameter

item

represents the context the XPath expression
will be operated on. The type of the context is implementation-dependent.
If the value is

null

, the operation must have no dependency on
the context, otherwise an XPathExpressionException will be thrown.

**Parameters:**
- item

- The context the XPath expression will be evaluated in.
- returnType

- The result type expected to be returned by the XPath expression.

**Returns:**
- The

Object

that is the result of evaluating the expression and converting the result to

returnType

.

**Throws:**
- XPathExpressionException

- If the expression cannot be evaluated.
- IllegalArgumentException

- If

returnType

is not one of the types defined in

XPathConstants

.
- NullPointerException

- If

returnType

is

null

.

**Implementation Note:**
- The type of the context is usually

Node

.

---

#### String
evaluate​(
Object
item)
throws
XPathExpressionException

Evaluate the compiled XPath expression in the specified context and return the result as a

String

.

This method calls

evaluate(Object item, QName returnType)

with a

returnType

of

XPathConstants.STRING

.

See

Evaluation of XPath Expressions

for context item evaluation,
variable, function and QName resolution and return type conversion.

The parameter

item

represents the context the XPath expression
will be operated on. The type of the context is implementation-dependent.
If the value is

null

, the operation must have no dependency on
the context, otherwise an XPathExpressionException will be thrown.

**Parameters:**
- item

- The context the XPath expression will be evaluated in.

**Returns:**
- The result of evaluating an XPath expression as a

String

.

**Throws:**
- XPathExpressionException

- If the expression cannot be evaluated.

**Implementation Note:**
- The type of the context is usually

Node

.

---

#### Object
evaluate​(
InputSource
source,

QName
returnType)
throws
XPathExpressionException

Evaluate the compiled XPath expression in the context
of the specified

InputSource

and return the result as the
specified type.

This method builds a data model for the

InputSource

and calls

evaluate(Object item, QName returnType)

on the resulting document object.

See

Evaluation of XPath Expressions

for context item evaluation,
variable, function and QName resolution and return type conversion.

If

returnType

is not one of the types defined in

XPathConstants

,
then an

IllegalArgumentException

is thrown.

If

source

or

returnType

is

null

,
then a

NullPointerException

is thrown.

**Parameters:**
- source

- The

InputSource

of the document to evaluate over.
- returnType

- The desired return type.

**Returns:**
- The

Object

that is the result of evaluating the expression and converting the result to

returnType

.

**Throws:**
- XPathExpressionException

- If the expression cannot be evaluated.
- IllegalArgumentException

- If

returnType

is not one of the types defined in

XPathConstants

.
- NullPointerException

- If

source or returnType

is

null

.

---

#### String
evaluate​(
InputSource
source)
throws
XPathExpressionException

Evaluate the compiled XPath expression in the context
of the specified

InputSource

and return the result as a

String

.

This method calls

evaluate(InputSource source, QName returnType)

with a

returnType

of

XPathConstants.STRING

.

See

Evaluation of XPath Expressions

for context item evaluation,
variable, function and QName resolution and return type conversion.

If

source

is

null

, then a

NullPointerException

is thrown.

**Parameters:**
- source

- The

InputSource

of the document to evaluate over.

**Returns:**
- The

String

that is the result of evaluating the expression and converting the result to a

String

.

**Throws:**
- XPathExpressionException

- If the expression cannot be evaluated.
- NullPointerException

- If

source

is

null

.

---

#### default <T> T evaluateExpression​(
Object
item,

Class
<T> type)
throws
XPathExpressionException

Evaluate the compiled XPath expression in the specified context, and return
the result with the type specified through the

class type

.

The parameter

item

represents the context the XPath expression
will be operated on. The type of the context is implementation-dependent.
If the value is

null

, the operation must have no dependency on
the context, otherwise an XPathExpressionException will be thrown.

**Parameters:**
- item

- The context the XPath expression will be evaluated in.
- type

- The class type expected to be returned by the XPath expression.

**Returns:**
- The result of evaluating the expression.

**Throws:**
- XPathExpressionException

- If the expression cannot be evaluated.
- IllegalArgumentException

- If

type

is not of the types
corresponding to the types defined in the

XPathResultType

, or XPathEvaluationResult is specified as the type but an
implementation supporting the

ANY

type is not available.
- NullPointerException

- If

type

is

null

.

**Since:**
- 9

**Implementation Requirements:**
- The default implementation in the XPath API is equivalent to:

```java
(T)evaluate(item, XPathEvaluationResult.XPathResultType.getQNameType(type));
```

Since the

evaluate

method does not support the

ANY

type, specifying
XPathEvaluationResult as the type will result in IllegalArgumentException.
Any implementation supporting the

ANY

type must override
this method.

**Implementation Note:**
- The type of the context is usually

Node

.

**Type Parameters:**
- T

- The class type that will be returned by the XPath expression.

---

#### default
XPathEvaluationResult
<?> evaluateExpression​(
Object
item)
throws
XPathExpressionException

Evaluate the compiled XPath expression in the specified context. This is
equivalent to calling

evaluateExpression(Object item, Class type)

with type

XPathEvaluationResult

:

```java
evaluateExpression(item, XPathEvaluationResult.class);
```

The parameter

item

represents the context the XPath expression
will be operated on. The type of the context is implementation-dependent.
If the value is

null

, the operation must have no dependency on
the context, otherwise an XPathExpressionException will be thrown.

**Parameters:**
- item

- The context the XPath expression will be evaluated in.

**Returns:**
- The result of evaluating the expression.

**Throws:**
- XPathExpressionException

- If the expression cannot be evaluated.
- IllegalArgumentException

- If the implementation of this method
does not support the

ANY

type.

**Since:**
- 9

**Implementation Requirements:**
- The default implementation in the XPath API is equivalent to:

```java
evaluateExpression(item, XPathEvaluationResult.class);
```

Since the

evaluate

method does not support the

ANY

type, the default implementation of this method will always throw an
IllegalArgumentException. Any implementation supporting the

ANY

type must therefore
override this method.

**Implementation Note:**
- The type of the context is usually

Node

.

---

#### default <T> T evaluateExpression​(
InputSource
source,

Class
<T> type)
throws
XPathExpressionException

Evaluate the compiled XPath expression in the specified context,
and return the result with the type specified through the

class type

This method builds a data model for the

InputSource

and calls

evaluateExpression(Object item, Class type)

on the resulting
document object.

By default, the JDK's data model is

Document

.

**Parameters:**
- source

- The

InputSource

of the document to evaluate over.
- type

- The class type expected to be returned by the XPath expression.

**Returns:**
- The result of evaluating the expression.

**Throws:**
- XPathExpressionException

- If the expression cannot be evaluated.
- IllegalArgumentException

- If

type

is not of the types
corresponding to the types defined in the

XPathResultType

, or XPathEvaluationResult is specified as the type but an
implementation supporting the

ANY

type
is not available.
- NullPointerException

- If

source or type

is

null

.

**Since:**
- 9

**Implementation Requirements:**
- The default implementation in the XPath API is equivalent to:

```java
(T)evaluate(source, XPathEvaluationResult.XPathResultType.getQNameType(type));
```

Since the

evaluate

method does not support the

ANY

type, specifying
XPathEvaluationResult as the type will result in IllegalArgumentException.
Any implementation supporting the

ANY

type must override
this method.

**Type Parameters:**
- T

- The class type that will be returned by the XPath expression.

---

#### default
XPathEvaluationResult
<?> evaluateExpression​(
InputSource
source)
throws
XPathExpressionException

Evaluate the compiled XPath expression in the specified context. This is
equivalent to calling

evaluateExpression(InputSource source, Class type)

with type

XPathEvaluationResult

:

```java
evaluateExpression(source, XPathEvaluationResult.class);
```

**Parameters:**
- source

- The

InputSource

of the document to evaluate over.

**Returns:**
- The result of evaluating the expression.

**Throws:**
- XPathExpressionException

- If the expression cannot be evaluated.
- IllegalArgumentException

- If the implementation of this method
does not support the

ANY

type.
- NullPointerException

- If

source

is

null

.

**Since:**
- 9

**Implementation Requirements:**
- The default implementation in the XPath API is equivalent to:

```java
(XPathEvaluationResult)evaluateExpression(source, XPathEvaluationResult.class);
```

Since the

evaluate

method does not support the

ANY

type, the default implementation of this method will always throw an
IllegalArgumentException. Any implementation supporting the

ANY

type must therefore
override this method.

---

### Additional Sections

#### Interface XPathExpression

```java
public interface
XPathExpression
```

XPathExpression

provides access to compiled XPath expressions.
The XPath evaluation is affected by the factors described in the following table.

Evaluation of XPath Expressions

Factor

Behavior

context

The type of the context is implementation-dependent. If the value is
null, the operation must have no dependency on the context, otherwise
an XPathExpressionException will be thrown.

For the purposes of evaluating XPath expressions, a DocumentFragment
is treated like a Document node.

variables

If the expression contains a variable reference, its value will be found through the

XPathVariableResolver

.
An

XPathExpressionException

is raised if the variable resolver is undefined or
the resolver returns

null

for the variable.
The value of a variable must be immutable through the course of any single evaluation.

functions

If the expression contains a function reference, the function will be found through the

XPathFunctionResolver

.
An

XPathExpressionException

is raised if the function resolver is undefined or
the function resolver returns

null

for the function.

QNames

QNames in the expression are resolved against the XPath namespace context.

result

This result of evaluating an expression is converted to an instance of the desired return type.
Valid return types are defined in

XPathConstants

.
Conversion to the return type follows XPath conversion rules.

An XPath expression is not thread-safe and not reentrant.
In other words, it is the application's responsibility to make
sure that one

XPathExpression

object is not used from
more than one thread at any given time, and while the

evaluate

method is invoked, applications may not recursively call
the

evaluate

method.

**Since:** 1.5
**See Also:** XML Path Language (XPath) Version 1.0, Expressions

public interface

XPathExpression

XPathExpression

provides access to compiled XPath expressions.
The XPath evaluation is affected by the factors described in the following table.

Evaluation of XPath Expressions

Factor

Behavior

context

The type of the context is implementation-dependent. If the value is
null, the operation must have no dependency on the context, otherwise
an XPathExpressionException will be thrown.

For the purposes of evaluating XPath expressions, a DocumentFragment
is treated like a Document node.

variables

If the expression contains a variable reference, its value will be found through the

XPathVariableResolver

.
An

XPathExpressionException

is raised if the variable resolver is undefined or
the resolver returns

null

for the variable.
The value of a variable must be immutable through the course of any single evaluation.

functions

If the expression contains a function reference, the function will be found through the

XPathFunctionResolver

.
An

XPathExpressionException

is raised if the function resolver is undefined or
the function resolver returns

null

for the function.

QNames

QNames in the expression are resolved against the XPath namespace context.

result

This result of evaluating an expression is converted to an instance of the desired return type.
Valid return types are defined in

XPathConstants

.
Conversion to the return type follows XPath conversion rules.

An XPath expression is not thread-safe and not reentrant.
In other words, it is the application's responsibility to make
sure that one

XPathExpression

object is not used from
more than one thread at any given time, and while the

evaluate

method is invoked, applications may not recursively call
the

evaluate

method.

An XPath expression is not thread-safe and not reentrant.
In other words, it is the application's responsibility to make
sure that one

XPathExpression

object is not used from
more than one thread at any given time, and while the

evaluate

method is invoked, applications may not recursively call
the

evaluate

method.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Default Methods

Modifier and Type

Method

Description

String

evaluate

​(

Object

item)

Evaluate the compiled XPath expression in the specified context and return the result as a

String

.

Object

evaluate

​(

Object

item,

QName

returnType)

Evaluate the compiled XPath expression in the specified context and return the result as the specified type.

String

evaluate

​(

InputSource

source)

Evaluate the compiled XPath expression in the context
of the specified

InputSource

and return the result as a

String

.

Object

evaluate

​(

InputSource

source,

QName

returnType)

Evaluate the compiled XPath expression in the context
of the specified

InputSource

and return the result as the
specified type.

default

XPathEvaluationResult

<?>

evaluateExpression

​(

Object

item)

Evaluate the compiled XPath expression in the specified context.

default <T> T

evaluateExpression

​(

Object

item,

Class

<T> type)

Evaluate the compiled XPath expression in the specified context, and return
the result with the type specified through the

class type

.

default

XPathEvaluationResult

<?>

evaluateExpression

​(

InputSource

source)

Evaluate the compiled XPath expression in the specified context.

default <T> T

evaluateExpression

​(

InputSource

source,

Class

<T> type)

Evaluate the compiled XPath expression in the specified context,
and return the result with the type specified through the

class type

Method Summary

All Methods

Instance Methods

Abstract Methods

Default Methods

Modifier and Type

Method

Description

String

evaluate

​(

Object

item)

Evaluate the compiled XPath expression in the specified context and return the result as a

String

.

Object

evaluate

​(

Object

item,

QName

returnType)

Evaluate the compiled XPath expression in the specified context and return the result as the specified type.

String

evaluate

​(

InputSource

source)

Evaluate the compiled XPath expression in the context
of the specified

InputSource

and return the result as a

String

.

Object

evaluate

​(

InputSource

source,

QName

returnType)

Evaluate the compiled XPath expression in the context
of the specified

InputSource

and return the result as the
specified type.

default

XPathEvaluationResult

<?>

evaluateExpression

​(

Object

item)

Evaluate the compiled XPath expression in the specified context.

default <T> T

evaluateExpression

​(

Object

item,

Class

<T> type)

Evaluate the compiled XPath expression in the specified context, and return
the result with the type specified through the

class type

.

default

XPathEvaluationResult

<?>

evaluateExpression

​(

InputSource

source)

Evaluate the compiled XPath expression in the specified context.

default <T> T

evaluateExpression

​(

InputSource

source,

Class

<T> type)

Evaluate the compiled XPath expression in the specified context,
and return the result with the type specified through the

class type

---

#### Method Summary

Evaluate the compiled XPath expression in the specified context and return the result as a

String

.

Evaluate the compiled XPath expression in the specified context and return the result as the specified type.

Evaluate the compiled XPath expression in the context
of the specified

InputSource

and return the result as a

String

.

Evaluate the compiled XPath expression in the context
of the specified

InputSource

and return the result as the
specified type.

Evaluate the compiled XPath expression in the specified context.

Evaluate the compiled XPath expression in the specified context, and return
the result with the type specified through the

class type

.

Evaluate the compiled XPath expression in the specified context,
and return the result with the type specified through the

class type

============ METHOD DETAIL ==========

- Method Detail

- evaluate

```java
Object
evaluate​(
Object
item,

QName
returnType)
throws
XPathExpressionException
```

Evaluate the compiled XPath expression in the specified context and return the result as the specified type.

See

Evaluation of XPath Expressions

for context item evaluation,
variable, function and QName resolution and return type conversion.

The parameter

item

represents the context the XPath expression
will be operated on. The type of the context is implementation-dependent.
If the value is

null

, the operation must have no dependency on
the context, otherwise an XPathExpressionException will be thrown.

**Implementation Note:** The type of the context is usually

Node

.
**Parameters:** item

- The context the XPath expression will be evaluated in.
**Parameters:** returnType

- The result type expected to be returned by the XPath expression.
**Returns:** The

Object

that is the result of evaluating the expression and converting the result to

returnType

.
**Throws:** XPathExpressionException

- If the expression cannot be evaluated.
**Throws:** IllegalArgumentException

- If

returnType

is not one of the types defined in

XPathConstants

.
**Throws:** NullPointerException

- If

returnType

is

null

.

- evaluate

```java
String
evaluate​(
Object
item)
throws
XPathExpressionException
```

Evaluate the compiled XPath expression in the specified context and return the result as a

String

.

This method calls

evaluate(Object item, QName returnType)

with a

returnType

of

XPathConstants.STRING

.

See

Evaluation of XPath Expressions

for context item evaluation,
variable, function and QName resolution and return type conversion.

The parameter

item

represents the context the XPath expression
will be operated on. The type of the context is implementation-dependent.
If the value is

null

, the operation must have no dependency on
the context, otherwise an XPathExpressionException will be thrown.

**Implementation Note:** The type of the context is usually

Node

.
**Parameters:** item

- The context the XPath expression will be evaluated in.
**Returns:** The result of evaluating an XPath expression as a

String

.
**Throws:** XPathExpressionException

- If the expression cannot be evaluated.

- evaluate

```java
Object
evaluate​(
InputSource
source,

QName
returnType)
throws
XPathExpressionException
```

Evaluate the compiled XPath expression in the context
of the specified

InputSource

and return the result as the
specified type.

This method builds a data model for the

InputSource

and calls

evaluate(Object item, QName returnType)

on the resulting document object.

See

Evaluation of XPath Expressions

for context item evaluation,
variable, function and QName resolution and return type conversion.

If

returnType

is not one of the types defined in

XPathConstants

,
then an

IllegalArgumentException

is thrown.

If

source

or

returnType

is

null

,
then a

NullPointerException

is thrown.

**Parameters:** source

- The

InputSource

of the document to evaluate over.
**Parameters:** returnType

- The desired return type.
**Returns:** The

Object

that is the result of evaluating the expression and converting the result to

returnType

.
**Throws:** XPathExpressionException

- If the expression cannot be evaluated.
**Throws:** IllegalArgumentException

- If

returnType

is not one of the types defined in

XPathConstants

.
**Throws:** NullPointerException

- If

source or returnType

is

null

.

- evaluate

```java
String
evaluate​(
InputSource
source)
throws
XPathExpressionException
```

Evaluate the compiled XPath expression in the context
of the specified

InputSource

and return the result as a

String

.

This method calls

evaluate(InputSource source, QName returnType)

with a

returnType

of

XPathConstants.STRING

.

See

Evaluation of XPath Expressions

for context item evaluation,
variable, function and QName resolution and return type conversion.

If

source

is

null

, then a

NullPointerException

is thrown.

**Parameters:** source

- The

InputSource

of the document to evaluate over.
**Returns:** The

String

that is the result of evaluating the expression and converting the result to a

String

.
**Throws:** XPathExpressionException

- If the expression cannot be evaluated.
**Throws:** NullPointerException

- If

source

is

null

.

- evaluateExpression

```java
default <T> T evaluateExpression​(
Object
item,

Class
<T> type)
throws
XPathExpressionException
```

Evaluate the compiled XPath expression in the specified context, and return
the result with the type specified through the

class type

.

The parameter

item

represents the context the XPath expression
will be operated on. The type of the context is implementation-dependent.
If the value is

null

, the operation must have no dependency on
the context, otherwise an XPathExpressionException will be thrown.

**Implementation Requirements:** The default implementation in the XPath API is equivalent to:

```java
(T)evaluate(item, XPathEvaluationResult.XPathResultType.getQNameType(type));
```

Since the

evaluate

method does not support the

ANY

type, specifying
XPathEvaluationResult as the type will result in IllegalArgumentException.
Any implementation supporting the

ANY

type must override
this method.
**Implementation Note:** The type of the context is usually

Node

.
**Type Parameters:** T

- The class type that will be returned by the XPath expression.
**Parameters:** item

- The context the XPath expression will be evaluated in.
**Parameters:** type

- The class type expected to be returned by the XPath expression.
**Returns:** The result of evaluating the expression.
**Throws:** XPathExpressionException

- If the expression cannot be evaluated.
**Throws:** IllegalArgumentException

- If

type

is not of the types
corresponding to the types defined in the

XPathResultType

, or XPathEvaluationResult is specified as the type but an
implementation supporting the

ANY

type is not available.
**Throws:** NullPointerException

- If

type

is

null

.
**Since:** 9

- evaluateExpression

```java
default
XPathEvaluationResult
<?> evaluateExpression​(
Object
item)
throws
XPathExpressionException
```

Evaluate the compiled XPath expression in the specified context. This is
equivalent to calling

evaluateExpression(Object item, Class type)

with type

XPathEvaluationResult

:

```java
evaluateExpression(item, XPathEvaluationResult.class);
```

The parameter

item

represents the context the XPath expression
will be operated on. The type of the context is implementation-dependent.
If the value is

null

, the operation must have no dependency on
the context, otherwise an XPathExpressionException will be thrown.

**Implementation Requirements:** The default implementation in the XPath API is equivalent to:

```java
evaluateExpression(item, XPathEvaluationResult.class);
```

Since the

evaluate

method does not support the

ANY

type, the default implementation of this method will always throw an
IllegalArgumentException. Any implementation supporting the

ANY

type must therefore
override this method.
**Implementation Note:** The type of the context is usually

Node

.
**Parameters:** item

- The context the XPath expression will be evaluated in.
**Returns:** The result of evaluating the expression.
**Throws:** XPathExpressionException

- If the expression cannot be evaluated.
**Throws:** IllegalArgumentException

- If the implementation of this method
does not support the

ANY

type.
**Since:** 9

- evaluateExpression

```java
default <T> T evaluateExpression​(
InputSource
source,

Class
<T> type)
throws
XPathExpressionException
```

Evaluate the compiled XPath expression in the specified context,
and return the result with the type specified through the

class type

This method builds a data model for the

InputSource

and calls

evaluateExpression(Object item, Class type)

on the resulting
document object.

By default, the JDK's data model is

Document

.

**Implementation Requirements:** The default implementation in the XPath API is equivalent to:

```java
(T)evaluate(source, XPathEvaluationResult.XPathResultType.getQNameType(type));
```

Since the

evaluate

method does not support the

ANY

type, specifying
XPathEvaluationResult as the type will result in IllegalArgumentException.
Any implementation supporting the

ANY

type must override
this method.
**Type Parameters:** T

- The class type that will be returned by the XPath expression.
**Parameters:** source

- The

InputSource

of the document to evaluate over.
**Parameters:** type

- The class type expected to be returned by the XPath expression.
**Returns:** The result of evaluating the expression.
**Throws:** XPathExpressionException

- If the expression cannot be evaluated.
**Throws:** IllegalArgumentException

- If

type

is not of the types
corresponding to the types defined in the

XPathResultType

, or XPathEvaluationResult is specified as the type but an
implementation supporting the

ANY

type
is not available.
**Throws:** NullPointerException

- If

source or type

is

null

.
**Since:** 9

- evaluateExpression

```java
default
XPathEvaluationResult
<?> evaluateExpression​(
InputSource
source)
throws
XPathExpressionException
```

Evaluate the compiled XPath expression in the specified context. This is
equivalent to calling

evaluateExpression(InputSource source, Class type)

with type

XPathEvaluationResult

:

```java
evaluateExpression(source, XPathEvaluationResult.class);
```

**Implementation Requirements:** The default implementation in the XPath API is equivalent to:

```java
(XPathEvaluationResult)evaluateExpression(source, XPathEvaluationResult.class);
```

Since the

evaluate

method does not support the

ANY

type, the default implementation of this method will always throw an
IllegalArgumentException. Any implementation supporting the

ANY

type must therefore
override this method.
**Parameters:** source

- The

InputSource

of the document to evaluate over.
**Returns:** The result of evaluating the expression.
**Throws:** XPathExpressionException

- If the expression cannot be evaluated.
**Throws:** IllegalArgumentException

- If the implementation of this method
does not support the

ANY

type.
**Throws:** NullPointerException

- If

source

is

null

.
**Since:** 9

Method Detail

- evaluate

```java
Object
evaluate​(
Object
item,

QName
returnType)
throws
XPathExpressionException
```

Evaluate the compiled XPath expression in the specified context and return the result as the specified type.

See

Evaluation of XPath Expressions

for context item evaluation,
variable, function and QName resolution and return type conversion.

The parameter

item

represents the context the XPath expression
will be operated on. The type of the context is implementation-dependent.
If the value is

null

, the operation must have no dependency on
the context, otherwise an XPathExpressionException will be thrown.

**Implementation Note:** The type of the context is usually

Node

.
**Parameters:** item

- The context the XPath expression will be evaluated in.
**Parameters:** returnType

- The result type expected to be returned by the XPath expression.
**Returns:** The

Object

that is the result of evaluating the expression and converting the result to

returnType

.
**Throws:** XPathExpressionException

- If the expression cannot be evaluated.
**Throws:** IllegalArgumentException

- If

returnType

is not one of the types defined in

XPathConstants

.
**Throws:** NullPointerException

- If

returnType

is

null

.

- evaluate

```java
String
evaluate​(
Object
item)
throws
XPathExpressionException
```

Evaluate the compiled XPath expression in the specified context and return the result as a

String

.

This method calls

evaluate(Object item, QName returnType)

with a

returnType

of

XPathConstants.STRING

.

See

Evaluation of XPath Expressions

for context item evaluation,
variable, function and QName resolution and return type conversion.

The parameter

item

represents the context the XPath expression
will be operated on. The type of the context is implementation-dependent.
If the value is

null

, the operation must have no dependency on
the context, otherwise an XPathExpressionException will be thrown.

**Implementation Note:** The type of the context is usually

Node

.
**Parameters:** item

- The context the XPath expression will be evaluated in.
**Returns:** The result of evaluating an XPath expression as a

String

.
**Throws:** XPathExpressionException

- If the expression cannot be evaluated.

- evaluate

```java
Object
evaluate​(
InputSource
source,

QName
returnType)
throws
XPathExpressionException
```

Evaluate the compiled XPath expression in the context
of the specified

InputSource

and return the result as the
specified type.

This method builds a data model for the

InputSource

and calls

evaluate(Object item, QName returnType)

on the resulting document object.

See

Evaluation of XPath Expressions

for context item evaluation,
variable, function and QName resolution and return type conversion.

If

returnType

is not one of the types defined in

XPathConstants

,
then an

IllegalArgumentException

is thrown.

If

source

or

returnType

is

null

,
then a

NullPointerException

is thrown.

**Parameters:** source

- The

InputSource

of the document to evaluate over.
**Parameters:** returnType

- The desired return type.
**Returns:** The

Object

that is the result of evaluating the expression and converting the result to

returnType

.
**Throws:** XPathExpressionException

- If the expression cannot be evaluated.
**Throws:** IllegalArgumentException

- If

returnType

is not one of the types defined in

XPathConstants

.
**Throws:** NullPointerException

- If

source or returnType

is

null

.

- evaluate

```java
String
evaluate​(
InputSource
source)
throws
XPathExpressionException
```

Evaluate the compiled XPath expression in the context
of the specified

InputSource

and return the result as a

String

.

This method calls

evaluate(InputSource source, QName returnType)

with a

returnType

of

XPathConstants.STRING

.

See

Evaluation of XPath Expressions

for context item evaluation,
variable, function and QName resolution and return type conversion.

If

source

is

null

, then a

NullPointerException

is thrown.

**Parameters:** source

- The

InputSource

of the document to evaluate over.
**Returns:** The

String

that is the result of evaluating the expression and converting the result to a

String

.
**Throws:** XPathExpressionException

- If the expression cannot be evaluated.
**Throws:** NullPointerException

- If

source

is

null

.

- evaluateExpression

```java
default <T> T evaluateExpression​(
Object
item,

Class
<T> type)
throws
XPathExpressionException
```

Evaluate the compiled XPath expression in the specified context, and return
the result with the type specified through the

class type

.

The parameter

item

represents the context the XPath expression
will be operated on. The type of the context is implementation-dependent.
If the value is

null

, the operation must have no dependency on
the context, otherwise an XPathExpressionException will be thrown.

**Implementation Requirements:** The default implementation in the XPath API is equivalent to:

```java
(T)evaluate(item, XPathEvaluationResult.XPathResultType.getQNameType(type));
```

Since the

evaluate

method does not support the

ANY

type, specifying
XPathEvaluationResult as the type will result in IllegalArgumentException.
Any implementation supporting the

ANY

type must override
this method.
**Implementation Note:** The type of the context is usually

Node

.
**Type Parameters:** T

- The class type that will be returned by the XPath expression.
**Parameters:** item

- The context the XPath expression will be evaluated in.
**Parameters:** type

- The class type expected to be returned by the XPath expression.
**Returns:** The result of evaluating the expression.
**Throws:** XPathExpressionException

- If the expression cannot be evaluated.
**Throws:** IllegalArgumentException

- If

type

is not of the types
corresponding to the types defined in the

XPathResultType

, or XPathEvaluationResult is specified as the type but an
implementation supporting the

ANY

type is not available.
**Throws:** NullPointerException

- If

type

is

null

.
**Since:** 9

- evaluateExpression

```java
default
XPathEvaluationResult
<?> evaluateExpression​(
Object
item)
throws
XPathExpressionException
```

Evaluate the compiled XPath expression in the specified context. This is
equivalent to calling

evaluateExpression(Object item, Class type)

with type

XPathEvaluationResult

:

```java
evaluateExpression(item, XPathEvaluationResult.class);
```

The parameter

item

represents the context the XPath expression
will be operated on. The type of the context is implementation-dependent.
If the value is

null

, the operation must have no dependency on
the context, otherwise an XPathExpressionException will be thrown.

**Implementation Requirements:** The default implementation in the XPath API is equivalent to:

```java
evaluateExpression(item, XPathEvaluationResult.class);
```

Since the

evaluate

method does not support the

ANY

type, the default implementation of this method will always throw an
IllegalArgumentException. Any implementation supporting the

ANY

type must therefore
override this method.
**Implementation Note:** The type of the context is usually

Node

.
**Parameters:** item

- The context the XPath expression will be evaluated in.
**Returns:** The result of evaluating the expression.
**Throws:** XPathExpressionException

- If the expression cannot be evaluated.
**Throws:** IllegalArgumentException

- If the implementation of this method
does not support the

ANY

type.
**Since:** 9

- evaluateExpression

```java
default <T> T evaluateExpression​(
InputSource
source,

Class
<T> type)
throws
XPathExpressionException
```

Evaluate the compiled XPath expression in the specified context,
and return the result with the type specified through the

class type

This method builds a data model for the

InputSource

and calls

evaluateExpression(Object item, Class type)

on the resulting
document object.

By default, the JDK's data model is

Document

.

**Implementation Requirements:** The default implementation in the XPath API is equivalent to:

```java
(T)evaluate(source, XPathEvaluationResult.XPathResultType.getQNameType(type));
```

Since the

evaluate

method does not support the

ANY

type, specifying
XPathEvaluationResult as the type will result in IllegalArgumentException.
Any implementation supporting the

ANY

type must override
this method.
**Type Parameters:** T

- The class type that will be returned by the XPath expression.
**Parameters:** source

- The

InputSource

of the document to evaluate over.
**Parameters:** type

- The class type expected to be returned by the XPath expression.
**Returns:** The result of evaluating the expression.
**Throws:** XPathExpressionException

- If the expression cannot be evaluated.
**Throws:** IllegalArgumentException

- If

type

is not of the types
corresponding to the types defined in the

XPathResultType

, or XPathEvaluationResult is specified as the type but an
implementation supporting the

ANY

type
is not available.
**Throws:** NullPointerException

- If

source or type

is

null

.
**Since:** 9

- evaluateExpression

```java
default
XPathEvaluationResult
<?> evaluateExpression​(
InputSource
source)
throws
XPathExpressionException
```

Evaluate the compiled XPath expression in the specified context. This is
equivalent to calling

evaluateExpression(InputSource source, Class type)

with type

XPathEvaluationResult

:

```java
evaluateExpression(source, XPathEvaluationResult.class);
```

**Implementation Requirements:** The default implementation in the XPath API is equivalent to:

```java
(XPathEvaluationResult)evaluateExpression(source, XPathEvaluationResult.class);
```

Since the

evaluate

method does not support the

ANY

type, the default implementation of this method will always throw an
IllegalArgumentException. Any implementation supporting the

ANY

type must therefore
override this method.
**Parameters:** source

- The

InputSource

of the document to evaluate over.
**Returns:** The result of evaluating the expression.
**Throws:** XPathExpressionException

- If the expression cannot be evaluated.
**Throws:** IllegalArgumentException

- If the implementation of this method
does not support the

ANY

type.
**Throws:** NullPointerException

- If

source

is

null

.
**Since:** 9

---

#### Method Detail

evaluate

```java
Object
evaluate​(
Object
item,

QName
returnType)
throws
XPathExpressionException
```

Evaluate the compiled XPath expression in the specified context and return the result as the specified type.

See

Evaluation of XPath Expressions

for context item evaluation,
variable, function and QName resolution and return type conversion.

The parameter

item

represents the context the XPath expression
will be operated on. The type of the context is implementation-dependent.
If the value is

null

, the operation must have no dependency on
the context, otherwise an XPathExpressionException will be thrown.

**Implementation Note:** The type of the context is usually

Node

.
**Parameters:** item

- The context the XPath expression will be evaluated in.
**Parameters:** returnType

- The result type expected to be returned by the XPath expression.
**Returns:** The

Object

that is the result of evaluating the expression and converting the result to

returnType

.
**Throws:** XPathExpressionException

- If the expression cannot be evaluated.
**Throws:** IllegalArgumentException

- If

returnType

is not one of the types defined in

XPathConstants

.
**Throws:** NullPointerException

- If

returnType

is

null

.

---

#### evaluate

Object

evaluate​(

Object

item,

QName

returnType)
throws

XPathExpressionException

Evaluate the compiled XPath expression in the specified context and return the result as the specified type.

See

Evaluation of XPath Expressions

for context item evaluation,
variable, function and QName resolution and return type conversion.

The parameter

item

represents the context the XPath expression
will be operated on. The type of the context is implementation-dependent.
If the value is

null

, the operation must have no dependency on
the context, otherwise an XPathExpressionException will be thrown.

See

Evaluation of XPath Expressions

for context item evaluation,
variable, function and QName resolution and return type conversion.

The parameter

item

represents the context the XPath expression
will be operated on. The type of the context is implementation-dependent.
If the value is

null

, the operation must have no dependency on
the context, otherwise an XPathExpressionException will be thrown.

The parameter

item

represents the context the XPath expression
will be operated on. The type of the context is implementation-dependent.
If the value is

null

, the operation must have no dependency on
the context, otherwise an XPathExpressionException will be thrown.

evaluate

```java
String
evaluate​(
Object
item)
throws
XPathExpressionException
```

Evaluate the compiled XPath expression in the specified context and return the result as a

String

.

This method calls

evaluate(Object item, QName returnType)

with a

returnType

of

XPathConstants.STRING

.

See

Evaluation of XPath Expressions

for context item evaluation,
variable, function and QName resolution and return type conversion.

The parameter

item

represents the context the XPath expression
will be operated on. The type of the context is implementation-dependent.
If the value is

null

, the operation must have no dependency on
the context, otherwise an XPathExpressionException will be thrown.

**Implementation Note:** The type of the context is usually

Node

.
**Parameters:** item

- The context the XPath expression will be evaluated in.
**Returns:** The result of evaluating an XPath expression as a

String

.
**Throws:** XPathExpressionException

- If the expression cannot be evaluated.

---

#### evaluate

String

evaluate​(

Object

item)
throws

XPathExpressionException

Evaluate the compiled XPath expression in the specified context and return the result as a

String

.

This method calls

evaluate(Object item, QName returnType)

with a

returnType

of

XPathConstants.STRING

.

See

Evaluation of XPath Expressions

for context item evaluation,
variable, function and QName resolution and return type conversion.

The parameter

item

represents the context the XPath expression
will be operated on. The type of the context is implementation-dependent.
If the value is

null

, the operation must have no dependency on
the context, otherwise an XPathExpressionException will be thrown.

This method calls

evaluate(Object item, QName returnType)

with a

returnType

of

XPathConstants.STRING

.

See

Evaluation of XPath Expressions

for context item evaluation,
variable, function and QName resolution and return type conversion.

The parameter

item

represents the context the XPath expression
will be operated on. The type of the context is implementation-dependent.
If the value is

null

, the operation must have no dependency on
the context, otherwise an XPathExpressionException will be thrown.

See

Evaluation of XPath Expressions

for context item evaluation,
variable, function and QName resolution and return type conversion.

The parameter

item

represents the context the XPath expression
will be operated on. The type of the context is implementation-dependent.
If the value is

null

, the operation must have no dependency on
the context, otherwise an XPathExpressionException will be thrown.

The parameter

item

represents the context the XPath expression
will be operated on. The type of the context is implementation-dependent.
If the value is

null

, the operation must have no dependency on
the context, otherwise an XPathExpressionException will be thrown.

evaluate

```java
Object
evaluate​(
InputSource
source,

QName
returnType)
throws
XPathExpressionException
```

Evaluate the compiled XPath expression in the context
of the specified

InputSource

and return the result as the
specified type.

This method builds a data model for the

InputSource

and calls

evaluate(Object item, QName returnType)

on the resulting document object.

See

Evaluation of XPath Expressions

for context item evaluation,
variable, function and QName resolution and return type conversion.

If

returnType

is not one of the types defined in

XPathConstants

,
then an

IllegalArgumentException

is thrown.

If

source

or

returnType

is

null

,
then a

NullPointerException

is thrown.

**Parameters:** source

- The

InputSource

of the document to evaluate over.
**Parameters:** returnType

- The desired return type.
**Returns:** The

Object

that is the result of evaluating the expression and converting the result to

returnType

.
**Throws:** XPathExpressionException

- If the expression cannot be evaluated.
**Throws:** IllegalArgumentException

- If

returnType

is not one of the types defined in

XPathConstants

.
**Throws:** NullPointerException

- If

source or returnType

is

null

.

---

#### evaluate

Object

evaluate​(

InputSource

source,

QName

returnType)
throws

XPathExpressionException

Evaluate the compiled XPath expression in the context
of the specified

InputSource

and return the result as the
specified type.

This method builds a data model for the

InputSource

and calls

evaluate(Object item, QName returnType)

on the resulting document object.

See

Evaluation of XPath Expressions

for context item evaluation,
variable, function and QName resolution and return type conversion.

If

returnType

is not one of the types defined in

XPathConstants

,
then an

IllegalArgumentException

is thrown.

If

source

or

returnType

is

null

,
then a

NullPointerException

is thrown.

This method builds a data model for the

InputSource

and calls

evaluate(Object item, QName returnType)

on the resulting document object.

See

Evaluation of XPath Expressions

for context item evaluation,
variable, function and QName resolution and return type conversion.

If

returnType

is not one of the types defined in

XPathConstants

,
then an

IllegalArgumentException

is thrown.

If

source

or

returnType

is

null

,
then a

NullPointerException

is thrown.

See

Evaluation of XPath Expressions

for context item evaluation,
variable, function and QName resolution and return type conversion.

If

returnType

is not one of the types defined in

XPathConstants

,
then an

IllegalArgumentException

is thrown.

If

source

or

returnType

is

null

,
then a

NullPointerException

is thrown.

If

returnType

is not one of the types defined in

XPathConstants

,
then an

IllegalArgumentException

is thrown.

If

source

or

returnType

is

null

,
then a

NullPointerException

is thrown.

If

source

or

returnType

is

null

,
then a

NullPointerException

is thrown.

evaluate

```java
String
evaluate​(
InputSource
source)
throws
XPathExpressionException
```

Evaluate the compiled XPath expression in the context
of the specified

InputSource

and return the result as a

String

.

This method calls

evaluate(InputSource source, QName returnType)

with a

returnType

of

XPathConstants.STRING

.

See

Evaluation of XPath Expressions

for context item evaluation,
variable, function and QName resolution and return type conversion.

If

source

is

null

, then a

NullPointerException

is thrown.

**Parameters:** source

- The

InputSource

of the document to evaluate over.
**Returns:** The

String

that is the result of evaluating the expression and converting the result to a

String

.
**Throws:** XPathExpressionException

- If the expression cannot be evaluated.
**Throws:** NullPointerException

- If

source

is

null

.

---

#### evaluate

String

evaluate​(

InputSource

source)
throws

XPathExpressionException

Evaluate the compiled XPath expression in the context
of the specified

InputSource

and return the result as a

String

.

This method calls

evaluate(InputSource source, QName returnType)

with a

returnType

of

XPathConstants.STRING

.

See

Evaluation of XPath Expressions

for context item evaluation,
variable, function and QName resolution and return type conversion.

If

source

is

null

, then a

NullPointerException

is thrown.

This method calls

evaluate(InputSource source, QName returnType)

with a

returnType

of

XPathConstants.STRING

.

See

Evaluation of XPath Expressions

for context item evaluation,
variable, function and QName resolution and return type conversion.

If

source

is

null

, then a

NullPointerException

is thrown.

See

Evaluation of XPath Expressions

for context item evaluation,
variable, function and QName resolution and return type conversion.

If

source

is

null

, then a

NullPointerException

is thrown.

If

source

is

null

, then a

NullPointerException

is thrown.

evaluateExpression

```java
default <T> T evaluateExpression​(
Object
item,

Class
<T> type)
throws
XPathExpressionException
```

Evaluate the compiled XPath expression in the specified context, and return
the result with the type specified through the

class type

.

The parameter

item

represents the context the XPath expression
will be operated on. The type of the context is implementation-dependent.
If the value is

null

, the operation must have no dependency on
the context, otherwise an XPathExpressionException will be thrown.

**Implementation Requirements:** The default implementation in the XPath API is equivalent to:

```java
(T)evaluate(item, XPathEvaluationResult.XPathResultType.getQNameType(type));
```

Since the

evaluate

method does not support the

ANY

type, specifying
XPathEvaluationResult as the type will result in IllegalArgumentException.
Any implementation supporting the

ANY

type must override
this method.
**Implementation Note:** The type of the context is usually

Node

.
**Type Parameters:** T

- The class type that will be returned by the XPath expression.
**Parameters:** item

- The context the XPath expression will be evaluated in.
**Parameters:** type

- The class type expected to be returned by the XPath expression.
**Returns:** The result of evaluating the expression.
**Throws:** XPathExpressionException

- If the expression cannot be evaluated.
**Throws:** IllegalArgumentException

- If

type

is not of the types
corresponding to the types defined in the

XPathResultType

, or XPathEvaluationResult is specified as the type but an
implementation supporting the

ANY

type is not available.
**Throws:** NullPointerException

- If

type

is

null

.
**Since:** 9

---

#### evaluateExpression

default <T> T evaluateExpression​(

Object

item,

Class

<T> type)
throws

XPathExpressionException

Evaluate the compiled XPath expression in the specified context, and return
the result with the type specified through the

class type

.

The parameter

item

represents the context the XPath expression
will be operated on. The type of the context is implementation-dependent.
If the value is

null

, the operation must have no dependency on
the context, otherwise an XPathExpressionException will be thrown.

The parameter

item

represents the context the XPath expression
will be operated on. The type of the context is implementation-dependent.
If the value is

null

, the operation must have no dependency on
the context, otherwise an XPathExpressionException will be thrown.

(T)evaluate(item, XPathEvaluationResult.XPathResultType.getQNameType(type));

evaluateExpression

```java
default
XPathEvaluationResult
<?> evaluateExpression​(
Object
item)
throws
XPathExpressionException
```

Evaluate the compiled XPath expression in the specified context. This is
equivalent to calling

evaluateExpression(Object item, Class type)

with type

XPathEvaluationResult

:

```java
evaluateExpression(item, XPathEvaluationResult.class);
```

The parameter

item

represents the context the XPath expression
will be operated on. The type of the context is implementation-dependent.
If the value is

null

, the operation must have no dependency on
the context, otherwise an XPathExpressionException will be thrown.

**Implementation Requirements:** The default implementation in the XPath API is equivalent to:

```java
evaluateExpression(item, XPathEvaluationResult.class);
```

Since the

evaluate

method does not support the

ANY

type, the default implementation of this method will always throw an
IllegalArgumentException. Any implementation supporting the

ANY

type must therefore
override this method.
**Implementation Note:** The type of the context is usually

Node

.
**Parameters:** item

- The context the XPath expression will be evaluated in.
**Returns:** The result of evaluating the expression.
**Throws:** XPathExpressionException

- If the expression cannot be evaluated.
**Throws:** IllegalArgumentException

- If the implementation of this method
does not support the

ANY

type.
**Since:** 9

---

#### evaluateExpression

default

XPathEvaluationResult

<?> evaluateExpression​(

Object

item)
throws

XPathExpressionException

Evaluate the compiled XPath expression in the specified context. This is
equivalent to calling

evaluateExpression(Object item, Class type)

with type

XPathEvaluationResult

:

```java
evaluateExpression(item, XPathEvaluationResult.class);
```

The parameter

item

represents the context the XPath expression
will be operated on. The type of the context is implementation-dependent.
If the value is

null

, the operation must have no dependency on
the context, otherwise an XPathExpressionException will be thrown.

evaluateExpression(item, XPathEvaluationResult.class);

The parameter

item

represents the context the XPath expression
will be operated on. The type of the context is implementation-dependent.
If the value is

null

, the operation must have no dependency on
the context, otherwise an XPathExpressionException will be thrown.

evaluateExpression

```java
default <T> T evaluateExpression​(
InputSource
source,

Class
<T> type)
throws
XPathExpressionException
```

Evaluate the compiled XPath expression in the specified context,
and return the result with the type specified through the

class type

This method builds a data model for the

InputSource

and calls

evaluateExpression(Object item, Class type)

on the resulting
document object.

By default, the JDK's data model is

Document

.

**Implementation Requirements:** The default implementation in the XPath API is equivalent to:

```java
(T)evaluate(source, XPathEvaluationResult.XPathResultType.getQNameType(type));
```

Since the

evaluate

method does not support the

ANY

type, specifying
XPathEvaluationResult as the type will result in IllegalArgumentException.
Any implementation supporting the

ANY

type must override
this method.
**Type Parameters:** T

- The class type that will be returned by the XPath expression.
**Parameters:** source

- The

InputSource

of the document to evaluate over.
**Parameters:** type

- The class type expected to be returned by the XPath expression.
**Returns:** The result of evaluating the expression.
**Throws:** XPathExpressionException

- If the expression cannot be evaluated.
**Throws:** IllegalArgumentException

- If

type

is not of the types
corresponding to the types defined in the

XPathResultType

, or XPathEvaluationResult is specified as the type but an
implementation supporting the

ANY

type
is not available.
**Throws:** NullPointerException

- If

source or type

is

null

.
**Since:** 9

---

#### evaluateExpression

default <T> T evaluateExpression​(

InputSource

source,

Class

<T> type)
throws

XPathExpressionException

Evaluate the compiled XPath expression in the specified context,
and return the result with the type specified through the

class type

This method builds a data model for the

InputSource

and calls

evaluateExpression(Object item, Class type)

on the resulting
document object.

By default, the JDK's data model is

Document

.

This method builds a data model for the

InputSource

and calls

evaluateExpression(Object item, Class type)

on the resulting
document object.

By default, the JDK's data model is

Document

.

By default, the JDK's data model is

Document

.

(T)evaluate(source, XPathEvaluationResult.XPathResultType.getQNameType(type));

evaluateExpression

```java
default
XPathEvaluationResult
<?> evaluateExpression​(
InputSource
source)
throws
XPathExpressionException
```

Evaluate the compiled XPath expression in the specified context. This is
equivalent to calling

evaluateExpression(InputSource source, Class type)

with type

XPathEvaluationResult

:

```java
evaluateExpression(source, XPathEvaluationResult.class);
```

**Implementation Requirements:** The default implementation in the XPath API is equivalent to:

```java
(XPathEvaluationResult)evaluateExpression(source, XPathEvaluationResult.class);
```

Since the

evaluate

method does not support the

ANY

type, the default implementation of this method will always throw an
IllegalArgumentException. Any implementation supporting the

ANY

type must therefore
override this method.
**Parameters:** source

- The

InputSource

of the document to evaluate over.
**Returns:** The result of evaluating the expression.
**Throws:** XPathExpressionException

- If the expression cannot be evaluated.
**Throws:** IllegalArgumentException

- If the implementation of this method
does not support the

ANY

type.
**Throws:** NullPointerException

- If

source

is

null

.
**Since:** 9

---

#### evaluateExpression

default

XPathEvaluationResult

<?> evaluateExpression​(

InputSource

source)
throws

XPathExpressionException

Evaluate the compiled XPath expression in the specified context. This is
equivalent to calling

evaluateExpression(InputSource source, Class type)

with type

XPathEvaluationResult

:

```java
evaluateExpression(source, XPathEvaluationResult.class);
```

evaluateExpression(source, XPathEvaluationResult.class);

(XPathEvaluationResult)evaluateExpression(source, XPathEvaluationResult.class);

---

