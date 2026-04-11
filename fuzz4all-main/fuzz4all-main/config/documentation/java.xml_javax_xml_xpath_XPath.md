# Interface XPath

**Source:** `java.xml\javax\xml\xpath\XPath.html`

### Class Description

```java
public interface
XPath
```

XPath

provides access to the XPath evaluation environment and expressions.
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

set with

setXPathVariableResolver(XPathVariableResolver resolver)

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

set with

setXPathFunctionResolver(XPathFunctionResolver resolver)

.
An

XPathExpressionException

is raised if the function resolver is undefined or
the function resolver returns

null

for the function.

QNames

QNames in the expression are resolved against the XPath namespace context
set with

setNamespaceContext(NamespaceContext nsContext)

.

result

This result of evaluating an expression is converted to an instance of the desired return type.
Valid return types are defined in

XPathConstants

.
Conversion to the return type follows XPath conversion rules.

An XPath object is not thread-safe and not reentrant.
In other words, it is the application's responsibility to make
sure that one

XPath

object is not used from
more than one thread at any given time, and while the

evaluate

method is invoked, applications may not recursively call
the

evaluate

method.

**Since:** 1.5
**See Also:** XML Path Language (XPath) Version 1.0

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void reset()

Reset this

XPath

to its original configuration.

XPath

is reset to the same state as when it was created with

XPathFactory.newXPath()

.

reset()

is designed to allow the reuse of existing

XPath

s
thus saving resources associated with the creation of new

XPath

s.

The reset

XPath

is not guaranteed to have the same

XPathFunctionResolver

,

XPathVariableResolver

or

NamespaceContext

Object

s, e.g.

Object.equals(Object obj)

.
It is guaranteed to have a functionally equal

XPathFunctionResolver

,

XPathVariableResolver

and

NamespaceContext

.

---

#### void setXPathVariableResolver​(
XPathVariableResolver
resolver)

Establish a variable resolver.

A

NullPointerException

is thrown if

resolver

is

null

.

**Parameters:**
- resolver

- Variable resolver.

**Throws:**
- NullPointerException

- If

resolver

is

null

.

---

#### XPathVariableResolver
getXPathVariableResolver()

Return the current variable resolver.

null

is returned in no variable resolver is in effect.

**Returns:**
- Current variable resolver.

---

#### void setXPathFunctionResolver​(
XPathFunctionResolver
resolver)

Establish a function resolver.

A

NullPointerException

is thrown if

resolver

is

null

.

**Parameters:**
- resolver

- XPath function resolver.

**Throws:**
- NullPointerException

- If

resolver

is

null

.

---

#### XPathFunctionResolver
getXPathFunctionResolver()

Return the current function resolver.

null

is returned in no function resolver is in effect.

**Returns:**
- Current function resolver.

---

#### void setNamespaceContext​(
NamespaceContext
nsContext)

Establish a namespace context.

A

NullPointerException

is thrown if

nsContext

is

null

.

**Parameters:**
- nsContext

- Namespace context to use.

**Throws:**
- NullPointerException

- If

nsContext

is

null

.

---

#### NamespaceContext
getNamespaceContext()

Return the current namespace context.

null

is returned in no namespace context is in effect.

**Returns:**
- Current Namespace context.

---

#### XPathExpression
compile​(
String
expression)
throws
XPathExpressionException

Compile an XPath expression for later evaluation.

If

expression

contains any

XPathFunction

s,
they must be available via the

XPathFunctionResolver

.
An

XPathExpressionException

will be thrown if the

XPathFunction

cannot be resovled with the

XPathFunctionResolver

.

If

expression

contains any variables, the

XPathVariableResolver

in effect

at compile time

will be used to resolve them.

**Parameters:**
- expression

- The XPath expression.

**Returns:**
- Compiled XPath expression.

**Throws:**
- XPathExpressionException

- If

expression

cannot be compiled.
- NullPointerException

- If

expression

is

null

.

---

#### Object
evaluate​(
String
expression,

Object
item,

QName
returnType)
throws
XPathExpressionException

Evaluate an

XPath

expression in the specified context and
return the result as the specified type.

See

Evaluation of XPath Expressions

for context item evaluation, variable, function and

QName

resolution
and return type conversion.

The parameter

item

represents the context the XPath expression
will be operated on. The type of the context is implementation-dependent.
If the value is

null

, the operation must have no dependency on
the context, otherwise an XPathExpressionException will be thrown.

**Parameters:**
- expression

- The XPath expression.
- item

- The context the XPath expression will be evaluated in.
- returnType

- The result type expected to be returned by the XPath expression.

**Returns:**
- The result of evaluating an XPath expression as an

Object

of

returnType

.

**Throws:**
- XPathExpressionException

- If

expression

cannot be evaluated.
- IllegalArgumentException

- If

returnType

is not one of the types defined in

XPathConstants

(

NUMBER

,

STRING

,

BOOLEAN

,

NODE

or

NODESET

).
- NullPointerException

- If

expression or returnType

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
String
expression,

Object
item)
throws
XPathExpressionException

Evaluate an XPath expression in the specified context and return the result as a

String

.

This method calls

evaluate(String expression, Object item, QName returnType)

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
- expression

- The XPath expression.
- item

- The context the XPath expression will be evaluated in.

**Returns:**
- The result of evaluating an XPath expression as a

String

.

**Throws:**
- XPathExpressionException

- If

expression

cannot be evaluated.
- NullPointerException

- If

expression

is

null

.

**Implementation Note:**
- The type of the context is usually

Node

.

---

#### Object
evaluate​(
String
expression,

InputSource
source,

QName
returnType)
throws
XPathExpressionException

Evaluate an XPath expression in the context of the specified

InputSource

and return the result as the specified type.

This method builds a data model for the

InputSource

and calls

evaluate(String expression, Object item, QName returnType)

on the resulting document object.

See

Evaluation of XPath Expressions

for context item evaluation,
variable, function and QName resolution and return type conversion.

**Parameters:**
- expression

- The XPath expression.
- source

- The input source of the document to evaluate over.
- returnType

- The desired return type.

**Returns:**
- The

Object

that encapsulates the result of evaluating the expression.

**Throws:**
- XPathExpressionException

- If expression cannot be evaluated.
- IllegalArgumentException

- If

returnType

is not one of the types defined in

XPathConstants

.
- NullPointerException

- If

expression, source or returnType

is

null

.

---

#### String
evaluate​(
String
expression,

InputSource
source)
throws
XPathExpressionException

Evaluate an XPath expression in the context of the specified

InputSource

and return the result as a

String

.

This method calls

evaluate(String expression, InputSource source, QName returnType)

with a

returnType

of

XPathConstants.STRING

.

See

Evaluation of XPath Expressions

for context item evaluation,
variable, function and QName resolution and return type conversion.

**Parameters:**
- expression

- The XPath expression.
- source

- The

InputSource

of the document to evaluate over.

**Returns:**
- The

String

that is the result of evaluating the expression and
converting the result to a

String

.

**Throws:**
- XPathExpressionException

- If expression cannot be evaluated.
- NullPointerException

- If

expression or source

is

null

.

---

#### default <T> T evaluateExpression​(
String
expression,

Object
item,

Class
<T> type)
throws
XPathExpressionException

Evaluate an XPath expression in the specified context and return
the result with the type specified through the

class type

The parameter

item

represents the context the XPath expression
will be operated on. The type of the context is implementation-dependent.
If the value is

null

, the operation must have no dependency on
the context, otherwise an XPathExpressionException will be thrown.

**Parameters:**
- expression

- The XPath expression.
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

XPathEvaluationResult.XPathResultType

,
or XPathEvaluationResult is specified as the type but an implementation supporting the

ANY

type is not available.
- NullPointerException

- If

expression or type

is

null

.

**Since:**
- 9

**Implementation Requirements:**
- The default implementation in the XPath API is equivalent to:

```java
(T)evaluate(expression, item,
XPathEvaluationResult.XPathResultType.getQNameType(type));
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
String
expression,

Object
item)
throws
XPathExpressionException

Evaluate an XPath expression in the specified context. This is equivalent to
calling

evaluateExpression(String expression, Object item, Class type)

with type

XPathEvaluationResult

:

```java
evaluateExpression(expression, item, XPathEvaluationResult.class);
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
- expression

- The XPath expression.
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
- NullPointerException

- If

expression

is

null

.

**Since:**
- 9

**Implementation Requirements:**
- The default implementation in the XPath API is equivalent to:

```java
evaluateExpression(expression, item, XPathEvaluationResult.class);
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
String
expression,

InputSource
source,

Class
<T> type)
throws
XPathExpressionException

Evaluate an XPath expression in the context of the specified

source

and return the result as specified.

This method builds a data model for the

InputSource

and calls

evaluateExpression(String expression, Object item, Class type)

on the resulting document object. The data model is usually

Document

**Parameters:**
- expression

- The XPath expression.
- source

- The input source of the document to evaluate over.
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

expression, source or type

is

null

.

**Since:**
- 9

**Implementation Requirements:**
- The default implementation in the XPath API is equivalent to:

```java
(T)evaluate(expression, source,
XPathEvaluationResult.XPathResultType.getQNameType(type));
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
String
expression,

InputSource
source)
throws
XPathExpressionException

Evaluate an XPath expression in the specified context. This is equivalent to
calling

evaluateExpression(String expression, Object item, Class type)

with type

XPathEvaluationResult

:

```java
evaluateExpression(expression, item, XPathEvaluationResult.class);
```

**Parameters:**
- expression

- The XPath expression.
- source

- The input source of the document to evaluate over.

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

expression or source

is

null

.

**Since:**
- 9

**Implementation Requirements:**
- The default implementation in the XPath API is equivalent to:

```java
evaluateExpression(expression, source, XPathEvaluationResult.class);
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

#### Interface XPath

```java
public interface
XPath
```

XPath

provides access to the XPath evaluation environment and expressions.
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

set with

setXPathVariableResolver(XPathVariableResolver resolver)

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

set with

setXPathFunctionResolver(XPathFunctionResolver resolver)

.
An

XPathExpressionException

is raised if the function resolver is undefined or
the function resolver returns

null

for the function.

QNames

QNames in the expression are resolved against the XPath namespace context
set with

setNamespaceContext(NamespaceContext nsContext)

.

result

This result of evaluating an expression is converted to an instance of the desired return type.
Valid return types are defined in

XPathConstants

.
Conversion to the return type follows XPath conversion rules.

An XPath object is not thread-safe and not reentrant.
In other words, it is the application's responsibility to make
sure that one

XPath

object is not used from
more than one thread at any given time, and while the

evaluate

method is invoked, applications may not recursively call
the

evaluate

method.

**Since:** 1.5
**See Also:** XML Path Language (XPath) Version 1.0

public interface

XPath

XPath

provides access to the XPath evaluation environment and expressions.
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

set with

setXPathVariableResolver(XPathVariableResolver resolver)

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

set with

setXPathFunctionResolver(XPathFunctionResolver resolver)

.
An

XPathExpressionException

is raised if the function resolver is undefined or
the function resolver returns

null

for the function.

QNames

QNames in the expression are resolved against the XPath namespace context
set with

setNamespaceContext(NamespaceContext nsContext)

.

result

This result of evaluating an expression is converted to an instance of the desired return type.
Valid return types are defined in

XPathConstants

.
Conversion to the return type follows XPath conversion rules.

An XPath object is not thread-safe and not reentrant.
In other words, it is the application's responsibility to make
sure that one

XPath

object is not used from
more than one thread at any given time, and while the

evaluate

method is invoked, applications may not recursively call
the

evaluate

method.

An XPath object is not thread-safe and not reentrant.
In other words, it is the application's responsibility to make
sure that one

XPath

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

XPathExpression

compile

​(

String

expression)

Compile an XPath expression for later evaluation.

String

evaluate

​(

String

expression,

Object

item)

Evaluate an XPath expression in the specified context and return the result as a

String

.

Object

evaluate

​(

String

expression,

Object

item,

QName

returnType)

Evaluate an

XPath

expression in the specified context and
return the result as the specified type.

String

evaluate

​(

String

expression,

InputSource

source)

Evaluate an XPath expression in the context of the specified

InputSource

and return the result as a

String

.

Object

evaluate

​(

String

expression,

InputSource

source,

QName

returnType)

Evaluate an XPath expression in the context of the specified

InputSource

and return the result as the specified type.

default

XPathEvaluationResult

<?>

evaluateExpression

​(

String

expression,

Object

item)

Evaluate an XPath expression in the specified context.

default <T> T

evaluateExpression

​(

String

expression,

Object

item,

Class

<T> type)

Evaluate an XPath expression in the specified context and return
the result with the type specified through the

class type

default

XPathEvaluationResult

<?>

evaluateExpression

​(

String

expression,

InputSource

source)

Evaluate an XPath expression in the specified context.

default <T> T

evaluateExpression

​(

String

expression,

InputSource

source,

Class

<T> type)

Evaluate an XPath expression in the context of the specified

source

and return the result as specified.

NamespaceContext

getNamespaceContext

()

Return the current namespace context.

XPathFunctionResolver

getXPathFunctionResolver

()

Return the current function resolver.

XPathVariableResolver

getXPathVariableResolver

()

Return the current variable resolver.

void

reset

()

Reset this

XPath

to its original configuration.

void

setNamespaceContext

​(

NamespaceContext

nsContext)

Establish a namespace context.

void

setXPathFunctionResolver

​(

XPathFunctionResolver

resolver)

Establish a function resolver.

void

setXPathVariableResolver

​(

XPathVariableResolver

resolver)

Establish a variable resolver.

Method Summary

All Methods

Instance Methods

Abstract Methods

Default Methods

Modifier and Type

Method

Description

XPathExpression

compile

​(

String

expression)

Compile an XPath expression for later evaluation.

String

evaluate

​(

String

expression,

Object

item)

Evaluate an XPath expression in the specified context and return the result as a

String

.

Object

evaluate

​(

String

expression,

Object

item,

QName

returnType)

Evaluate an

XPath

expression in the specified context and
return the result as the specified type.

String

evaluate

​(

String

expression,

InputSource

source)

Evaluate an XPath expression in the context of the specified

InputSource

and return the result as a

String

.

Object

evaluate

​(

String

expression,

InputSource

source,

QName

returnType)

Evaluate an XPath expression in the context of the specified

InputSource

and return the result as the specified type.

default

XPathEvaluationResult

<?>

evaluateExpression

​(

String

expression,

Object

item)

Evaluate an XPath expression in the specified context.

default <T> T

evaluateExpression

​(

String

expression,

Object

item,

Class

<T> type)

Evaluate an XPath expression in the specified context and return
the result with the type specified through the

class type

default

XPathEvaluationResult

<?>

evaluateExpression

​(

String

expression,

InputSource

source)

Evaluate an XPath expression in the specified context.

default <T> T

evaluateExpression

​(

String

expression,

InputSource

source,

Class

<T> type)

Evaluate an XPath expression in the context of the specified

source

and return the result as specified.

NamespaceContext

getNamespaceContext

()

Return the current namespace context.

XPathFunctionResolver

getXPathFunctionResolver

()

Return the current function resolver.

XPathVariableResolver

getXPathVariableResolver

()

Return the current variable resolver.

void

reset

()

Reset this

XPath

to its original configuration.

void

setNamespaceContext

​(

NamespaceContext

nsContext)

Establish a namespace context.

void

setXPathFunctionResolver

​(

XPathFunctionResolver

resolver)

Establish a function resolver.

void

setXPathVariableResolver

​(

XPathVariableResolver

resolver)

Establish a variable resolver.

---

#### Method Summary

Compile an XPath expression for later evaluation.

Evaluate an XPath expression in the specified context and return the result as a

String

.

Evaluate an

XPath

expression in the specified context and
return the result as the specified type.

Evaluate an XPath expression in the context of the specified

InputSource

and return the result as a

String

.

Evaluate an XPath expression in the context of the specified

InputSource

and return the result as the specified type.

Evaluate an XPath expression in the specified context.

Evaluate an XPath expression in the specified context and return
the result with the type specified through the

class type

Evaluate an XPath expression in the context of the specified

source

and return the result as specified.

Return the current namespace context.

Return the current function resolver.

Return the current variable resolver.

Reset this

XPath

to its original configuration.

Establish a namespace context.

Establish a function resolver.

Establish a variable resolver.

============ METHOD DETAIL ==========

- Method Detail

- reset

```java
void reset()
```

Reset this

XPath

to its original configuration.

XPath

is reset to the same state as when it was created with

XPathFactory.newXPath()

.

reset()

is designed to allow the reuse of existing

XPath

s
thus saving resources associated with the creation of new

XPath

s.

The reset

XPath

is not guaranteed to have the same

XPathFunctionResolver

,

XPathVariableResolver

or

NamespaceContext

Object

s, e.g.

Object.equals(Object obj)

.
It is guaranteed to have a functionally equal

XPathFunctionResolver

,

XPathVariableResolver

and

NamespaceContext

.

- setXPathVariableResolver

```java
void setXPathVariableResolver​(
XPathVariableResolver
resolver)
```

Establish a variable resolver.

A

NullPointerException

is thrown if

resolver

is

null

.

**Parameters:** resolver

- Variable resolver.
**Throws:** NullPointerException

- If

resolver

is

null

.

- getXPathVariableResolver

```java
XPathVariableResolver
getXPathVariableResolver()
```

Return the current variable resolver.

null

is returned in no variable resolver is in effect.

**Returns:** Current variable resolver.

- setXPathFunctionResolver

```java
void setXPathFunctionResolver​(
XPathFunctionResolver
resolver)
```

Establish a function resolver.

A

NullPointerException

is thrown if

resolver

is

null

.

**Parameters:** resolver

- XPath function resolver.
**Throws:** NullPointerException

- If

resolver

is

null

.

- getXPathFunctionResolver

```java
XPathFunctionResolver
getXPathFunctionResolver()
```

Return the current function resolver.

null

is returned in no function resolver is in effect.

**Returns:** Current function resolver.

- setNamespaceContext

```java
void setNamespaceContext​(
NamespaceContext
nsContext)
```

Establish a namespace context.

A

NullPointerException

is thrown if

nsContext

is

null

.

**Parameters:** nsContext

- Namespace context to use.
**Throws:** NullPointerException

- If

nsContext

is

null

.

- getNamespaceContext

```java
NamespaceContext
getNamespaceContext()
```

Return the current namespace context.

null

is returned in no namespace context is in effect.

**Returns:** Current Namespace context.

- compile

```java
XPathExpression
compile​(
String
expression)
throws
XPathExpressionException
```

Compile an XPath expression for later evaluation.

If

expression

contains any

XPathFunction

s,
they must be available via the

XPathFunctionResolver

.
An

XPathExpressionException

will be thrown if the

XPathFunction

cannot be resovled with the

XPathFunctionResolver

.

If

expression

contains any variables, the

XPathVariableResolver

in effect

at compile time

will be used to resolve them.

**Parameters:** expression

- The XPath expression.
**Returns:** Compiled XPath expression.
**Throws:** XPathExpressionException

- If

expression

cannot be compiled.
**Throws:** NullPointerException

- If

expression

is

null

.

- evaluate

```java
Object
evaluate​(
String
expression,

Object
item,

QName
returnType)
throws
XPathExpressionException
```

Evaluate an

XPath

expression in the specified context and
return the result as the specified type.

See

Evaluation of XPath Expressions

for context item evaluation, variable, function and

QName

resolution
and return type conversion.

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
**Parameters:** expression

- The XPath expression.
**Parameters:** item

- The context the XPath expression will be evaluated in.
**Parameters:** returnType

- The result type expected to be returned by the XPath expression.
**Returns:** The result of evaluating an XPath expression as an

Object

of

returnType

.
**Throws:** XPathExpressionException

- If

expression

cannot be evaluated.
**Throws:** IllegalArgumentException

- If

returnType

is not one of the types defined in

XPathConstants

(

NUMBER

,

STRING

,

BOOLEAN

,

NODE

or

NODESET

).
**Throws:** NullPointerException

- If

expression or returnType

is

null

.

- evaluate

```java
String
evaluate​(
String
expression,

Object
item)
throws
XPathExpressionException
```

Evaluate an XPath expression in the specified context and return the result as a

String

.

This method calls

evaluate(String expression, Object item, QName returnType)

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
**Parameters:** expression

- The XPath expression.
**Parameters:** item

- The context the XPath expression will be evaluated in.
**Returns:** The result of evaluating an XPath expression as a

String

.
**Throws:** XPathExpressionException

- If

expression

cannot be evaluated.
**Throws:** NullPointerException

- If

expression

is

null

.

- evaluate

```java
Object
evaluate​(
String
expression,

InputSource
source,

QName
returnType)
throws
XPathExpressionException
```

Evaluate an XPath expression in the context of the specified

InputSource

and return the result as the specified type.

This method builds a data model for the

InputSource

and calls

evaluate(String expression, Object item, QName returnType)

on the resulting document object.

See

Evaluation of XPath Expressions

for context item evaluation,
variable, function and QName resolution and return type conversion.

**Parameters:** expression

- The XPath expression.
**Parameters:** source

- The input source of the document to evaluate over.
**Parameters:** returnType

- The desired return type.
**Returns:** The

Object

that encapsulates the result of evaluating the expression.
**Throws:** XPathExpressionException

- If expression cannot be evaluated.
**Throws:** IllegalArgumentException

- If

returnType

is not one of the types defined in

XPathConstants

.
**Throws:** NullPointerException

- If

expression, source or returnType

is

null

.

- evaluate

```java
String
evaluate​(
String
expression,

InputSource
source)
throws
XPathExpressionException
```

Evaluate an XPath expression in the context of the specified

InputSource

and return the result as a

String

.

This method calls

evaluate(String expression, InputSource source, QName returnType)

with a

returnType

of

XPathConstants.STRING

.

See

Evaluation of XPath Expressions

for context item evaluation,
variable, function and QName resolution and return type conversion.

**Parameters:** expression

- The XPath expression.
**Parameters:** source

- The

InputSource

of the document to evaluate over.
**Returns:** The

String

that is the result of evaluating the expression and
converting the result to a

String

.
**Throws:** XPathExpressionException

- If expression cannot be evaluated.
**Throws:** NullPointerException

- If

expression or source

is

null

.

- evaluateExpression

```java
default <T> T evaluateExpression​(
String
expression,

Object
item,

Class
<T> type)
throws
XPathExpressionException
```

Evaluate an XPath expression in the specified context and return
the result with the type specified through the

class type

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
(T)evaluate(expression, item,
XPathEvaluationResult.XPathResultType.getQNameType(type));
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
**Parameters:** expression

- The XPath expression.
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

XPathEvaluationResult.XPathResultType

,
or XPathEvaluationResult is specified as the type but an implementation supporting the

ANY

type is not available.
**Throws:** NullPointerException

- If

expression or type

is

null

.
**Since:** 9

- evaluateExpression

```java
default
XPathEvaluationResult
<?> evaluateExpression​(
String
expression,

Object
item)
throws
XPathExpressionException
```

Evaluate an XPath expression in the specified context. This is equivalent to
calling

evaluateExpression(String expression, Object item, Class type)

with type

XPathEvaluationResult

:

```java
evaluateExpression(expression, item, XPathEvaluationResult.class);
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
evaluateExpression(expression, item, XPathEvaluationResult.class);
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
**Parameters:** expression

- The XPath expression.
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
**Throws:** NullPointerException

- If

expression

is

null

.
**Since:** 9

- evaluateExpression

```java
default <T> T evaluateExpression​(
String
expression,

InputSource
source,

Class
<T> type)
throws
XPathExpressionException
```

Evaluate an XPath expression in the context of the specified

source

and return the result as specified.

This method builds a data model for the

InputSource

and calls

evaluateExpression(String expression, Object item, Class type)

on the resulting document object. The data model is usually

Document

**Implementation Requirements:** The default implementation in the XPath API is equivalent to:

```java
(T)evaluate(expression, source,
XPathEvaluationResult.XPathResultType.getQNameType(type));
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
**Parameters:** expression

- The XPath expression.
**Parameters:** source

- The input source of the document to evaluate over.
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

expression, source or type

is

null

.
**Since:** 9

- evaluateExpression

```java
default
XPathEvaluationResult
<?> evaluateExpression​(
String
expression,

InputSource
source)
throws
XPathExpressionException
```

Evaluate an XPath expression in the specified context. This is equivalent to
calling

evaluateExpression(String expression, Object item, Class type)

with type

XPathEvaluationResult

:

```java
evaluateExpression(expression, item, XPathEvaluationResult.class);
```

**Implementation Requirements:** The default implementation in the XPath API is equivalent to:

```java
evaluateExpression(expression, source, XPathEvaluationResult.class);
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
**Parameters:** expression

- The XPath expression.
**Parameters:** source

- The input source of the document to evaluate over.
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

expression or source

is

null

.
**Since:** 9

Method Detail

- reset

```java
void reset()
```

Reset this

XPath

to its original configuration.

XPath

is reset to the same state as when it was created with

XPathFactory.newXPath()

.

reset()

is designed to allow the reuse of existing

XPath

s
thus saving resources associated with the creation of new

XPath

s.

The reset

XPath

is not guaranteed to have the same

XPathFunctionResolver

,

XPathVariableResolver

or

NamespaceContext

Object

s, e.g.

Object.equals(Object obj)

.
It is guaranteed to have a functionally equal

XPathFunctionResolver

,

XPathVariableResolver

and

NamespaceContext

.

- setXPathVariableResolver

```java
void setXPathVariableResolver​(
XPathVariableResolver
resolver)
```

Establish a variable resolver.

A

NullPointerException

is thrown if

resolver

is

null

.

**Parameters:** resolver

- Variable resolver.
**Throws:** NullPointerException

- If

resolver

is

null

.

- getXPathVariableResolver

```java
XPathVariableResolver
getXPathVariableResolver()
```

Return the current variable resolver.

null

is returned in no variable resolver is in effect.

**Returns:** Current variable resolver.

- setXPathFunctionResolver

```java
void setXPathFunctionResolver​(
XPathFunctionResolver
resolver)
```

Establish a function resolver.

A

NullPointerException

is thrown if

resolver

is

null

.

**Parameters:** resolver

- XPath function resolver.
**Throws:** NullPointerException

- If

resolver

is

null

.

- getXPathFunctionResolver

```java
XPathFunctionResolver
getXPathFunctionResolver()
```

Return the current function resolver.

null

is returned in no function resolver is in effect.

**Returns:** Current function resolver.

- setNamespaceContext

```java
void setNamespaceContext​(
NamespaceContext
nsContext)
```

Establish a namespace context.

A

NullPointerException

is thrown if

nsContext

is

null

.

**Parameters:** nsContext

- Namespace context to use.
**Throws:** NullPointerException

- If

nsContext

is

null

.

- getNamespaceContext

```java
NamespaceContext
getNamespaceContext()
```

Return the current namespace context.

null

is returned in no namespace context is in effect.

**Returns:** Current Namespace context.

- compile

```java
XPathExpression
compile​(
String
expression)
throws
XPathExpressionException
```

Compile an XPath expression for later evaluation.

If

expression

contains any

XPathFunction

s,
they must be available via the

XPathFunctionResolver

.
An

XPathExpressionException

will be thrown if the

XPathFunction

cannot be resovled with the

XPathFunctionResolver

.

If

expression

contains any variables, the

XPathVariableResolver

in effect

at compile time

will be used to resolve them.

**Parameters:** expression

- The XPath expression.
**Returns:** Compiled XPath expression.
**Throws:** XPathExpressionException

- If

expression

cannot be compiled.
**Throws:** NullPointerException

- If

expression

is

null

.

- evaluate

```java
Object
evaluate​(
String
expression,

Object
item,

QName
returnType)
throws
XPathExpressionException
```

Evaluate an

XPath

expression in the specified context and
return the result as the specified type.

See

Evaluation of XPath Expressions

for context item evaluation, variable, function and

QName

resolution
and return type conversion.

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
**Parameters:** expression

- The XPath expression.
**Parameters:** item

- The context the XPath expression will be evaluated in.
**Parameters:** returnType

- The result type expected to be returned by the XPath expression.
**Returns:** The result of evaluating an XPath expression as an

Object

of

returnType

.
**Throws:** XPathExpressionException

- If

expression

cannot be evaluated.
**Throws:** IllegalArgumentException

- If

returnType

is not one of the types defined in

XPathConstants

(

NUMBER

,

STRING

,

BOOLEAN

,

NODE

or

NODESET

).
**Throws:** NullPointerException

- If

expression or returnType

is

null

.

- evaluate

```java
String
evaluate​(
String
expression,

Object
item)
throws
XPathExpressionException
```

Evaluate an XPath expression in the specified context and return the result as a

String

.

This method calls

evaluate(String expression, Object item, QName returnType)

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
**Parameters:** expression

- The XPath expression.
**Parameters:** item

- The context the XPath expression will be evaluated in.
**Returns:** The result of evaluating an XPath expression as a

String

.
**Throws:** XPathExpressionException

- If

expression

cannot be evaluated.
**Throws:** NullPointerException

- If

expression

is

null

.

- evaluate

```java
Object
evaluate​(
String
expression,

InputSource
source,

QName
returnType)
throws
XPathExpressionException
```

Evaluate an XPath expression in the context of the specified

InputSource

and return the result as the specified type.

This method builds a data model for the

InputSource

and calls

evaluate(String expression, Object item, QName returnType)

on the resulting document object.

See

Evaluation of XPath Expressions

for context item evaluation,
variable, function and QName resolution and return type conversion.

**Parameters:** expression

- The XPath expression.
**Parameters:** source

- The input source of the document to evaluate over.
**Parameters:** returnType

- The desired return type.
**Returns:** The

Object

that encapsulates the result of evaluating the expression.
**Throws:** XPathExpressionException

- If expression cannot be evaluated.
**Throws:** IllegalArgumentException

- If

returnType

is not one of the types defined in

XPathConstants

.
**Throws:** NullPointerException

- If

expression, source or returnType

is

null

.

- evaluate

```java
String
evaluate​(
String
expression,

InputSource
source)
throws
XPathExpressionException
```

Evaluate an XPath expression in the context of the specified

InputSource

and return the result as a

String

.

This method calls

evaluate(String expression, InputSource source, QName returnType)

with a

returnType

of

XPathConstants.STRING

.

See

Evaluation of XPath Expressions

for context item evaluation,
variable, function and QName resolution and return type conversion.

**Parameters:** expression

- The XPath expression.
**Parameters:** source

- The

InputSource

of the document to evaluate over.
**Returns:** The

String

that is the result of evaluating the expression and
converting the result to a

String

.
**Throws:** XPathExpressionException

- If expression cannot be evaluated.
**Throws:** NullPointerException

- If

expression or source

is

null

.

- evaluateExpression

```java
default <T> T evaluateExpression​(
String
expression,

Object
item,

Class
<T> type)
throws
XPathExpressionException
```

Evaluate an XPath expression in the specified context and return
the result with the type specified through the

class type

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
(T)evaluate(expression, item,
XPathEvaluationResult.XPathResultType.getQNameType(type));
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
**Parameters:** expression

- The XPath expression.
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

XPathEvaluationResult.XPathResultType

,
or XPathEvaluationResult is specified as the type but an implementation supporting the

ANY

type is not available.
**Throws:** NullPointerException

- If

expression or type

is

null

.
**Since:** 9

- evaluateExpression

```java
default
XPathEvaluationResult
<?> evaluateExpression​(
String
expression,

Object
item)
throws
XPathExpressionException
```

Evaluate an XPath expression in the specified context. This is equivalent to
calling

evaluateExpression(String expression, Object item, Class type)

with type

XPathEvaluationResult

:

```java
evaluateExpression(expression, item, XPathEvaluationResult.class);
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
evaluateExpression(expression, item, XPathEvaluationResult.class);
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
**Parameters:** expression

- The XPath expression.
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
**Throws:** NullPointerException

- If

expression

is

null

.
**Since:** 9

- evaluateExpression

```java
default <T> T evaluateExpression​(
String
expression,

InputSource
source,

Class
<T> type)
throws
XPathExpressionException
```

Evaluate an XPath expression in the context of the specified

source

and return the result as specified.

This method builds a data model for the

InputSource

and calls

evaluateExpression(String expression, Object item, Class type)

on the resulting document object. The data model is usually

Document

**Implementation Requirements:** The default implementation in the XPath API is equivalent to:

```java
(T)evaluate(expression, source,
XPathEvaluationResult.XPathResultType.getQNameType(type));
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
**Parameters:** expression

- The XPath expression.
**Parameters:** source

- The input source of the document to evaluate over.
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

expression, source or type

is

null

.
**Since:** 9

- evaluateExpression

```java
default
XPathEvaluationResult
<?> evaluateExpression​(
String
expression,

InputSource
source)
throws
XPathExpressionException
```

Evaluate an XPath expression in the specified context. This is equivalent to
calling

evaluateExpression(String expression, Object item, Class type)

with type

XPathEvaluationResult

:

```java
evaluateExpression(expression, item, XPathEvaluationResult.class);
```

**Implementation Requirements:** The default implementation in the XPath API is equivalent to:

```java
evaluateExpression(expression, source, XPathEvaluationResult.class);
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
**Parameters:** expression

- The XPath expression.
**Parameters:** source

- The input source of the document to evaluate over.
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

expression or source

is

null

.
**Since:** 9

---

#### Method Detail

reset

```java
void reset()
```

Reset this

XPath

to its original configuration.

XPath

is reset to the same state as when it was created with

XPathFactory.newXPath()

.

reset()

is designed to allow the reuse of existing

XPath

s
thus saving resources associated with the creation of new

XPath

s.

The reset

XPath

is not guaranteed to have the same

XPathFunctionResolver

,

XPathVariableResolver

or

NamespaceContext

Object

s, e.g.

Object.equals(Object obj)

.
It is guaranteed to have a functionally equal

XPathFunctionResolver

,

XPathVariableResolver

and

NamespaceContext

.

---

#### reset

void reset()

Reset this

XPath

to its original configuration.

XPath

is reset to the same state as when it was created with

XPathFactory.newXPath()

.

reset()

is designed to allow the reuse of existing

XPath

s
thus saving resources associated with the creation of new

XPath

s.

The reset

XPath

is not guaranteed to have the same

XPathFunctionResolver

,

XPathVariableResolver

or

NamespaceContext

Object

s, e.g.

Object.equals(Object obj)

.
It is guaranteed to have a functionally equal

XPathFunctionResolver

,

XPathVariableResolver

and

NamespaceContext

.

XPath

is reset to the same state as when it was created with

XPathFactory.newXPath()

.

reset()

is designed to allow the reuse of existing

XPath

s
thus saving resources associated with the creation of new

XPath

s.

The reset

XPath

is not guaranteed to have the same

XPathFunctionResolver

,

XPathVariableResolver

or

NamespaceContext

Object

s, e.g.

Object.equals(Object obj)

.
It is guaranteed to have a functionally equal

XPathFunctionResolver

,

XPathVariableResolver

and

NamespaceContext

.

The reset

XPath

is not guaranteed to have the same

XPathFunctionResolver

,

XPathVariableResolver

or

NamespaceContext

Object

s, e.g.

Object.equals(Object obj)

.
It is guaranteed to have a functionally equal

XPathFunctionResolver

,

XPathVariableResolver

and

NamespaceContext

.

setXPathVariableResolver

```java
void setXPathVariableResolver​(
XPathVariableResolver
resolver)
```

Establish a variable resolver.

A

NullPointerException

is thrown if

resolver

is

null

.

**Parameters:** resolver

- Variable resolver.
**Throws:** NullPointerException

- If

resolver

is

null

.

---

#### setXPathVariableResolver

void setXPathVariableResolver​(

XPathVariableResolver

resolver)

Establish a variable resolver.

A

NullPointerException

is thrown if

resolver

is

null

.

A

NullPointerException

is thrown if

resolver

is

null

.

getXPathVariableResolver

```java
XPathVariableResolver
getXPathVariableResolver()
```

Return the current variable resolver.

null

is returned in no variable resolver is in effect.

**Returns:** Current variable resolver.

---

#### getXPathVariableResolver

XPathVariableResolver

getXPathVariableResolver()

Return the current variable resolver.

null

is returned in no variable resolver is in effect.

null

is returned in no variable resolver is in effect.

setXPathFunctionResolver

```java
void setXPathFunctionResolver​(
XPathFunctionResolver
resolver)
```

Establish a function resolver.

A

NullPointerException

is thrown if

resolver

is

null

.

**Parameters:** resolver

- XPath function resolver.
**Throws:** NullPointerException

- If

resolver

is

null

.

---

#### setXPathFunctionResolver

void setXPathFunctionResolver​(

XPathFunctionResolver

resolver)

Establish a function resolver.

A

NullPointerException

is thrown if

resolver

is

null

.

A

NullPointerException

is thrown if

resolver

is

null

.

getXPathFunctionResolver

```java
XPathFunctionResolver
getXPathFunctionResolver()
```

Return the current function resolver.

null

is returned in no function resolver is in effect.

**Returns:** Current function resolver.

---

#### getXPathFunctionResolver

XPathFunctionResolver

getXPathFunctionResolver()

Return the current function resolver.

null

is returned in no function resolver is in effect.

null

is returned in no function resolver is in effect.

setNamespaceContext

```java
void setNamespaceContext​(
NamespaceContext
nsContext)
```

Establish a namespace context.

A

NullPointerException

is thrown if

nsContext

is

null

.

**Parameters:** nsContext

- Namespace context to use.
**Throws:** NullPointerException

- If

nsContext

is

null

.

---

#### setNamespaceContext

void setNamespaceContext​(

NamespaceContext

nsContext)

Establish a namespace context.

A

NullPointerException

is thrown if

nsContext

is

null

.

A

NullPointerException

is thrown if

nsContext

is

null

.

getNamespaceContext

```java
NamespaceContext
getNamespaceContext()
```

Return the current namespace context.

null

is returned in no namespace context is in effect.

**Returns:** Current Namespace context.

---

#### getNamespaceContext

NamespaceContext

getNamespaceContext()

Return the current namespace context.

null

is returned in no namespace context is in effect.

null

is returned in no namespace context is in effect.

compile

```java
XPathExpression
compile​(
String
expression)
throws
XPathExpressionException
```

Compile an XPath expression for later evaluation.

If

expression

contains any

XPathFunction

s,
they must be available via the

XPathFunctionResolver

.
An

XPathExpressionException

will be thrown if the

XPathFunction

cannot be resovled with the

XPathFunctionResolver

.

If

expression

contains any variables, the

XPathVariableResolver

in effect

at compile time

will be used to resolve them.

**Parameters:** expression

- The XPath expression.
**Returns:** Compiled XPath expression.
**Throws:** XPathExpressionException

- If

expression

cannot be compiled.
**Throws:** NullPointerException

- If

expression

is

null

.

---

#### compile

XPathExpression

compile​(

String

expression)
throws

XPathExpressionException

Compile an XPath expression for later evaluation.

If

expression

contains any

XPathFunction

s,
they must be available via the

XPathFunctionResolver

.
An

XPathExpressionException

will be thrown if the

XPathFunction

cannot be resovled with the

XPathFunctionResolver

.

If

expression

contains any variables, the

XPathVariableResolver

in effect

at compile time

will be used to resolve them.

If

expression

contains any

XPathFunction

s,
they must be available via the

XPathFunctionResolver

.
An

XPathExpressionException

will be thrown if the

XPathFunction

cannot be resovled with the

XPathFunctionResolver

.

If

expression

contains any variables, the

XPathVariableResolver

in effect

at compile time

will be used to resolve them.

If

expression

contains any variables, the

XPathVariableResolver

in effect

at compile time

will be used to resolve them.

evaluate

```java
Object
evaluate​(
String
expression,

Object
item,

QName
returnType)
throws
XPathExpressionException
```

Evaluate an

XPath

expression in the specified context and
return the result as the specified type.

See

Evaluation of XPath Expressions

for context item evaluation, variable, function and

QName

resolution
and return type conversion.

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
**Parameters:** expression

- The XPath expression.
**Parameters:** item

- The context the XPath expression will be evaluated in.
**Parameters:** returnType

- The result type expected to be returned by the XPath expression.
**Returns:** The result of evaluating an XPath expression as an

Object

of

returnType

.
**Throws:** XPathExpressionException

- If

expression

cannot be evaluated.
**Throws:** IllegalArgumentException

- If

returnType

is not one of the types defined in

XPathConstants

(

NUMBER

,

STRING

,

BOOLEAN

,

NODE

or

NODESET

).
**Throws:** NullPointerException

- If

expression or returnType

is

null

.

---

#### evaluate

Object

evaluate​(

String

expression,

Object

item,

QName

returnType)
throws

XPathExpressionException

Evaluate an

XPath

expression in the specified context and
return the result as the specified type.

See

Evaluation of XPath Expressions

for context item evaluation, variable, function and

QName

resolution
and return type conversion.

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

for context item evaluation, variable, function and

QName

resolution
and return type conversion.

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
String
expression,

Object
item)
throws
XPathExpressionException
```

Evaluate an XPath expression in the specified context and return the result as a

String

.

This method calls

evaluate(String expression, Object item, QName returnType)

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
**Parameters:** expression

- The XPath expression.
**Parameters:** item

- The context the XPath expression will be evaluated in.
**Returns:** The result of evaluating an XPath expression as a

String

.
**Throws:** XPathExpressionException

- If

expression

cannot be evaluated.
**Throws:** NullPointerException

- If

expression

is

null

.

---

#### evaluate

String

evaluate​(

String

expression,

Object

item)
throws

XPathExpressionException

Evaluate an XPath expression in the specified context and return the result as a

String

.

This method calls

evaluate(String expression, Object item, QName returnType)

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

evaluate(String expression, Object item, QName returnType)

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
String
expression,

InputSource
source,

QName
returnType)
throws
XPathExpressionException
```

Evaluate an XPath expression in the context of the specified

InputSource

and return the result as the specified type.

This method builds a data model for the

InputSource

and calls

evaluate(String expression, Object item, QName returnType)

on the resulting document object.

See

Evaluation of XPath Expressions

for context item evaluation,
variable, function and QName resolution and return type conversion.

**Parameters:** expression

- The XPath expression.
**Parameters:** source

- The input source of the document to evaluate over.
**Parameters:** returnType

- The desired return type.
**Returns:** The

Object

that encapsulates the result of evaluating the expression.
**Throws:** XPathExpressionException

- If expression cannot be evaluated.
**Throws:** IllegalArgumentException

- If

returnType

is not one of the types defined in

XPathConstants

.
**Throws:** NullPointerException

- If

expression, source or returnType

is

null

.

---

#### evaluate

Object

evaluate​(

String

expression,

InputSource

source,

QName

returnType)
throws

XPathExpressionException

Evaluate an XPath expression in the context of the specified

InputSource

and return the result as the specified type.

This method builds a data model for the

InputSource

and calls

evaluate(String expression, Object item, QName returnType)

on the resulting document object.

See

Evaluation of XPath Expressions

for context item evaluation,
variable, function and QName resolution and return type conversion.

This method builds a data model for the

InputSource

and calls

evaluate(String expression, Object item, QName returnType)

on the resulting document object.

See

Evaluation of XPath Expressions

for context item evaluation,
variable, function and QName resolution and return type conversion.

See

Evaluation of XPath Expressions

for context item evaluation,
variable, function and QName resolution and return type conversion.

evaluate

```java
String
evaluate​(
String
expression,

InputSource
source)
throws
XPathExpressionException
```

Evaluate an XPath expression in the context of the specified

InputSource

and return the result as a

String

.

This method calls

evaluate(String expression, InputSource source, QName returnType)

with a

returnType

of

XPathConstants.STRING

.

See

Evaluation of XPath Expressions

for context item evaluation,
variable, function and QName resolution and return type conversion.

**Parameters:** expression

- The XPath expression.
**Parameters:** source

- The

InputSource

of the document to evaluate over.
**Returns:** The

String

that is the result of evaluating the expression and
converting the result to a

String

.
**Throws:** XPathExpressionException

- If expression cannot be evaluated.
**Throws:** NullPointerException

- If

expression or source

is

null

.

---

#### evaluate

String

evaluate​(

String

expression,

InputSource

source)
throws

XPathExpressionException

Evaluate an XPath expression in the context of the specified

InputSource

and return the result as a

String

.

This method calls

evaluate(String expression, InputSource source, QName returnType)

with a

returnType

of

XPathConstants.STRING

.

See

Evaluation of XPath Expressions

for context item evaluation,
variable, function and QName resolution and return type conversion.

This method calls

evaluate(String expression, InputSource source, QName returnType)

with a

returnType

of

XPathConstants.STRING

.

See

Evaluation of XPath Expressions

for context item evaluation,
variable, function and QName resolution and return type conversion.

See

Evaluation of XPath Expressions

for context item evaluation,
variable, function and QName resolution and return type conversion.

evaluateExpression

```java
default <T> T evaluateExpression​(
String
expression,

Object
item,

Class
<T> type)
throws
XPathExpressionException
```

Evaluate an XPath expression in the specified context and return
the result with the type specified through the

class type

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
(T)evaluate(expression, item,
XPathEvaluationResult.XPathResultType.getQNameType(type));
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
**Parameters:** expression

- The XPath expression.
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

XPathEvaluationResult.XPathResultType

,
or XPathEvaluationResult is specified as the type but an implementation supporting the

ANY

type is not available.
**Throws:** NullPointerException

- If

expression or type

is

null

.
**Since:** 9

---

#### evaluateExpression

default <T> T evaluateExpression​(

String

expression,

Object

item,

Class

<T> type)
throws

XPathExpressionException

Evaluate an XPath expression in the specified context and return
the result with the type specified through the

class type

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

(T)evaluate(expression, item,
XPathEvaluationResult.XPathResultType.getQNameType(type));

evaluateExpression

```java
default
XPathEvaluationResult
<?> evaluateExpression​(
String
expression,

Object
item)
throws
XPathExpressionException
```

Evaluate an XPath expression in the specified context. This is equivalent to
calling

evaluateExpression(String expression, Object item, Class type)

with type

XPathEvaluationResult

:

```java
evaluateExpression(expression, item, XPathEvaluationResult.class);
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
evaluateExpression(expression, item, XPathEvaluationResult.class);
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
**Parameters:** expression

- The XPath expression.
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
**Throws:** NullPointerException

- If

expression

is

null

.
**Since:** 9

---

#### evaluateExpression

default

XPathEvaluationResult

<?> evaluateExpression​(

String

expression,

Object

item)
throws

XPathExpressionException

Evaluate an XPath expression in the specified context. This is equivalent to
calling

evaluateExpression(String expression, Object item, Class type)

with type

XPathEvaluationResult

:

```java
evaluateExpression(expression, item, XPathEvaluationResult.class);
```

The parameter

item

represents the context the XPath expression
will be operated on. The type of the context is implementation-dependent.
If the value is

null

, the operation must have no dependency on
the context, otherwise an XPathExpressionException will be thrown.

evaluateExpression(expression, item, XPathEvaluationResult.class);

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
String
expression,

InputSource
source,

Class
<T> type)
throws
XPathExpressionException
```

Evaluate an XPath expression in the context of the specified

source

and return the result as specified.

This method builds a data model for the

InputSource

and calls

evaluateExpression(String expression, Object item, Class type)

on the resulting document object. The data model is usually

Document

**Implementation Requirements:** The default implementation in the XPath API is equivalent to:

```java
(T)evaluate(expression, source,
XPathEvaluationResult.XPathResultType.getQNameType(type));
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
**Parameters:** expression

- The XPath expression.
**Parameters:** source

- The input source of the document to evaluate over.
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

expression, source or type

is

null

.
**Since:** 9

---

#### evaluateExpression

default <T> T evaluateExpression​(

String

expression,

InputSource

source,

Class

<T> type)
throws

XPathExpressionException

Evaluate an XPath expression in the context of the specified

source

and return the result as specified.

This method builds a data model for the

InputSource

and calls

evaluateExpression(String expression, Object item, Class type)

on the resulting document object. The data model is usually

Document

This method builds a data model for the

InputSource

and calls

evaluateExpression(String expression, Object item, Class type)

on the resulting document object. The data model is usually

Document

(T)evaluate(expression, source,
XPathEvaluationResult.XPathResultType.getQNameType(type));

evaluateExpression

```java
default
XPathEvaluationResult
<?> evaluateExpression​(
String
expression,

InputSource
source)
throws
XPathExpressionException
```

Evaluate an XPath expression in the specified context. This is equivalent to
calling

evaluateExpression(String expression, Object item, Class type)

with type

XPathEvaluationResult

:

```java
evaluateExpression(expression, item, XPathEvaluationResult.class);
```

**Implementation Requirements:** The default implementation in the XPath API is equivalent to:

```java
evaluateExpression(expression, source, XPathEvaluationResult.class);
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
**Parameters:** expression

- The XPath expression.
**Parameters:** source

- The input source of the document to evaluate over.
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

expression or source

is

null

.
**Since:** 9

---

#### evaluateExpression

default

XPathEvaluationResult

<?> evaluateExpression​(

String

expression,

InputSource

source)
throws

XPathExpressionException

Evaluate an XPath expression in the specified context. This is equivalent to
calling

evaluateExpression(String expression, Object item, Class type)

with type

XPathEvaluationResult

:

```java
evaluateExpression(expression, item, XPathEvaluationResult.class);
```

evaluateExpression(expression, item, XPathEvaluationResult.class);

evaluateExpression(expression, source, XPathEvaluationResult.class);

---

