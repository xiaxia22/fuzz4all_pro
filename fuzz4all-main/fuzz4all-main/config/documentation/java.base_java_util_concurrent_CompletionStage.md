# Interface CompletionStage<T>

**Source:** `java.base\java\util\concurrent\CompletionStage.html`

### Class Description

```java
public interface
CompletionStage<T>
```

A stage of a possibly asynchronous computation, that performs an
action or computes a value when another CompletionStage completes.
A stage completes upon termination of its computation, but this may
in turn trigger other dependent stages. The functionality defined
in this interface takes only a few basic forms, which expand out to
a larger set of methods to capture a range of usage styles:

- The computation performed by a stage may be expressed as a
Function, Consumer, or Runnable (using methods with names including

apply

,

accept

, or

run

, respectively)
depending on whether it requires arguments and/or produces results.
For example:

```java
stage.thenApply(x -> square(x))
.thenAccept(x -> System.out.print(x))
.thenRun(() -> System.out.println());
```

An additional form (

compose

) allows the construction of
computation pipelines from functions returning completion stages.

Any argument to a stage's computation is the outcome of a
triggering stage's computation.

One stage's execution may be triggered by completion of a
single stage, or both of two stages, or either of two stages.
Dependencies on a single stage are arranged using methods with
prefix

then

. Those triggered by completion of

both

of two stages may

combine

their results or
effects, using correspondingly named methods. Those triggered by

either

of two stages make no guarantees about which of the
results or effects are used for the dependent stage's computation.

Dependencies among stages control the triggering of
computations, but do not otherwise guarantee any particular
ordering. Additionally, execution of a new stage's computations may
be arranged in any of three ways: default execution, default
asynchronous execution (using methods with suffix

async

that employ the stage's default asynchronous execution facility),
or custom (via a supplied

Executor

). The execution
properties of default and async modes are specified by
CompletionStage implementations, not this interface. Methods with
explicit Executor arguments may have arbitrary execution
properties, and might not even support concurrent execution, but
are arranged for processing in a way that accommodates asynchrony.

Two method forms (

handle

and

whenComplete

) support unconditional computation
whether the triggering stage completed normally or exceptionally.
Method

exceptionally

supports computation
only when the triggering stage completes exceptionally, computing a
replacement result, similarly to the java

catch

keyword.
In all other cases, if a stage's computation terminates abruptly
with an (unchecked) exception or error, then all dependent stages
requiring its completion complete exceptionally as well, with a

CompletionException

holding the exception as its cause. If
a stage is dependent on

both

of two stages, and both
complete exceptionally, then the CompletionException may correspond
to either one of these exceptions. If a stage is dependent on

either

of two others, and only one of them completes
exceptionally, no guarantees are made about whether the dependent
stage completes normally or exceptionally. In the case of method

whenComplete

, when the supplied action itself encounters an
exception, then the stage completes exceptionally with this
exception unless the source stage also completed exceptionally, in
which case the exceptional completion from the source stage is
given preference and propagated to the dependent stage.

All methods adhere to the above triggering, execution, and
exceptional completion specifications (which are not repeated in
individual method specifications). Additionally, while arguments
used to pass a completion result (that is, for parameters of type

T

) for methods accepting them may be null, passing a null
value for any other parameter will result in a

NullPointerException

being thrown.

Method form

handle

is the most general way of
creating a continuation stage, unconditionally performing a
computation that is given both the result and exception (if any) of
the triggering CompletionStage, and computing an arbitrary result.
Method

whenComplete

is similar, but preserves
the result of the triggering stage instead of computing a new one.
Because a stage's normal result may be

null

, both methods
should have a computation structured thus:

```java
(result, exception) -> {
if (exception == null) {
// triggering stage completed normally
} else {
// triggering stage completed exceptionally
}
}
```

This interface does not define methods for initially creating,
forcibly completing normally or exceptionally, probing completion
status or results, or awaiting completion of a stage.
Implementations of CompletionStage may provide means of achieving
such effects, as appropriate. Method

toCompletableFuture()

enables interoperability among different implementations of this
interface by providing a common conversion type.

**All Known Implementing Classes:** CompletableFuture

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### <U>
CompletionStage
<U> thenApply​(
Function
<? super
T
,​? extends U> fn)

Returns a new CompletionStage that, when this stage completes
normally, is executed with this stage's result as the argument
to the supplied function.

This method is analogous to

Optional.map

and

Stream.map

.

See the

CompletionStage

documentation for rules
covering exceptional completion.

**Parameters:**
- fn

- the function to use to compute the value of the
returned CompletionStage

**Returns:**
- the new CompletionStage

**Type Parameters:**
- U

- the function's return type

---

#### <U>
CompletionStage
<U> thenApplyAsync​(
Function
<? super
T
,​? extends U> fn)

Returns a new CompletionStage that, when this stage completes
normally, is executed using this stage's default asynchronous
execution facility, with this stage's result as the argument to
the supplied function.

See the

CompletionStage

documentation for rules
covering exceptional completion.

**Parameters:**
- fn

- the function to use to compute the value of the
returned CompletionStage

**Returns:**
- the new CompletionStage

**Type Parameters:**
- U

- the function's return type

---

#### <U>
CompletionStage
<U> thenApplyAsync​(
Function
<? super
T
,​? extends U> fn,

Executor
executor)

Returns a new CompletionStage that, when this stage completes
normally, is executed using the supplied Executor, with this
stage's result as the argument to the supplied function.

See the

CompletionStage

documentation for rules
covering exceptional completion.

**Parameters:**
- fn

- the function to use to compute the value of the
returned CompletionStage
- executor

- the executor to use for asynchronous execution

**Returns:**
- the new CompletionStage

**Type Parameters:**
- U

- the function's return type

---

#### CompletionStage
<
Void
> thenAccept​(
Consumer
<? super
T
> action)

Returns a new CompletionStage that, when this stage completes
normally, is executed with this stage's result as the argument
to the supplied action.

See the

CompletionStage

documentation for rules
covering exceptional completion.

**Parameters:**
- action

- the action to perform before completing the
returned CompletionStage

**Returns:**
- the new CompletionStage

---

#### CompletionStage
<
Void
> thenAcceptAsync​(
Consumer
<? super
T
> action)

Returns a new CompletionStage that, when this stage completes
normally, is executed using this stage's default asynchronous
execution facility, with this stage's result as the argument to
the supplied action.

See the

CompletionStage

documentation for rules
covering exceptional completion.

**Parameters:**
- action

- the action to perform before completing the
returned CompletionStage

**Returns:**
- the new CompletionStage

---

#### CompletionStage
<
Void
> thenAcceptAsync​(
Consumer
<? super
T
> action,

Executor
executor)

Returns a new CompletionStage that, when this stage completes
normally, is executed using the supplied Executor, with this
stage's result as the argument to the supplied action.

See the

CompletionStage

documentation for rules
covering exceptional completion.

**Parameters:**
- action

- the action to perform before completing the
returned CompletionStage
- executor

- the executor to use for asynchronous execution

**Returns:**
- the new CompletionStage

---

#### CompletionStage
<
Void
> thenRun​(
Runnable
action)

Returns a new CompletionStage that, when this stage completes
normally, executes the given action.

See the

CompletionStage

documentation for rules
covering exceptional completion.

**Parameters:**
- action

- the action to perform before completing the
returned CompletionStage

**Returns:**
- the new CompletionStage

---

#### CompletionStage
<
Void
> thenRunAsync​(
Runnable
action)

Returns a new CompletionStage that, when this stage completes
normally, executes the given action using this stage's default
asynchronous execution facility.

See the

CompletionStage

documentation for rules
covering exceptional completion.

**Parameters:**
- action

- the action to perform before completing the
returned CompletionStage

**Returns:**
- the new CompletionStage

---

#### CompletionStage
<
Void
> thenRunAsync​(
Runnable
action,

Executor
executor)

Returns a new CompletionStage that, when this stage completes
normally, executes the given action using the supplied Executor.

See the

CompletionStage

documentation for rules
covering exceptional completion.

**Parameters:**
- action

- the action to perform before completing the
returned CompletionStage
- executor

- the executor to use for asynchronous execution

**Returns:**
- the new CompletionStage

---

#### <U,​V>
CompletionStage
<V> thenCombine​(
CompletionStage
<? extends U> other,

BiFunction
<? super
T
,​? super U,​? extends V> fn)

Returns a new CompletionStage that, when this and the other
given stage both complete normally, is executed with the two
results as arguments to the supplied function.

See the

CompletionStage

documentation for rules
covering exceptional completion.

**Parameters:**
- other

- the other CompletionStage
- fn

- the function to use to compute the value of the
returned CompletionStage

**Returns:**
- the new CompletionStage

**Type Parameters:**
- U

- the type of the other CompletionStage's result
- V

- the function's return type

---

#### <U,​V>
CompletionStage
<V> thenCombineAsync​(
CompletionStage
<? extends U> other,

BiFunction
<? super
T
,​? super U,​? extends V> fn)

Returns a new CompletionStage that, when this and the other
given stage both complete normally, is executed using this
stage's default asynchronous execution facility, with the two
results as arguments to the supplied function.

See the

CompletionStage

documentation for rules
covering exceptional completion.

**Parameters:**
- other

- the other CompletionStage
- fn

- the function to use to compute the value of the
returned CompletionStage

**Returns:**
- the new CompletionStage

**Type Parameters:**
- U

- the type of the other CompletionStage's result
- V

- the function's return type

---

#### <U,​V>
CompletionStage
<V> thenCombineAsync​(
CompletionStage
<? extends U> other,

BiFunction
<? super
T
,​? super U,​? extends V> fn,

Executor
executor)

Returns a new CompletionStage that, when this and the other
given stage both complete normally, is executed using the
supplied executor, with the two results as arguments to the
supplied function.

See the

CompletionStage

documentation for rules
covering exceptional completion.

**Parameters:**
- other

- the other CompletionStage
- fn

- the function to use to compute the value of the
returned CompletionStage
- executor

- the executor to use for asynchronous execution

**Returns:**
- the new CompletionStage

**Type Parameters:**
- U

- the type of the other CompletionStage's result
- V

- the function's return type

---

#### <U>
CompletionStage
<
Void
> thenAcceptBoth​(
CompletionStage
<? extends U> other,

BiConsumer
<? super
T
,​? super U> action)

Returns a new CompletionStage that, when this and the other
given stage both complete normally, is executed with the two
results as arguments to the supplied action.

See the

CompletionStage

documentation for rules
covering exceptional completion.

**Parameters:**
- other

- the other CompletionStage
- action

- the action to perform before completing the
returned CompletionStage

**Returns:**
- the new CompletionStage

**Type Parameters:**
- U

- the type of the other CompletionStage's result

---

#### <U>
CompletionStage
<
Void
> thenAcceptBothAsync​(
CompletionStage
<? extends U> other,

BiConsumer
<? super
T
,​? super U> action)

Returns a new CompletionStage that, when this and the other
given stage both complete normally, is executed using this
stage's default asynchronous execution facility, with the two
results as arguments to the supplied action.

See the

CompletionStage

documentation for rules
covering exceptional completion.

**Parameters:**
- other

- the other CompletionStage
- action

- the action to perform before completing the
returned CompletionStage

**Returns:**
- the new CompletionStage

**Type Parameters:**
- U

- the type of the other CompletionStage's result

---

#### <U>
CompletionStage
<
Void
> thenAcceptBothAsync​(
CompletionStage
<? extends U> other,

BiConsumer
<? super
T
,​? super U> action,

Executor
executor)

Returns a new CompletionStage that, when this and the other
given stage both complete normally, is executed using the
supplied executor, with the two results as arguments to the
supplied action.

See the

CompletionStage

documentation for rules
covering exceptional completion.

**Parameters:**
- other

- the other CompletionStage
- action

- the action to perform before completing the
returned CompletionStage
- executor

- the executor to use for asynchronous execution

**Returns:**
- the new CompletionStage

**Type Parameters:**
- U

- the type of the other CompletionStage's result

---

#### CompletionStage
<
Void
> runAfterBoth​(
CompletionStage
<?> other,

Runnable
action)

Returns a new CompletionStage that, when this and the other
given stage both complete normally, executes the given action.

See the

CompletionStage

documentation for rules
covering exceptional completion.

**Parameters:**
- other

- the other CompletionStage
- action

- the action to perform before completing the
returned CompletionStage

**Returns:**
- the new CompletionStage

---

#### CompletionStage
<
Void
> runAfterBothAsync​(
CompletionStage
<?> other,

Runnable
action)

Returns a new CompletionStage that, when this and the other
given stage both complete normally, executes the given action
using this stage's default asynchronous execution facility.

See the

CompletionStage

documentation for rules
covering exceptional completion.

**Parameters:**
- other

- the other CompletionStage
- action

- the action to perform before completing the
returned CompletionStage

**Returns:**
- the new CompletionStage

---

#### CompletionStage
<
Void
> runAfterBothAsync​(
CompletionStage
<?> other,

Runnable
action,

Executor
executor)

Returns a new CompletionStage that, when this and the other
given stage both complete normally, executes the given action
using the supplied executor.

See the

CompletionStage

documentation for rules
covering exceptional completion.

**Parameters:**
- other

- the other CompletionStage
- action

- the action to perform before completing the
returned CompletionStage
- executor

- the executor to use for asynchronous execution

**Returns:**
- the new CompletionStage

---

#### <U>
CompletionStage
<U> applyToEither​(
CompletionStage
<? extends
T
> other,

Function
<? super
T
,​U> fn)

Returns a new CompletionStage that, when either this or the
other given stage complete normally, is executed with the
corresponding result as argument to the supplied function.

See the

CompletionStage

documentation for rules
covering exceptional completion.

**Parameters:**
- other

- the other CompletionStage
- fn

- the function to use to compute the value of the
returned CompletionStage

**Returns:**
- the new CompletionStage

**Type Parameters:**
- U

- the function's return type

---

#### <U>
CompletionStage
<U> applyToEitherAsync​(
CompletionStage
<? extends
T
> other,

Function
<? super
T
,​U> fn)

Returns a new CompletionStage that, when either this or the
other given stage complete normally, is executed using this
stage's default asynchronous execution facility, with the
corresponding result as argument to the supplied function.

See the

CompletionStage

documentation for rules
covering exceptional completion.

**Parameters:**
- other

- the other CompletionStage
- fn

- the function to use to compute the value of the
returned CompletionStage

**Returns:**
- the new CompletionStage

**Type Parameters:**
- U

- the function's return type

---

#### <U>
CompletionStage
<U> applyToEitherAsync​(
CompletionStage
<? extends
T
> other,

Function
<? super
T
,​U> fn,

Executor
executor)

Returns a new CompletionStage that, when either this or the
other given stage complete normally, is executed using the
supplied executor, with the corresponding result as argument to
the supplied function.

See the

CompletionStage

documentation for rules
covering exceptional completion.

**Parameters:**
- other

- the other CompletionStage
- fn

- the function to use to compute the value of the
returned CompletionStage
- executor

- the executor to use for asynchronous execution

**Returns:**
- the new CompletionStage

**Type Parameters:**
- U

- the function's return type

---

#### CompletionStage
<
Void
> acceptEither​(
CompletionStage
<? extends
T
> other,

Consumer
<? super
T
> action)

Returns a new CompletionStage that, when either this or the
other given stage complete normally, is executed with the
corresponding result as argument to the supplied action.

See the

CompletionStage

documentation for rules
covering exceptional completion.

**Parameters:**
- other

- the other CompletionStage
- action

- the action to perform before completing the
returned CompletionStage

**Returns:**
- the new CompletionStage

---

#### CompletionStage
<
Void
> acceptEitherAsync​(
CompletionStage
<? extends
T
> other,

Consumer
<? super
T
> action)

Returns a new CompletionStage that, when either this or the
other given stage complete normally, is executed using this
stage's default asynchronous execution facility, with the
corresponding result as argument to the supplied action.

See the

CompletionStage

documentation for rules
covering exceptional completion.

**Parameters:**
- other

- the other CompletionStage
- action

- the action to perform before completing the
returned CompletionStage

**Returns:**
- the new CompletionStage

---

#### CompletionStage
<
Void
> acceptEitherAsync​(
CompletionStage
<? extends
T
> other,

Consumer
<? super
T
> action,

Executor
executor)

Returns a new CompletionStage that, when either this or the
other given stage complete normally, is executed using the
supplied executor, with the corresponding result as argument to
the supplied action.

See the

CompletionStage

documentation for rules
covering exceptional completion.

**Parameters:**
- other

- the other CompletionStage
- action

- the action to perform before completing the
returned CompletionStage
- executor

- the executor to use for asynchronous execution

**Returns:**
- the new CompletionStage

---

#### CompletionStage
<
Void
> runAfterEither​(
CompletionStage
<?> other,

Runnable
action)

Returns a new CompletionStage that, when either this or the
other given stage complete normally, executes the given action.

See the

CompletionStage

documentation for rules
covering exceptional completion.

**Parameters:**
- other

- the other CompletionStage
- action

- the action to perform before completing the
returned CompletionStage

**Returns:**
- the new CompletionStage

---

#### CompletionStage
<
Void
> runAfterEitherAsync​(
CompletionStage
<?> other,

Runnable
action)

Returns a new CompletionStage that, when either this or the
other given stage complete normally, executes the given action
using this stage's default asynchronous execution facility.

See the

CompletionStage

documentation for rules
covering exceptional completion.

**Parameters:**
- other

- the other CompletionStage
- action

- the action to perform before completing the
returned CompletionStage

**Returns:**
- the new CompletionStage

---

#### CompletionStage
<
Void
> runAfterEitherAsync​(
CompletionStage
<?> other,

Runnable
action,

Executor
executor)

Returns a new CompletionStage that, when either this or the
other given stage complete normally, executes the given action
using the supplied executor.

See the

CompletionStage

documentation for rules
covering exceptional completion.

**Parameters:**
- other

- the other CompletionStage
- action

- the action to perform before completing the
returned CompletionStage
- executor

- the executor to use for asynchronous execution

**Returns:**
- the new CompletionStage

---

#### <U>
CompletionStage
<U> thenCompose​(
Function
<? super
T
,​? extends
CompletionStage
<U>> fn)

Returns a new CompletionStage that is completed with the same
value as the CompletionStage returned by the given function.

When this stage completes normally, the given function is
invoked with this stage's result as the argument, returning
another CompletionStage. When that stage completes normally,
the CompletionStage returned by this method is completed with
the same value.

To ensure progress, the supplied function must arrange
eventual completion of its result.

This method is analogous to

Optional.flatMap

and

Stream.flatMap

.

See the

CompletionStage

documentation for rules
covering exceptional completion.

**Parameters:**
- fn

- the function to use to compute another CompletionStage

**Returns:**
- the new CompletionStage

**Type Parameters:**
- U

- the type of the returned CompletionStage's result

---

#### <U>
CompletionStage
<U> thenComposeAsync​(
Function
<? super
T
,​? extends
CompletionStage
<U>> fn)

Returns a new CompletionStage that is completed with the same
value as the CompletionStage returned by the given function,
executed using this stage's default asynchronous execution
facility.

When this stage completes normally, the given function is
invoked with this stage's result as the argument, returning
another CompletionStage. When that stage completes normally,
the CompletionStage returned by this method is completed with
the same value.

To ensure progress, the supplied function must arrange
eventual completion of its result.

See the

CompletionStage

documentation for rules
covering exceptional completion.

**Parameters:**
- fn

- the function to use to compute another CompletionStage

**Returns:**
- the new CompletionStage

**Type Parameters:**
- U

- the type of the returned CompletionStage's result

---

#### <U>
CompletionStage
<U> thenComposeAsync​(
Function
<? super
T
,​? extends
CompletionStage
<U>> fn,

Executor
executor)

Returns a new CompletionStage that is completed with the same
value as the CompletionStage returned by the given function,
executed using the supplied Executor.

When this stage completes normally, the given function is
invoked with this stage's result as the argument, returning
another CompletionStage. When that stage completes normally,
the CompletionStage returned by this method is completed with
the same value.

To ensure progress, the supplied function must arrange
eventual completion of its result.

See the

CompletionStage

documentation for rules
covering exceptional completion.

**Parameters:**
- fn

- the function to use to compute another CompletionStage
- executor

- the executor to use for asynchronous execution

**Returns:**
- the new CompletionStage

**Type Parameters:**
- U

- the type of the returned CompletionStage's result

---

#### <U>
CompletionStage
<U> handle​(
BiFunction
<? super
T
,​
Throwable
,​? extends U> fn)

Returns a new CompletionStage that, when this stage completes
either normally or exceptionally, is executed with this stage's
result and exception as arguments to the supplied function.

When this stage is complete, the given function is invoked
with the result (or

null

if none) and the exception (or

null

if none) of this stage as arguments, and the
function's result is used to complete the returned stage.

**Parameters:**
- fn

- the function to use to compute the value of the
returned CompletionStage

**Returns:**
- the new CompletionStage

**Type Parameters:**
- U

- the function's return type

---

#### <U>
CompletionStage
<U> handleAsync​(
BiFunction
<? super
T
,​
Throwable
,​? extends U> fn)

Returns a new CompletionStage that, when this stage completes
either normally or exceptionally, is executed using this stage's
default asynchronous execution facility, with this stage's
result and exception as arguments to the supplied function.

When this stage is complete, the given function is invoked
with the result (or

null

if none) and the exception (or

null

if none) of this stage as arguments, and the
function's result is used to complete the returned stage.

**Parameters:**
- fn

- the function to use to compute the value of the
returned CompletionStage

**Returns:**
- the new CompletionStage

**Type Parameters:**
- U

- the function's return type

---

#### <U>
CompletionStage
<U> handleAsync​(
BiFunction
<? super
T
,​
Throwable
,​? extends U> fn,

Executor
executor)

Returns a new CompletionStage that, when this stage completes
either normally or exceptionally, is executed using the
supplied executor, with this stage's result and exception as
arguments to the supplied function.

When this stage is complete, the given function is invoked
with the result (or

null

if none) and the exception (or

null

if none) of this stage as arguments, and the
function's result is used to complete the returned stage.

**Parameters:**
- fn

- the function to use to compute the value of the
returned CompletionStage
- executor

- the executor to use for asynchronous execution

**Returns:**
- the new CompletionStage

**Type Parameters:**
- U

- the function's return type

---

#### CompletionStage
<
T
> whenComplete​(
BiConsumer
<? super
T
,​? super
Throwable
> action)

Returns a new CompletionStage with the same result or exception as
this stage, that executes the given action when this stage completes.

When this stage is complete, the given action is invoked
with the result (or

null

if none) and the exception (or

null

if none) of this stage as arguments. The returned
stage is completed when the action returns.

Unlike method

handle

,
this method is not designed to translate completion outcomes,
so the supplied action should not throw an exception. However,
if it does, the following rules apply: if this stage completed
normally but the supplied action throws an exception, then the
returned stage completes exceptionally with the supplied
action's exception. Or, if this stage completed exceptionally
and the supplied action throws an exception, then the returned
stage completes exceptionally with this stage's exception.

**Parameters:**
- action

- the action to perform

**Returns:**
- the new CompletionStage

---

#### CompletionStage
<
T
> whenCompleteAsync​(
BiConsumer
<? super
T
,​? super
Throwable
> action)

Returns a new CompletionStage with the same result or exception as
this stage, that executes the given action using this stage's
default asynchronous execution facility when this stage completes.

When this stage is complete, the given action is invoked with the
result (or

null

if none) and the exception (or

null

if none) of this stage as arguments. The returned stage is completed
when the action returns.

Unlike method

handleAsync

,
this method is not designed to translate completion outcomes,
so the supplied action should not throw an exception. However,
if it does, the following rules apply: If this stage completed
normally but the supplied action throws an exception, then the
returned stage completes exceptionally with the supplied
action's exception. Or, if this stage completed exceptionally
and the supplied action throws an exception, then the returned
stage completes exceptionally with this stage's exception.

**Parameters:**
- action

- the action to perform

**Returns:**
- the new CompletionStage

---

#### CompletionStage
<
T
> whenCompleteAsync​(
BiConsumer
<? super
T
,​? super
Throwable
> action,

Executor
executor)

Returns a new CompletionStage with the same result or exception as
this stage, that executes the given action using the supplied
Executor when this stage completes.

When this stage is complete, the given action is invoked with the
result (or

null

if none) and the exception (or

null

if none) of this stage as arguments. The returned stage is completed
when the action returns.

Unlike method

handleAsync

,
this method is not designed to translate completion outcomes,
so the supplied action should not throw an exception. However,
if it does, the following rules apply: If this stage completed
normally but the supplied action throws an exception, then the
returned stage completes exceptionally with the supplied
action's exception. Or, if this stage completed exceptionally
and the supplied action throws an exception, then the returned
stage completes exceptionally with this stage's exception.

**Parameters:**
- action

- the action to perform
- executor

- the executor to use for asynchronous execution

**Returns:**
- the new CompletionStage

---

#### CompletionStage
<
T
> exceptionally​(
Function
<
Throwable
,​? extends
T
> fn)

Returns a new CompletionStage that, when this stage completes
exceptionally, is executed with this stage's exception as the
argument to the supplied function. Otherwise, if this stage
completes normally, then the returned stage also completes
normally with the same value.

**Parameters:**
- fn

- the function to use to compute the value of the
returned CompletionStage if this CompletionStage completed
exceptionally

**Returns:**
- the new CompletionStage

---

#### CompletableFuture
<
T
> toCompletableFuture()

Returns a

CompletableFuture

maintaining the same
completion properties as this stage. If this stage is already a
CompletableFuture, this method may return this stage itself.
Otherwise, invocation of this method may be equivalent in
effect to

thenApply(x -> x)

, but returning an instance
of type

CompletableFuture

.

**Returns:**
- the CompletableFuture

---

### Additional Sections

#### Interface CompletionStage<T>

**All Known Implementing Classes:** CompletableFuture

```java
public interface
CompletionStage<T>
```

A stage of a possibly asynchronous computation, that performs an
action or computes a value when another CompletionStage completes.
A stage completes upon termination of its computation, but this may
in turn trigger other dependent stages. The functionality defined
in this interface takes only a few basic forms, which expand out to
a larger set of methods to capture a range of usage styles:

- The computation performed by a stage may be expressed as a
Function, Consumer, or Runnable (using methods with names including

apply

,

accept

, or

run

, respectively)
depending on whether it requires arguments and/or produces results.
For example:

```java
stage.thenApply(x -> square(x))
.thenAccept(x -> System.out.print(x))
.thenRun(() -> System.out.println());
```

An additional form (

compose

) allows the construction of
computation pipelines from functions returning completion stages.

Any argument to a stage's computation is the outcome of a
triggering stage's computation.

One stage's execution may be triggered by completion of a
single stage, or both of two stages, or either of two stages.
Dependencies on a single stage are arranged using methods with
prefix

then

. Those triggered by completion of

both

of two stages may

combine

their results or
effects, using correspondingly named methods. Those triggered by

either

of two stages make no guarantees about which of the
results or effects are used for the dependent stage's computation.

Dependencies among stages control the triggering of
computations, but do not otherwise guarantee any particular
ordering. Additionally, execution of a new stage's computations may
be arranged in any of three ways: default execution, default
asynchronous execution (using methods with suffix

async

that employ the stage's default asynchronous execution facility),
or custom (via a supplied

Executor

). The execution
properties of default and async modes are specified by
CompletionStage implementations, not this interface. Methods with
explicit Executor arguments may have arbitrary execution
properties, and might not even support concurrent execution, but
are arranged for processing in a way that accommodates asynchrony.

Two method forms (

handle

and

whenComplete

) support unconditional computation
whether the triggering stage completed normally or exceptionally.
Method

exceptionally

supports computation
only when the triggering stage completes exceptionally, computing a
replacement result, similarly to the java

catch

keyword.
In all other cases, if a stage's computation terminates abruptly
with an (unchecked) exception or error, then all dependent stages
requiring its completion complete exceptionally as well, with a

CompletionException

holding the exception as its cause. If
a stage is dependent on

both

of two stages, and both
complete exceptionally, then the CompletionException may correspond
to either one of these exceptions. If a stage is dependent on

either

of two others, and only one of them completes
exceptionally, no guarantees are made about whether the dependent
stage completes normally or exceptionally. In the case of method

whenComplete

, when the supplied action itself encounters an
exception, then the stage completes exceptionally with this
exception unless the source stage also completed exceptionally, in
which case the exceptional completion from the source stage is
given preference and propagated to the dependent stage.

All methods adhere to the above triggering, execution, and
exceptional completion specifications (which are not repeated in
individual method specifications). Additionally, while arguments
used to pass a completion result (that is, for parameters of type

T

) for methods accepting them may be null, passing a null
value for any other parameter will result in a

NullPointerException

being thrown.

Method form

handle

is the most general way of
creating a continuation stage, unconditionally performing a
computation that is given both the result and exception (if any) of
the triggering CompletionStage, and computing an arbitrary result.
Method

whenComplete

is similar, but preserves
the result of the triggering stage instead of computing a new one.
Because a stage's normal result may be

null

, both methods
should have a computation structured thus:

```java
(result, exception) -> {
if (exception == null) {
// triggering stage completed normally
} else {
// triggering stage completed exceptionally
}
}
```

This interface does not define methods for initially creating,
forcibly completing normally or exceptionally, probing completion
status or results, or awaiting completion of a stage.
Implementations of CompletionStage may provide means of achieving
such effects, as appropriate. Method

toCompletableFuture()

enables interoperability among different implementations of this
interface by providing a common conversion type.

**Since:** 1.8

public interface

CompletionStage<T>

A stage of a possibly asynchronous computation, that performs an
action or computes a value when another CompletionStage completes.
A stage completes upon termination of its computation, but this may
in turn trigger other dependent stages. The functionality defined
in this interface takes only a few basic forms, which expand out to
a larger set of methods to capture a range of usage styles:

- The computation performed by a stage may be expressed as a
Function, Consumer, or Runnable (using methods with names including

apply

,

accept

, or

run

, respectively)
depending on whether it requires arguments and/or produces results.
For example:

```java
stage.thenApply(x -> square(x))
.thenAccept(x -> System.out.print(x))
.thenRun(() -> System.out.println());
```

An additional form (

compose

) allows the construction of
computation pipelines from functions returning completion stages.

Any argument to a stage's computation is the outcome of a
triggering stage's computation.

One stage's execution may be triggered by completion of a
single stage, or both of two stages, or either of two stages.
Dependencies on a single stage are arranged using methods with
prefix

then

. Those triggered by completion of

both

of two stages may

combine

their results or
effects, using correspondingly named methods. Those triggered by

either

of two stages make no guarantees about which of the
results or effects are used for the dependent stage's computation.

Dependencies among stages control the triggering of
computations, but do not otherwise guarantee any particular
ordering. Additionally, execution of a new stage's computations may
be arranged in any of three ways: default execution, default
asynchronous execution (using methods with suffix

async

that employ the stage's default asynchronous execution facility),
or custom (via a supplied

Executor

). The execution
properties of default and async modes are specified by
CompletionStage implementations, not this interface. Methods with
explicit Executor arguments may have arbitrary execution
properties, and might not even support concurrent execution, but
are arranged for processing in a way that accommodates asynchrony.

Two method forms (

handle

and

whenComplete

) support unconditional computation
whether the triggering stage completed normally or exceptionally.
Method

exceptionally

supports computation
only when the triggering stage completes exceptionally, computing a
replacement result, similarly to the java

catch

keyword.
In all other cases, if a stage's computation terminates abruptly
with an (unchecked) exception or error, then all dependent stages
requiring its completion complete exceptionally as well, with a

CompletionException

holding the exception as its cause. If
a stage is dependent on

both

of two stages, and both
complete exceptionally, then the CompletionException may correspond
to either one of these exceptions. If a stage is dependent on

either

of two others, and only one of them completes
exceptionally, no guarantees are made about whether the dependent
stage completes normally or exceptionally. In the case of method

whenComplete

, when the supplied action itself encounters an
exception, then the stage completes exceptionally with this
exception unless the source stage also completed exceptionally, in
which case the exceptional completion from the source stage is
given preference and propagated to the dependent stage.

All methods adhere to the above triggering, execution, and
exceptional completion specifications (which are not repeated in
individual method specifications). Additionally, while arguments
used to pass a completion result (that is, for parameters of type

T

) for methods accepting them may be null, passing a null
value for any other parameter will result in a

NullPointerException

being thrown.

Method form

handle

is the most general way of
creating a continuation stage, unconditionally performing a
computation that is given both the result and exception (if any) of
the triggering CompletionStage, and computing an arbitrary result.
Method

whenComplete

is similar, but preserves
the result of the triggering stage instead of computing a new one.
Because a stage's normal result may be

null

, both methods
should have a computation structured thus:

```java
(result, exception) -> {
if (exception == null) {
// triggering stage completed normally
} else {
// triggering stage completed exceptionally
}
}
```

This interface does not define methods for initially creating,
forcibly completing normally or exceptionally, probing completion
status or results, or awaiting completion of a stage.
Implementations of CompletionStage may provide means of achieving
such effects, as appropriate. Method

toCompletableFuture()

enables interoperability among different implementations of this
interface by providing a common conversion type.

The computation performed by a stage may be expressed as a
Function, Consumer, or Runnable (using methods with names including

apply

,

accept

, or

run

, respectively)
depending on whether it requires arguments and/or produces results.
For example:

```java
stage.thenApply(x -> square(x))
.thenAccept(x -> System.out.print(x))
.thenRun(() -> System.out.println());
```

An additional form (

compose

) allows the construction of
computation pipelines from functions returning completion stages.

Any argument to a stage's computation is the outcome of a
triggering stage's computation.

One stage's execution may be triggered by completion of a
single stage, or both of two stages, or either of two stages.
Dependencies on a single stage are arranged using methods with
prefix

then

. Those triggered by completion of

both

of two stages may

combine

their results or
effects, using correspondingly named methods. Those triggered by

either

of two stages make no guarantees about which of the
results or effects are used for the dependent stage's computation.

Dependencies among stages control the triggering of
computations, but do not otherwise guarantee any particular
ordering. Additionally, execution of a new stage's computations may
be arranged in any of three ways: default execution, default
asynchronous execution (using methods with suffix

async

that employ the stage's default asynchronous execution facility),
or custom (via a supplied

Executor

). The execution
properties of default and async modes are specified by
CompletionStage implementations, not this interface. Methods with
explicit Executor arguments may have arbitrary execution
properties, and might not even support concurrent execution, but
are arranged for processing in a way that accommodates asynchrony.

Two method forms (

handle

and

whenComplete

) support unconditional computation
whether the triggering stage completed normally or exceptionally.
Method

exceptionally

supports computation
only when the triggering stage completes exceptionally, computing a
replacement result, similarly to the java

catch

keyword.
In all other cases, if a stage's computation terminates abruptly
with an (unchecked) exception or error, then all dependent stages
requiring its completion complete exceptionally as well, with a

CompletionException

holding the exception as its cause. If
a stage is dependent on

both

of two stages, and both
complete exceptionally, then the CompletionException may correspond
to either one of these exceptions. If a stage is dependent on

either

of two others, and only one of them completes
exceptionally, no guarantees are made about whether the dependent
stage completes normally or exceptionally. In the case of method

whenComplete

, when the supplied action itself encounters an
exception, then the stage completes exceptionally with this
exception unless the source stage also completed exceptionally, in
which case the exceptional completion from the source stage is
given preference and propagated to the dependent stage.

stage.thenApply(x -> square(x))
.thenAccept(x -> System.out.print(x))
.thenRun(() -> System.out.println());

Any argument to a stage's computation is the outcome of a
triggering stage's computation.

One stage's execution may be triggered by completion of a
single stage, or both of two stages, or either of two stages.
Dependencies on a single stage are arranged using methods with
prefix

then

. Those triggered by completion of

both

of two stages may

combine

their results or
effects, using correspondingly named methods. Those triggered by

either

of two stages make no guarantees about which of the
results or effects are used for the dependent stage's computation.

Dependencies among stages control the triggering of
computations, but do not otherwise guarantee any particular
ordering. Additionally, execution of a new stage's computations may
be arranged in any of three ways: default execution, default
asynchronous execution (using methods with suffix

async

that employ the stage's default asynchronous execution facility),
or custom (via a supplied

Executor

). The execution
properties of default and async modes are specified by
CompletionStage implementations, not this interface. Methods with
explicit Executor arguments may have arbitrary execution
properties, and might not even support concurrent execution, but
are arranged for processing in a way that accommodates asynchrony.

Two method forms (

handle

and

whenComplete

) support unconditional computation
whether the triggering stage completed normally or exceptionally.
Method

exceptionally

supports computation
only when the triggering stage completes exceptionally, computing a
replacement result, similarly to the java

catch

keyword.
In all other cases, if a stage's computation terminates abruptly
with an (unchecked) exception or error, then all dependent stages
requiring its completion complete exceptionally as well, with a

CompletionException

holding the exception as its cause. If
a stage is dependent on

both

of two stages, and both
complete exceptionally, then the CompletionException may correspond
to either one of these exceptions. If a stage is dependent on

either

of two others, and only one of them completes
exceptionally, no guarantees are made about whether the dependent
stage completes normally or exceptionally. In the case of method

whenComplete

, when the supplied action itself encounters an
exception, then the stage completes exceptionally with this
exception unless the source stage also completed exceptionally, in
which case the exceptional completion from the source stage is
given preference and propagated to the dependent stage.

All methods adhere to the above triggering, execution, and
exceptional completion specifications (which are not repeated in
individual method specifications). Additionally, while arguments
used to pass a completion result (that is, for parameters of type

T

) for methods accepting them may be null, passing a null
value for any other parameter will result in a

NullPointerException

being thrown.

Method form

handle

is the most general way of
creating a continuation stage, unconditionally performing a
computation that is given both the result and exception (if any) of
the triggering CompletionStage, and computing an arbitrary result.
Method

whenComplete

is similar, but preserves
the result of the triggering stage instead of computing a new one.
Because a stage's normal result may be

null

, both methods
should have a computation structured thus:

```java
(result, exception) -> {
if (exception == null) {
// triggering stage completed normally
} else {
// triggering stage completed exceptionally
}
}
```

This interface does not define methods for initially creating,
forcibly completing normally or exceptionally, probing completion
status or results, or awaiting completion of a stage.
Implementations of CompletionStage may provide means of achieving
such effects, as appropriate. Method

toCompletableFuture()

enables interoperability among different implementations of this
interface by providing a common conversion type.

Method form

handle

is the most general way of
creating a continuation stage, unconditionally performing a
computation that is given both the result and exception (if any) of
the triggering CompletionStage, and computing an arbitrary result.
Method

whenComplete

is similar, but preserves
the result of the triggering stage instead of computing a new one.
Because a stage's normal result may be

null

, both methods
should have a computation structured thus:

```java
(result, exception) -> {
if (exception == null) {
// triggering stage completed normally
} else {
// triggering stage completed exceptionally
}
}
```

This interface does not define methods for initially creating,
forcibly completing normally or exceptionally, probing completion
status or results, or awaiting completion of a stage.
Implementations of CompletionStage may provide means of achieving
such effects, as appropriate. Method

toCompletableFuture()

enables interoperability among different implementations of this
interface by providing a common conversion type.

(result, exception) -> {
if (exception == null) {
// triggering stage completed normally
} else {
// triggering stage completed exceptionally
}
}

This interface does not define methods for initially creating,
forcibly completing normally or exceptionally, probing completion
status or results, or awaiting completion of a stage.
Implementations of CompletionStage may provide means of achieving
such effects, as appropriate. Method

toCompletableFuture()

enables interoperability among different implementations of this
interface by providing a common conversion type.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

CompletionStage

<

Void

>

acceptEither

​(

CompletionStage

<? extends

T

> other,

Consumer

<? super

T

> action)

Returns a new CompletionStage that, when either this or the
other given stage complete normally, is executed with the
corresponding result as argument to the supplied action.

CompletionStage

<

Void

>

acceptEitherAsync

​(

CompletionStage

<? extends

T

> other,

Consumer

<? super

T

> action)

Returns a new CompletionStage that, when either this or the
other given stage complete normally, is executed using this
stage's default asynchronous execution facility, with the
corresponding result as argument to the supplied action.

CompletionStage

<

Void

>

acceptEitherAsync

​(

CompletionStage

<? extends

T

> other,

Consumer

<? super

T

> action,

Executor

executor)

Returns a new CompletionStage that, when either this or the
other given stage complete normally, is executed using the
supplied executor, with the corresponding result as argument to
the supplied action.

<U>

CompletionStage

<U>

applyToEither

​(

CompletionStage

<? extends

T

> other,

Function

<? super

T

,​U> fn)

Returns a new CompletionStage that, when either this or the
other given stage complete normally, is executed with the
corresponding result as argument to the supplied function.

<U>

CompletionStage

<U>

applyToEitherAsync

​(

CompletionStage

<? extends

T

> other,

Function

<? super

T

,​U> fn)

Returns a new CompletionStage that, when either this or the
other given stage complete normally, is executed using this
stage's default asynchronous execution facility, with the
corresponding result as argument to the supplied function.

<U>

CompletionStage

<U>

applyToEitherAsync

​(

CompletionStage

<? extends

T

> other,

Function

<? super

T

,​U> fn,

Executor

executor)

Returns a new CompletionStage that, when either this or the
other given stage complete normally, is executed using the
supplied executor, with the corresponding result as argument to
the supplied function.

CompletionStage

<

T

>

exceptionally

​(

Function

<

Throwable

,​? extends

T

> fn)

Returns a new CompletionStage that, when this stage completes
exceptionally, is executed with this stage's exception as the
argument to the supplied function.

<U>

CompletionStage

<U>

handle

​(

BiFunction

<? super

T

,​

Throwable

,​? extends U> fn)

Returns a new CompletionStage that, when this stage completes
either normally or exceptionally, is executed with this stage's
result and exception as arguments to the supplied function.

<U>

CompletionStage

<U>

handleAsync

​(

BiFunction

<? super

T

,​

Throwable

,​? extends U> fn)

Returns a new CompletionStage that, when this stage completes
either normally or exceptionally, is executed using this stage's
default asynchronous execution facility, with this stage's
result and exception as arguments to the supplied function.

<U>

CompletionStage

<U>

handleAsync

​(

BiFunction

<? super

T

,​

Throwable

,​? extends U> fn,

Executor

executor)

Returns a new CompletionStage that, when this stage completes
either normally or exceptionally, is executed using the
supplied executor, with this stage's result and exception as
arguments to the supplied function.

CompletionStage

<

Void

>

runAfterBoth

​(

CompletionStage

<?> other,

Runnable

action)

Returns a new CompletionStage that, when this and the other
given stage both complete normally, executes the given action.

CompletionStage

<

Void

>

runAfterBothAsync

​(

CompletionStage

<?> other,

Runnable

action)

Returns a new CompletionStage that, when this and the other
given stage both complete normally, executes the given action
using this stage's default asynchronous execution facility.

CompletionStage

<

Void

>

runAfterBothAsync

​(

CompletionStage

<?> other,

Runnable

action,

Executor

executor)

Returns a new CompletionStage that, when this and the other
given stage both complete normally, executes the given action
using the supplied executor.

CompletionStage

<

Void

>

runAfterEither

​(

CompletionStage

<?> other,

Runnable

action)

Returns a new CompletionStage that, when either this or the
other given stage complete normally, executes the given action.

CompletionStage

<

Void

>

runAfterEitherAsync

​(

CompletionStage

<?> other,

Runnable

action)

Returns a new CompletionStage that, when either this or the
other given stage complete normally, executes the given action
using this stage's default asynchronous execution facility.

CompletionStage

<

Void

>

runAfterEitherAsync

​(

CompletionStage

<?> other,

Runnable

action,

Executor

executor)

Returns a new CompletionStage that, when either this or the
other given stage complete normally, executes the given action
using the supplied executor.

CompletionStage

<

Void

>

thenAccept

​(

Consumer

<? super

T

> action)

Returns a new CompletionStage that, when this stage completes
normally, is executed with this stage's result as the argument
to the supplied action.

CompletionStage

<

Void

>

thenAcceptAsync

​(

Consumer

<? super

T

> action)

Returns a new CompletionStage that, when this stage completes
normally, is executed using this stage's default asynchronous
execution facility, with this stage's result as the argument to
the supplied action.

CompletionStage

<

Void

>

thenAcceptAsync

​(

Consumer

<? super

T

> action,

Executor

executor)

Returns a new CompletionStage that, when this stage completes
normally, is executed using the supplied Executor, with this
stage's result as the argument to the supplied action.

<U>

CompletionStage

<

Void

>

thenAcceptBoth

​(

CompletionStage

<? extends U> other,

BiConsumer

<? super

T

,​? super U> action)

Returns a new CompletionStage that, when this and the other
given stage both complete normally, is executed with the two
results as arguments to the supplied action.

<U>

CompletionStage

<

Void

>

thenAcceptBothAsync

​(

CompletionStage

<? extends U> other,

BiConsumer

<? super

T

,​? super U> action)

Returns a new CompletionStage that, when this and the other
given stage both complete normally, is executed using this
stage's default asynchronous execution facility, with the two
results as arguments to the supplied action.

<U>

CompletionStage

<

Void

>

thenAcceptBothAsync

​(

CompletionStage

<? extends U> other,

BiConsumer

<? super

T

,​? super U> action,

Executor

executor)

Returns a new CompletionStage that, when this and the other
given stage both complete normally, is executed using the
supplied executor, with the two results as arguments to the
supplied action.

<U>

CompletionStage

<U>

thenApply

​(

Function

<? super

T

,​? extends U> fn)

Returns a new CompletionStage that, when this stage completes
normally, is executed with this stage's result as the argument
to the supplied function.

<U>

CompletionStage

<U>

thenApplyAsync

​(

Function

<? super

T

,​? extends U> fn)

Returns a new CompletionStage that, when this stage completes
normally, is executed using this stage's default asynchronous
execution facility, with this stage's result as the argument to
the supplied function.

<U>

CompletionStage

<U>

thenApplyAsync

​(

Function

<? super

T

,​? extends U> fn,

Executor

executor)

Returns a new CompletionStage that, when this stage completes
normally, is executed using the supplied Executor, with this
stage's result as the argument to the supplied function.

<U,​V>

CompletionStage

<V>

thenCombine

​(

CompletionStage

<? extends U> other,

BiFunction

<? super

T

,​? super U,​? extends V> fn)

Returns a new CompletionStage that, when this and the other
given stage both complete normally, is executed with the two
results as arguments to the supplied function.

<U,​V>

CompletionStage

<V>

thenCombineAsync

​(

CompletionStage

<? extends U> other,

BiFunction

<? super

T

,​? super U,​? extends V> fn)

Returns a new CompletionStage that, when this and the other
given stage both complete normally, is executed using this
stage's default asynchronous execution facility, with the two
results as arguments to the supplied function.

<U,​V>

CompletionStage

<V>

thenCombineAsync

​(

CompletionStage

<? extends U> other,

BiFunction

<? super

T

,​? super U,​? extends V> fn,

Executor

executor)

Returns a new CompletionStage that, when this and the other
given stage both complete normally, is executed using the
supplied executor, with the two results as arguments to the
supplied function.

<U>

CompletionStage

<U>

thenCompose

​(

Function

<? super

T

,​? extends

CompletionStage

<U>> fn)

Returns a new CompletionStage that is completed with the same
value as the CompletionStage returned by the given function.

<U>

CompletionStage

<U>

thenComposeAsync

​(

Function

<? super

T

,​? extends

CompletionStage

<U>> fn)

Returns a new CompletionStage that is completed with the same
value as the CompletionStage returned by the given function,
executed using this stage's default asynchronous execution
facility.

<U>

CompletionStage

<U>

thenComposeAsync

​(

Function

<? super

T

,​? extends

CompletionStage

<U>> fn,

Executor

executor)

Returns a new CompletionStage that is completed with the same
value as the CompletionStage returned by the given function,
executed using the supplied Executor.

CompletionStage

<

Void

>

thenRun

​(

Runnable

action)

Returns a new CompletionStage that, when this stage completes
normally, executes the given action.

CompletionStage

<

Void

>

thenRunAsync

​(

Runnable

action)

Returns a new CompletionStage that, when this stage completes
normally, executes the given action using this stage's default
asynchronous execution facility.

CompletionStage

<

Void

>

thenRunAsync

​(

Runnable

action,

Executor

executor)

Returns a new CompletionStage that, when this stage completes
normally, executes the given action using the supplied Executor.

CompletableFuture

<

T

>

toCompletableFuture

()

Returns a

CompletableFuture

maintaining the same
completion properties as this stage.

CompletionStage

<

T

>

whenComplete

​(

BiConsumer

<? super

T

,​? super

Throwable

> action)

Returns a new CompletionStage with the same result or exception as
this stage, that executes the given action when this stage completes.

CompletionStage

<

T

>

whenCompleteAsync

​(

BiConsumer

<? super

T

,​? super

Throwable

> action)

Returns a new CompletionStage with the same result or exception as
this stage, that executes the given action using this stage's
default asynchronous execution facility when this stage completes.

CompletionStage

<

T

>

whenCompleteAsync

​(

BiConsumer

<? super

T

,​? super

Throwable

> action,

Executor

executor)

Returns a new CompletionStage with the same result or exception as
this stage, that executes the given action using the supplied
Executor when this stage completes.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

CompletionStage

<

Void

>

acceptEither

​(

CompletionStage

<? extends

T

> other,

Consumer

<? super

T

> action)

Returns a new CompletionStage that, when either this or the
other given stage complete normally, is executed with the
corresponding result as argument to the supplied action.

CompletionStage

<

Void

>

acceptEitherAsync

​(

CompletionStage

<? extends

T

> other,

Consumer

<? super

T

> action)

Returns a new CompletionStage that, when either this or the
other given stage complete normally, is executed using this
stage's default asynchronous execution facility, with the
corresponding result as argument to the supplied action.

CompletionStage

<

Void

>

acceptEitherAsync

​(

CompletionStage

<? extends

T

> other,

Consumer

<? super

T

> action,

Executor

executor)

Returns a new CompletionStage that, when either this or the
other given stage complete normally, is executed using the
supplied executor, with the corresponding result as argument to
the supplied action.

<U>

CompletionStage

<U>

applyToEither

​(

CompletionStage

<? extends

T

> other,

Function

<? super

T

,​U> fn)

Returns a new CompletionStage that, when either this or the
other given stage complete normally, is executed with the
corresponding result as argument to the supplied function.

<U>

CompletionStage

<U>

applyToEitherAsync

​(

CompletionStage

<? extends

T

> other,

Function

<? super

T

,​U> fn)

Returns a new CompletionStage that, when either this or the
other given stage complete normally, is executed using this
stage's default asynchronous execution facility, with the
corresponding result as argument to the supplied function.

<U>

CompletionStage

<U>

applyToEitherAsync

​(

CompletionStage

<? extends

T

> other,

Function

<? super

T

,​U> fn,

Executor

executor)

Returns a new CompletionStage that, when either this or the
other given stage complete normally, is executed using the
supplied executor, with the corresponding result as argument to
the supplied function.

CompletionStage

<

T

>

exceptionally

​(

Function

<

Throwable

,​? extends

T

> fn)

Returns a new CompletionStage that, when this stage completes
exceptionally, is executed with this stage's exception as the
argument to the supplied function.

<U>

CompletionStage

<U>

handle

​(

BiFunction

<? super

T

,​

Throwable

,​? extends U> fn)

Returns a new CompletionStage that, when this stage completes
either normally or exceptionally, is executed with this stage's
result and exception as arguments to the supplied function.

<U>

CompletionStage

<U>

handleAsync

​(

BiFunction

<? super

T

,​

Throwable

,​? extends U> fn)

Returns a new CompletionStage that, when this stage completes
either normally or exceptionally, is executed using this stage's
default asynchronous execution facility, with this stage's
result and exception as arguments to the supplied function.

<U>

CompletionStage

<U>

handleAsync

​(

BiFunction

<? super

T

,​

Throwable

,​? extends U> fn,

Executor

executor)

Returns a new CompletionStage that, when this stage completes
either normally or exceptionally, is executed using the
supplied executor, with this stage's result and exception as
arguments to the supplied function.

CompletionStage

<

Void

>

runAfterBoth

​(

CompletionStage

<?> other,

Runnable

action)

Returns a new CompletionStage that, when this and the other
given stage both complete normally, executes the given action.

CompletionStage

<

Void

>

runAfterBothAsync

​(

CompletionStage

<?> other,

Runnable

action)

Returns a new CompletionStage that, when this and the other
given stage both complete normally, executes the given action
using this stage's default asynchronous execution facility.

CompletionStage

<

Void

>

runAfterBothAsync

​(

CompletionStage

<?> other,

Runnable

action,

Executor

executor)

Returns a new CompletionStage that, when this and the other
given stage both complete normally, executes the given action
using the supplied executor.

CompletionStage

<

Void

>

runAfterEither

​(

CompletionStage

<?> other,

Runnable

action)

Returns a new CompletionStage that, when either this or the
other given stage complete normally, executes the given action.

CompletionStage

<

Void

>

runAfterEitherAsync

​(

CompletionStage

<?> other,

Runnable

action)

Returns a new CompletionStage that, when either this or the
other given stage complete normally, executes the given action
using this stage's default asynchronous execution facility.

CompletionStage

<

Void

>

runAfterEitherAsync

​(

CompletionStage

<?> other,

Runnable

action,

Executor

executor)

Returns a new CompletionStage that, when either this or the
other given stage complete normally, executes the given action
using the supplied executor.

CompletionStage

<

Void

>

thenAccept

​(

Consumer

<? super

T

> action)

Returns a new CompletionStage that, when this stage completes
normally, is executed with this stage's result as the argument
to the supplied action.

CompletionStage

<

Void

>

thenAcceptAsync

​(

Consumer

<? super

T

> action)

Returns a new CompletionStage that, when this stage completes
normally, is executed using this stage's default asynchronous
execution facility, with this stage's result as the argument to
the supplied action.

CompletionStage

<

Void

>

thenAcceptAsync

​(

Consumer

<? super

T

> action,

Executor

executor)

Returns a new CompletionStage that, when this stage completes
normally, is executed using the supplied Executor, with this
stage's result as the argument to the supplied action.

<U>

CompletionStage

<

Void

>

thenAcceptBoth

​(

CompletionStage

<? extends U> other,

BiConsumer

<? super

T

,​? super U> action)

Returns a new CompletionStage that, when this and the other
given stage both complete normally, is executed with the two
results as arguments to the supplied action.

<U>

CompletionStage

<

Void

>

thenAcceptBothAsync

​(

CompletionStage

<? extends U> other,

BiConsumer

<? super

T

,​? super U> action)

Returns a new CompletionStage that, when this and the other
given stage both complete normally, is executed using this
stage's default asynchronous execution facility, with the two
results as arguments to the supplied action.

<U>

CompletionStage

<

Void

>

thenAcceptBothAsync

​(

CompletionStage

<? extends U> other,

BiConsumer

<? super

T

,​? super U> action,

Executor

executor)

Returns a new CompletionStage that, when this and the other
given stage both complete normally, is executed using the
supplied executor, with the two results as arguments to the
supplied action.

<U>

CompletionStage

<U>

thenApply

​(

Function

<? super

T

,​? extends U> fn)

Returns a new CompletionStage that, when this stage completes
normally, is executed with this stage's result as the argument
to the supplied function.

<U>

CompletionStage

<U>

thenApplyAsync

​(

Function

<? super

T

,​? extends U> fn)

Returns a new CompletionStage that, when this stage completes
normally, is executed using this stage's default asynchronous
execution facility, with this stage's result as the argument to
the supplied function.

<U>

CompletionStage

<U>

thenApplyAsync

​(

Function

<? super

T

,​? extends U> fn,

Executor

executor)

Returns a new CompletionStage that, when this stage completes
normally, is executed using the supplied Executor, with this
stage's result as the argument to the supplied function.

<U,​V>

CompletionStage

<V>

thenCombine

​(

CompletionStage

<? extends U> other,

BiFunction

<? super

T

,​? super U,​? extends V> fn)

Returns a new CompletionStage that, when this and the other
given stage both complete normally, is executed with the two
results as arguments to the supplied function.

<U,​V>

CompletionStage

<V>

thenCombineAsync

​(

CompletionStage

<? extends U> other,

BiFunction

<? super

T

,​? super U,​? extends V> fn)

Returns a new CompletionStage that, when this and the other
given stage both complete normally, is executed using this
stage's default asynchronous execution facility, with the two
results as arguments to the supplied function.

<U,​V>

CompletionStage

<V>

thenCombineAsync

​(

CompletionStage

<? extends U> other,

BiFunction

<? super

T

,​? super U,​? extends V> fn,

Executor

executor)

Returns a new CompletionStage that, when this and the other
given stage both complete normally, is executed using the
supplied executor, with the two results as arguments to the
supplied function.

<U>

CompletionStage

<U>

thenCompose

​(

Function

<? super

T

,​? extends

CompletionStage

<U>> fn)

Returns a new CompletionStage that is completed with the same
value as the CompletionStage returned by the given function.

<U>

CompletionStage

<U>

thenComposeAsync

​(

Function

<? super

T

,​? extends

CompletionStage

<U>> fn)

Returns a new CompletionStage that is completed with the same
value as the CompletionStage returned by the given function,
executed using this stage's default asynchronous execution
facility.

<U>

CompletionStage

<U>

thenComposeAsync

​(

Function

<? super

T

,​? extends

CompletionStage

<U>> fn,

Executor

executor)

Returns a new CompletionStage that is completed with the same
value as the CompletionStage returned by the given function,
executed using the supplied Executor.

CompletionStage

<

Void

>

thenRun

​(

Runnable

action)

Returns a new CompletionStage that, when this stage completes
normally, executes the given action.

CompletionStage

<

Void

>

thenRunAsync

​(

Runnable

action)

Returns a new CompletionStage that, when this stage completes
normally, executes the given action using this stage's default
asynchronous execution facility.

CompletionStage

<

Void

>

thenRunAsync

​(

Runnable

action,

Executor

executor)

Returns a new CompletionStage that, when this stage completes
normally, executes the given action using the supplied Executor.

CompletableFuture

<

T

>

toCompletableFuture

()

Returns a

CompletableFuture

maintaining the same
completion properties as this stage.

CompletionStage

<

T

>

whenComplete

​(

BiConsumer

<? super

T

,​? super

Throwable

> action)

Returns a new CompletionStage with the same result or exception as
this stage, that executes the given action when this stage completes.

CompletionStage

<

T

>

whenCompleteAsync

​(

BiConsumer

<? super

T

,​? super

Throwable

> action)

Returns a new CompletionStage with the same result or exception as
this stage, that executes the given action using this stage's
default asynchronous execution facility when this stage completes.

CompletionStage

<

T

>

whenCompleteAsync

​(

BiConsumer

<? super

T

,​? super

Throwable

> action,

Executor

executor)

Returns a new CompletionStage with the same result or exception as
this stage, that executes the given action using the supplied
Executor when this stage completes.

---

#### Method Summary

Returns a new CompletionStage that, when either this or the
other given stage complete normally, is executed with the
corresponding result as argument to the supplied action.

Returns a new CompletionStage that, when either this or the
other given stage complete normally, is executed using this
stage's default asynchronous execution facility, with the
corresponding result as argument to the supplied action.

Returns a new CompletionStage that, when either this or the
other given stage complete normally, is executed using the
supplied executor, with the corresponding result as argument to
the supplied action.

Returns a new CompletionStage that, when either this or the
other given stage complete normally, is executed with the
corresponding result as argument to the supplied function.

Returns a new CompletionStage that, when either this or the
other given stage complete normally, is executed using this
stage's default asynchronous execution facility, with the
corresponding result as argument to the supplied function.

Returns a new CompletionStage that, when either this or the
other given stage complete normally, is executed using the
supplied executor, with the corresponding result as argument to
the supplied function.

Returns a new CompletionStage that, when this stage completes
exceptionally, is executed with this stage's exception as the
argument to the supplied function.

Returns a new CompletionStage that, when this stage completes
either normally or exceptionally, is executed with this stage's
result and exception as arguments to the supplied function.

Returns a new CompletionStage that, when this stage completes
either normally or exceptionally, is executed using this stage's
default asynchronous execution facility, with this stage's
result and exception as arguments to the supplied function.

Returns a new CompletionStage that, when this stage completes
either normally or exceptionally, is executed using the
supplied executor, with this stage's result and exception as
arguments to the supplied function.

Returns a new CompletionStage that, when this and the other
given stage both complete normally, executes the given action.

Returns a new CompletionStage that, when this and the other
given stage both complete normally, executes the given action
using this stage's default asynchronous execution facility.

Returns a new CompletionStage that, when this and the other
given stage both complete normally, executes the given action
using the supplied executor.

Returns a new CompletionStage that, when either this or the
other given stage complete normally, executes the given action.

Returns a new CompletionStage that, when either this or the
other given stage complete normally, executes the given action
using this stage's default asynchronous execution facility.

Returns a new CompletionStage that, when either this or the
other given stage complete normally, executes the given action
using the supplied executor.

Returns a new CompletionStage that, when this stage completes
normally, is executed with this stage's result as the argument
to the supplied action.

Returns a new CompletionStage that, when this stage completes
normally, is executed using this stage's default asynchronous
execution facility, with this stage's result as the argument to
the supplied action.

Returns a new CompletionStage that, when this stage completes
normally, is executed using the supplied Executor, with this
stage's result as the argument to the supplied action.

Returns a new CompletionStage that, when this and the other
given stage both complete normally, is executed with the two
results as arguments to the supplied action.

Returns a new CompletionStage that, when this and the other
given stage both complete normally, is executed using this
stage's default asynchronous execution facility, with the two
results as arguments to the supplied action.

Returns a new CompletionStage that, when this and the other
given stage both complete normally, is executed using the
supplied executor, with the two results as arguments to the
supplied action.

Returns a new CompletionStage that, when this stage completes
normally, is executed with this stage's result as the argument
to the supplied function.

Returns a new CompletionStage that, when this stage completes
normally, is executed using this stage's default asynchronous
execution facility, with this stage's result as the argument to
the supplied function.

Returns a new CompletionStage that, when this stage completes
normally, is executed using the supplied Executor, with this
stage's result as the argument to the supplied function.

Returns a new CompletionStage that, when this and the other
given stage both complete normally, is executed with the two
results as arguments to the supplied function.

Returns a new CompletionStage that, when this and the other
given stage both complete normally, is executed using this
stage's default asynchronous execution facility, with the two
results as arguments to the supplied function.

Returns a new CompletionStage that, when this and the other
given stage both complete normally, is executed using the
supplied executor, with the two results as arguments to the
supplied function.

Returns a new CompletionStage that is completed with the same
value as the CompletionStage returned by the given function.

Returns a new CompletionStage that is completed with the same
value as the CompletionStage returned by the given function,
executed using this stage's default asynchronous execution
facility.

Returns a new CompletionStage that is completed with the same
value as the CompletionStage returned by the given function,
executed using the supplied Executor.

Returns a new CompletionStage that, when this stage completes
normally, executes the given action.

Returns a new CompletionStage that, when this stage completes
normally, executes the given action using this stage's default
asynchronous execution facility.

Returns a new CompletionStage that, when this stage completes
normally, executes the given action using the supplied Executor.

Returns a

CompletableFuture

maintaining the same
completion properties as this stage.

Returns a new CompletionStage with the same result or exception as
this stage, that executes the given action when this stage completes.

Returns a new CompletionStage with the same result or exception as
this stage, that executes the given action using this stage's
default asynchronous execution facility when this stage completes.

Returns a new CompletionStage with the same result or exception as
this stage, that executes the given action using the supplied
Executor when this stage completes.

============ METHOD DETAIL ==========

- Method Detail

- thenApply

```java
<U>
CompletionStage
<U> thenApply​(
Function
<? super
T
,​? extends U> fn)
```

Returns a new CompletionStage that, when this stage completes
normally, is executed with this stage's result as the argument
to the supplied function.

This method is analogous to

Optional.map

and

Stream.map

.

See the

CompletionStage

documentation for rules
covering exceptional completion.

**Type Parameters:** U

- the function's return type
**Parameters:** fn

- the function to use to compute the value of the
returned CompletionStage
**Returns:** the new CompletionStage

- thenApplyAsync

```java
<U>
CompletionStage
<U> thenApplyAsync​(
Function
<? super
T
,​? extends U> fn)
```

Returns a new CompletionStage that, when this stage completes
normally, is executed using this stage's default asynchronous
execution facility, with this stage's result as the argument to
the supplied function.

See the

CompletionStage

documentation for rules
covering exceptional completion.

**Type Parameters:** U

- the function's return type
**Parameters:** fn

- the function to use to compute the value of the
returned CompletionStage
**Returns:** the new CompletionStage

- thenApplyAsync

```java
<U>
CompletionStage
<U> thenApplyAsync​(
Function
<? super
T
,​? extends U> fn,

Executor
executor)
```

Returns a new CompletionStage that, when this stage completes
normally, is executed using the supplied Executor, with this
stage's result as the argument to the supplied function.

See the

CompletionStage

documentation for rules
covering exceptional completion.

**Type Parameters:** U

- the function's return type
**Parameters:** fn

- the function to use to compute the value of the
returned CompletionStage
**Parameters:** executor

- the executor to use for asynchronous execution
**Returns:** the new CompletionStage

- thenAccept

```java
CompletionStage
<
Void
> thenAccept​(
Consumer
<? super
T
> action)
```

Returns a new CompletionStage that, when this stage completes
normally, is executed with this stage's result as the argument
to the supplied action.

See the

CompletionStage

documentation for rules
covering exceptional completion.

**Parameters:** action

- the action to perform before completing the
returned CompletionStage
**Returns:** the new CompletionStage

- thenAcceptAsync

```java
CompletionStage
<
Void
> thenAcceptAsync​(
Consumer
<? super
T
> action)
```

Returns a new CompletionStage that, when this stage completes
normally, is executed using this stage's default asynchronous
execution facility, with this stage's result as the argument to
the supplied action.

See the

CompletionStage

documentation for rules
covering exceptional completion.

**Parameters:** action

- the action to perform before completing the
returned CompletionStage
**Returns:** the new CompletionStage

- thenAcceptAsync

```java
CompletionStage
<
Void
> thenAcceptAsync​(
Consumer
<? super
T
> action,

Executor
executor)
```

Returns a new CompletionStage that, when this stage completes
normally, is executed using the supplied Executor, with this
stage's result as the argument to the supplied action.

See the

CompletionStage

documentation for rules
covering exceptional completion.

**Parameters:** action

- the action to perform before completing the
returned CompletionStage
**Parameters:** executor

- the executor to use for asynchronous execution
**Returns:** the new CompletionStage

- thenRun

```java
CompletionStage
<
Void
> thenRun​(
Runnable
action)
```

Returns a new CompletionStage that, when this stage completes
normally, executes the given action.

See the

CompletionStage

documentation for rules
covering exceptional completion.

**Parameters:** action

- the action to perform before completing the
returned CompletionStage
**Returns:** the new CompletionStage

- thenRunAsync

```java
CompletionStage
<
Void
> thenRunAsync​(
Runnable
action)
```

Returns a new CompletionStage that, when this stage completes
normally, executes the given action using this stage's default
asynchronous execution facility.

See the

CompletionStage

documentation for rules
covering exceptional completion.

**Parameters:** action

- the action to perform before completing the
returned CompletionStage
**Returns:** the new CompletionStage

- thenRunAsync

```java
CompletionStage
<
Void
> thenRunAsync​(
Runnable
action,

Executor
executor)
```

Returns a new CompletionStage that, when this stage completes
normally, executes the given action using the supplied Executor.

See the

CompletionStage

documentation for rules
covering exceptional completion.

**Parameters:** action

- the action to perform before completing the
returned CompletionStage
**Parameters:** executor

- the executor to use for asynchronous execution
**Returns:** the new CompletionStage

- thenCombine

```java
<U,​V>
CompletionStage
<V> thenCombine​(
CompletionStage
<? extends U> other,

BiFunction
<? super
T
,​? super U,​? extends V> fn)
```

Returns a new CompletionStage that, when this and the other
given stage both complete normally, is executed with the two
results as arguments to the supplied function.

See the

CompletionStage

documentation for rules
covering exceptional completion.

**Type Parameters:** U

- the type of the other CompletionStage's result
**Type Parameters:** V

- the function's return type
**Parameters:** other

- the other CompletionStage
**Parameters:** fn

- the function to use to compute the value of the
returned CompletionStage
**Returns:** the new CompletionStage

- thenCombineAsync

```java
<U,​V>
CompletionStage
<V> thenCombineAsync​(
CompletionStage
<? extends U> other,

BiFunction
<? super
T
,​? super U,​? extends V> fn)
```

Returns a new CompletionStage that, when this and the other
given stage both complete normally, is executed using this
stage's default asynchronous execution facility, with the two
results as arguments to the supplied function.

See the

CompletionStage

documentation for rules
covering exceptional completion.

**Type Parameters:** U

- the type of the other CompletionStage's result
**Type Parameters:** V

- the function's return type
**Parameters:** other

- the other CompletionStage
**Parameters:** fn

- the function to use to compute the value of the
returned CompletionStage
**Returns:** the new CompletionStage

- thenCombineAsync

```java
<U,​V>
CompletionStage
<V> thenCombineAsync​(
CompletionStage
<? extends U> other,

BiFunction
<? super
T
,​? super U,​? extends V> fn,

Executor
executor)
```

Returns a new CompletionStage that, when this and the other
given stage both complete normally, is executed using the
supplied executor, with the two results as arguments to the
supplied function.

See the

CompletionStage

documentation for rules
covering exceptional completion.

**Type Parameters:** U

- the type of the other CompletionStage's result
**Type Parameters:** V

- the function's return type
**Parameters:** other

- the other CompletionStage
**Parameters:** fn

- the function to use to compute the value of the
returned CompletionStage
**Parameters:** executor

- the executor to use for asynchronous execution
**Returns:** the new CompletionStage

- thenAcceptBoth

```java
<U>
CompletionStage
<
Void
> thenAcceptBoth​(
CompletionStage
<? extends U> other,

BiConsumer
<? super
T
,​? super U> action)
```

Returns a new CompletionStage that, when this and the other
given stage both complete normally, is executed with the two
results as arguments to the supplied action.

See the

CompletionStage

documentation for rules
covering exceptional completion.

**Type Parameters:** U

- the type of the other CompletionStage's result
**Parameters:** other

- the other CompletionStage
**Parameters:** action

- the action to perform before completing the
returned CompletionStage
**Returns:** the new CompletionStage

- thenAcceptBothAsync

```java
<U>
CompletionStage
<
Void
> thenAcceptBothAsync​(
CompletionStage
<? extends U> other,

BiConsumer
<? super
T
,​? super U> action)
```

Returns a new CompletionStage that, when this and the other
given stage both complete normally, is executed using this
stage's default asynchronous execution facility, with the two
results as arguments to the supplied action.

See the

CompletionStage

documentation for rules
covering exceptional completion.

**Type Parameters:** U

- the type of the other CompletionStage's result
**Parameters:** other

- the other CompletionStage
**Parameters:** action

- the action to perform before completing the
returned CompletionStage
**Returns:** the new CompletionStage

- thenAcceptBothAsync

```java
<U>
CompletionStage
<
Void
> thenAcceptBothAsync​(
CompletionStage
<? extends U> other,

BiConsumer
<? super
T
,​? super U> action,

Executor
executor)
```

Returns a new CompletionStage that, when this and the other
given stage both complete normally, is executed using the
supplied executor, with the two results as arguments to the
supplied action.

See the

CompletionStage

documentation for rules
covering exceptional completion.

**Type Parameters:** U

- the type of the other CompletionStage's result
**Parameters:** other

- the other CompletionStage
**Parameters:** action

- the action to perform before completing the
returned CompletionStage
**Parameters:** executor

- the executor to use for asynchronous execution
**Returns:** the new CompletionStage

- runAfterBoth

```java
CompletionStage
<
Void
> runAfterBoth​(
CompletionStage
<?> other,

Runnable
action)
```

Returns a new CompletionStage that, when this and the other
given stage both complete normally, executes the given action.

See the

CompletionStage

documentation for rules
covering exceptional completion.

**Parameters:** other

- the other CompletionStage
**Parameters:** action

- the action to perform before completing the
returned CompletionStage
**Returns:** the new CompletionStage

- runAfterBothAsync

```java
CompletionStage
<
Void
> runAfterBothAsync​(
CompletionStage
<?> other,

Runnable
action)
```

Returns a new CompletionStage that, when this and the other
given stage both complete normally, executes the given action
using this stage's default asynchronous execution facility.

See the

CompletionStage

documentation for rules
covering exceptional completion.

**Parameters:** other

- the other CompletionStage
**Parameters:** action

- the action to perform before completing the
returned CompletionStage
**Returns:** the new CompletionStage

- runAfterBothAsync

```java
CompletionStage
<
Void
> runAfterBothAsync​(
CompletionStage
<?> other,

Runnable
action,

Executor
executor)
```

Returns a new CompletionStage that, when this and the other
given stage both complete normally, executes the given action
using the supplied executor.

See the

CompletionStage

documentation for rules
covering exceptional completion.

**Parameters:** other

- the other CompletionStage
**Parameters:** action

- the action to perform before completing the
returned CompletionStage
**Parameters:** executor

- the executor to use for asynchronous execution
**Returns:** the new CompletionStage

- applyToEither

```java
<U>
CompletionStage
<U> applyToEither​(
CompletionStage
<? extends
T
> other,

Function
<? super
T
,​U> fn)
```

Returns a new CompletionStage that, when either this or the
other given stage complete normally, is executed with the
corresponding result as argument to the supplied function.

See the

CompletionStage

documentation for rules
covering exceptional completion.

**Type Parameters:** U

- the function's return type
**Parameters:** other

- the other CompletionStage
**Parameters:** fn

- the function to use to compute the value of the
returned CompletionStage
**Returns:** the new CompletionStage

- applyToEitherAsync

```java
<U>
CompletionStage
<U> applyToEitherAsync​(
CompletionStage
<? extends
T
> other,

Function
<? super
T
,​U> fn)
```

Returns a new CompletionStage that, when either this or the
other given stage complete normally, is executed using this
stage's default asynchronous execution facility, with the
corresponding result as argument to the supplied function.

See the

CompletionStage

documentation for rules
covering exceptional completion.

**Type Parameters:** U

- the function's return type
**Parameters:** other

- the other CompletionStage
**Parameters:** fn

- the function to use to compute the value of the
returned CompletionStage
**Returns:** the new CompletionStage

- applyToEitherAsync

```java
<U>
CompletionStage
<U> applyToEitherAsync​(
CompletionStage
<? extends
T
> other,

Function
<? super
T
,​U> fn,

Executor
executor)
```

Returns a new CompletionStage that, when either this or the
other given stage complete normally, is executed using the
supplied executor, with the corresponding result as argument to
the supplied function.

See the

CompletionStage

documentation for rules
covering exceptional completion.

**Type Parameters:** U

- the function's return type
**Parameters:** other

- the other CompletionStage
**Parameters:** fn

- the function to use to compute the value of the
returned CompletionStage
**Parameters:** executor

- the executor to use for asynchronous execution
**Returns:** the new CompletionStage

- acceptEither

```java
CompletionStage
<
Void
> acceptEither​(
CompletionStage
<? extends
T
> other,

Consumer
<? super
T
> action)
```

Returns a new CompletionStage that, when either this or the
other given stage complete normally, is executed with the
corresponding result as argument to the supplied action.

See the

CompletionStage

documentation for rules
covering exceptional completion.

**Parameters:** other

- the other CompletionStage
**Parameters:** action

- the action to perform before completing the
returned CompletionStage
**Returns:** the new CompletionStage

- acceptEitherAsync

```java
CompletionStage
<
Void
> acceptEitherAsync​(
CompletionStage
<? extends
T
> other,

Consumer
<? super
T
> action)
```

Returns a new CompletionStage that, when either this or the
other given stage complete normally, is executed using this
stage's default asynchronous execution facility, with the
corresponding result as argument to the supplied action.

See the

CompletionStage

documentation for rules
covering exceptional completion.

**Parameters:** other

- the other CompletionStage
**Parameters:** action

- the action to perform before completing the
returned CompletionStage
**Returns:** the new CompletionStage

- acceptEitherAsync

```java
CompletionStage
<
Void
> acceptEitherAsync​(
CompletionStage
<? extends
T
> other,

Consumer
<? super
T
> action,

Executor
executor)
```

Returns a new CompletionStage that, when either this or the
other given stage complete normally, is executed using the
supplied executor, with the corresponding result as argument to
the supplied action.

See the

CompletionStage

documentation for rules
covering exceptional completion.

**Parameters:** other

- the other CompletionStage
**Parameters:** action

- the action to perform before completing the
returned CompletionStage
**Parameters:** executor

- the executor to use for asynchronous execution
**Returns:** the new CompletionStage

- runAfterEither

```java
CompletionStage
<
Void
> runAfterEither​(
CompletionStage
<?> other,

Runnable
action)
```

Returns a new CompletionStage that, when either this or the
other given stage complete normally, executes the given action.

See the

CompletionStage

documentation for rules
covering exceptional completion.

**Parameters:** other

- the other CompletionStage
**Parameters:** action

- the action to perform before completing the
returned CompletionStage
**Returns:** the new CompletionStage

- runAfterEitherAsync

```java
CompletionStage
<
Void
> runAfterEitherAsync​(
CompletionStage
<?> other,

Runnable
action)
```

Returns a new CompletionStage that, when either this or the
other given stage complete normally, executes the given action
using this stage's default asynchronous execution facility.

See the

CompletionStage

documentation for rules
covering exceptional completion.

**Parameters:** other

- the other CompletionStage
**Parameters:** action

- the action to perform before completing the
returned CompletionStage
**Returns:** the new CompletionStage

- runAfterEitherAsync

```java
CompletionStage
<
Void
> runAfterEitherAsync​(
CompletionStage
<?> other,

Runnable
action,

Executor
executor)
```

Returns a new CompletionStage that, when either this or the
other given stage complete normally, executes the given action
using the supplied executor.

See the

CompletionStage

documentation for rules
covering exceptional completion.

**Parameters:** other

- the other CompletionStage
**Parameters:** action

- the action to perform before completing the
returned CompletionStage
**Parameters:** executor

- the executor to use for asynchronous execution
**Returns:** the new CompletionStage

- thenCompose

```java
<U>
CompletionStage
<U> thenCompose​(
Function
<? super
T
,​? extends
CompletionStage
<U>> fn)
```

Returns a new CompletionStage that is completed with the same
value as the CompletionStage returned by the given function.

When this stage completes normally, the given function is
invoked with this stage's result as the argument, returning
another CompletionStage. When that stage completes normally,
the CompletionStage returned by this method is completed with
the same value.

To ensure progress, the supplied function must arrange
eventual completion of its result.

This method is analogous to

Optional.flatMap

and

Stream.flatMap

.

See the

CompletionStage

documentation for rules
covering exceptional completion.

**Type Parameters:** U

- the type of the returned CompletionStage's result
**Parameters:** fn

- the function to use to compute another CompletionStage
**Returns:** the new CompletionStage

- thenComposeAsync

```java
<U>
CompletionStage
<U> thenComposeAsync​(
Function
<? super
T
,​? extends
CompletionStage
<U>> fn)
```

Returns a new CompletionStage that is completed with the same
value as the CompletionStage returned by the given function,
executed using this stage's default asynchronous execution
facility.

When this stage completes normally, the given function is
invoked with this stage's result as the argument, returning
another CompletionStage. When that stage completes normally,
the CompletionStage returned by this method is completed with
the same value.

To ensure progress, the supplied function must arrange
eventual completion of its result.

See the

CompletionStage

documentation for rules
covering exceptional completion.

**Type Parameters:** U

- the type of the returned CompletionStage's result
**Parameters:** fn

- the function to use to compute another CompletionStage
**Returns:** the new CompletionStage

- thenComposeAsync

```java
<U>
CompletionStage
<U> thenComposeAsync​(
Function
<? super
T
,​? extends
CompletionStage
<U>> fn,

Executor
executor)
```

Returns a new CompletionStage that is completed with the same
value as the CompletionStage returned by the given function,
executed using the supplied Executor.

When this stage completes normally, the given function is
invoked with this stage's result as the argument, returning
another CompletionStage. When that stage completes normally,
the CompletionStage returned by this method is completed with
the same value.

To ensure progress, the supplied function must arrange
eventual completion of its result.

See the

CompletionStage

documentation for rules
covering exceptional completion.

**Type Parameters:** U

- the type of the returned CompletionStage's result
**Parameters:** fn

- the function to use to compute another CompletionStage
**Parameters:** executor

- the executor to use for asynchronous execution
**Returns:** the new CompletionStage

- handle

```java
<U>
CompletionStage
<U> handle​(
BiFunction
<? super
T
,​
Throwable
,​? extends U> fn)
```

Returns a new CompletionStage that, when this stage completes
either normally or exceptionally, is executed with this stage's
result and exception as arguments to the supplied function.

When this stage is complete, the given function is invoked
with the result (or

null

if none) and the exception (or

null

if none) of this stage as arguments, and the
function's result is used to complete the returned stage.

**Type Parameters:** U

- the function's return type
**Parameters:** fn

- the function to use to compute the value of the
returned CompletionStage
**Returns:** the new CompletionStage

- handleAsync

```java
<U>
CompletionStage
<U> handleAsync​(
BiFunction
<? super
T
,​
Throwable
,​? extends U> fn)
```

Returns a new CompletionStage that, when this stage completes
either normally or exceptionally, is executed using this stage's
default asynchronous execution facility, with this stage's
result and exception as arguments to the supplied function.

When this stage is complete, the given function is invoked
with the result (or

null

if none) and the exception (or

null

if none) of this stage as arguments, and the
function's result is used to complete the returned stage.

**Type Parameters:** U

- the function's return type
**Parameters:** fn

- the function to use to compute the value of the
returned CompletionStage
**Returns:** the new CompletionStage

- handleAsync

```java
<U>
CompletionStage
<U> handleAsync​(
BiFunction
<? super
T
,​
Throwable
,​? extends U> fn,

Executor
executor)
```

Returns a new CompletionStage that, when this stage completes
either normally or exceptionally, is executed using the
supplied executor, with this stage's result and exception as
arguments to the supplied function.

When this stage is complete, the given function is invoked
with the result (or

null

if none) and the exception (or

null

if none) of this stage as arguments, and the
function's result is used to complete the returned stage.

**Type Parameters:** U

- the function's return type
**Parameters:** fn

- the function to use to compute the value of the
returned CompletionStage
**Parameters:** executor

- the executor to use for asynchronous execution
**Returns:** the new CompletionStage

- whenComplete

```java
CompletionStage
<
T
> whenComplete​(
BiConsumer
<? super
T
,​? super
Throwable
> action)
```

Returns a new CompletionStage with the same result or exception as
this stage, that executes the given action when this stage completes.

When this stage is complete, the given action is invoked
with the result (or

null

if none) and the exception (or

null

if none) of this stage as arguments. The returned
stage is completed when the action returns.

Unlike method

handle

,
this method is not designed to translate completion outcomes,
so the supplied action should not throw an exception. However,
if it does, the following rules apply: if this stage completed
normally but the supplied action throws an exception, then the
returned stage completes exceptionally with the supplied
action's exception. Or, if this stage completed exceptionally
and the supplied action throws an exception, then the returned
stage completes exceptionally with this stage's exception.

**Parameters:** action

- the action to perform
**Returns:** the new CompletionStage

- whenCompleteAsync

```java
CompletionStage
<
T
> whenCompleteAsync​(
BiConsumer
<? super
T
,​? super
Throwable
> action)
```

Returns a new CompletionStage with the same result or exception as
this stage, that executes the given action using this stage's
default asynchronous execution facility when this stage completes.

When this stage is complete, the given action is invoked with the
result (or

null

if none) and the exception (or

null

if none) of this stage as arguments. The returned stage is completed
when the action returns.

Unlike method

handleAsync

,
this method is not designed to translate completion outcomes,
so the supplied action should not throw an exception. However,
if it does, the following rules apply: If this stage completed
normally but the supplied action throws an exception, then the
returned stage completes exceptionally with the supplied
action's exception. Or, if this stage completed exceptionally
and the supplied action throws an exception, then the returned
stage completes exceptionally with this stage's exception.

**Parameters:** action

- the action to perform
**Returns:** the new CompletionStage

- whenCompleteAsync

```java
CompletionStage
<
T
> whenCompleteAsync​(
BiConsumer
<? super
T
,​? super
Throwable
> action,

Executor
executor)
```

Returns a new CompletionStage with the same result or exception as
this stage, that executes the given action using the supplied
Executor when this stage completes.

When this stage is complete, the given action is invoked with the
result (or

null

if none) and the exception (or

null

if none) of this stage as arguments. The returned stage is completed
when the action returns.

Unlike method

handleAsync

,
this method is not designed to translate completion outcomes,
so the supplied action should not throw an exception. However,
if it does, the following rules apply: If this stage completed
normally but the supplied action throws an exception, then the
returned stage completes exceptionally with the supplied
action's exception. Or, if this stage completed exceptionally
and the supplied action throws an exception, then the returned
stage completes exceptionally with this stage's exception.

**Parameters:** action

- the action to perform
**Parameters:** executor

- the executor to use for asynchronous execution
**Returns:** the new CompletionStage

- exceptionally

```java
CompletionStage
<
T
> exceptionally​(
Function
<
Throwable
,​? extends
T
> fn)
```

Returns a new CompletionStage that, when this stage completes
exceptionally, is executed with this stage's exception as the
argument to the supplied function. Otherwise, if this stage
completes normally, then the returned stage also completes
normally with the same value.

**Parameters:** fn

- the function to use to compute the value of the
returned CompletionStage if this CompletionStage completed
exceptionally
**Returns:** the new CompletionStage

- toCompletableFuture

```java
CompletableFuture
<
T
> toCompletableFuture()
```

Returns a

CompletableFuture

maintaining the same
completion properties as this stage. If this stage is already a
CompletableFuture, this method may return this stage itself.
Otherwise, invocation of this method may be equivalent in
effect to

thenApply(x -> x)

, but returning an instance
of type

CompletableFuture

.

**Returns:** the CompletableFuture

Method Detail

- thenApply

```java
<U>
CompletionStage
<U> thenApply​(
Function
<? super
T
,​? extends U> fn)
```

Returns a new CompletionStage that, when this stage completes
normally, is executed with this stage's result as the argument
to the supplied function.

This method is analogous to

Optional.map

and

Stream.map

.

See the

CompletionStage

documentation for rules
covering exceptional completion.

**Type Parameters:** U

- the function's return type
**Parameters:** fn

- the function to use to compute the value of the
returned CompletionStage
**Returns:** the new CompletionStage

- thenApplyAsync

```java
<U>
CompletionStage
<U> thenApplyAsync​(
Function
<? super
T
,​? extends U> fn)
```

Returns a new CompletionStage that, when this stage completes
normally, is executed using this stage's default asynchronous
execution facility, with this stage's result as the argument to
the supplied function.

See the

CompletionStage

documentation for rules
covering exceptional completion.

**Type Parameters:** U

- the function's return type
**Parameters:** fn

- the function to use to compute the value of the
returned CompletionStage
**Returns:** the new CompletionStage

- thenApplyAsync

```java
<U>
CompletionStage
<U> thenApplyAsync​(
Function
<? super
T
,​? extends U> fn,

Executor
executor)
```

Returns a new CompletionStage that, when this stage completes
normally, is executed using the supplied Executor, with this
stage's result as the argument to the supplied function.

See the

CompletionStage

documentation for rules
covering exceptional completion.

**Type Parameters:** U

- the function's return type
**Parameters:** fn

- the function to use to compute the value of the
returned CompletionStage
**Parameters:** executor

- the executor to use for asynchronous execution
**Returns:** the new CompletionStage

- thenAccept

```java
CompletionStage
<
Void
> thenAccept​(
Consumer
<? super
T
> action)
```

Returns a new CompletionStage that, when this stage completes
normally, is executed with this stage's result as the argument
to the supplied action.

See the

CompletionStage

documentation for rules
covering exceptional completion.

**Parameters:** action

- the action to perform before completing the
returned CompletionStage
**Returns:** the new CompletionStage

- thenAcceptAsync

```java
CompletionStage
<
Void
> thenAcceptAsync​(
Consumer
<? super
T
> action)
```

Returns a new CompletionStage that, when this stage completes
normally, is executed using this stage's default asynchronous
execution facility, with this stage's result as the argument to
the supplied action.

See the

CompletionStage

documentation for rules
covering exceptional completion.

**Parameters:** action

- the action to perform before completing the
returned CompletionStage
**Returns:** the new CompletionStage

- thenAcceptAsync

```java
CompletionStage
<
Void
> thenAcceptAsync​(
Consumer
<? super
T
> action,

Executor
executor)
```

Returns a new CompletionStage that, when this stage completes
normally, is executed using the supplied Executor, with this
stage's result as the argument to the supplied action.

See the

CompletionStage

documentation for rules
covering exceptional completion.

**Parameters:** action

- the action to perform before completing the
returned CompletionStage
**Parameters:** executor

- the executor to use for asynchronous execution
**Returns:** the new CompletionStage

- thenRun

```java
CompletionStage
<
Void
> thenRun​(
Runnable
action)
```

Returns a new CompletionStage that, when this stage completes
normally, executes the given action.

See the

CompletionStage

documentation for rules
covering exceptional completion.

**Parameters:** action

- the action to perform before completing the
returned CompletionStage
**Returns:** the new CompletionStage

- thenRunAsync

```java
CompletionStage
<
Void
> thenRunAsync​(
Runnable
action)
```

Returns a new CompletionStage that, when this stage completes
normally, executes the given action using this stage's default
asynchronous execution facility.

See the

CompletionStage

documentation for rules
covering exceptional completion.

**Parameters:** action

- the action to perform before completing the
returned CompletionStage
**Returns:** the new CompletionStage

- thenRunAsync

```java
CompletionStage
<
Void
> thenRunAsync​(
Runnable
action,

Executor
executor)
```

Returns a new CompletionStage that, when this stage completes
normally, executes the given action using the supplied Executor.

See the

CompletionStage

documentation for rules
covering exceptional completion.

**Parameters:** action

- the action to perform before completing the
returned CompletionStage
**Parameters:** executor

- the executor to use for asynchronous execution
**Returns:** the new CompletionStage

- thenCombine

```java
<U,​V>
CompletionStage
<V> thenCombine​(
CompletionStage
<? extends U> other,

BiFunction
<? super
T
,​? super U,​? extends V> fn)
```

Returns a new CompletionStage that, when this and the other
given stage both complete normally, is executed with the two
results as arguments to the supplied function.

See the

CompletionStage

documentation for rules
covering exceptional completion.

**Type Parameters:** U

- the type of the other CompletionStage's result
**Type Parameters:** V

- the function's return type
**Parameters:** other

- the other CompletionStage
**Parameters:** fn

- the function to use to compute the value of the
returned CompletionStage
**Returns:** the new CompletionStage

- thenCombineAsync

```java
<U,​V>
CompletionStage
<V> thenCombineAsync​(
CompletionStage
<? extends U> other,

BiFunction
<? super
T
,​? super U,​? extends V> fn)
```

Returns a new CompletionStage that, when this and the other
given stage both complete normally, is executed using this
stage's default asynchronous execution facility, with the two
results as arguments to the supplied function.

See the

CompletionStage

documentation for rules
covering exceptional completion.

**Type Parameters:** U

- the type of the other CompletionStage's result
**Type Parameters:** V

- the function's return type
**Parameters:** other

- the other CompletionStage
**Parameters:** fn

- the function to use to compute the value of the
returned CompletionStage
**Returns:** the new CompletionStage

- thenCombineAsync

```java
<U,​V>
CompletionStage
<V> thenCombineAsync​(
CompletionStage
<? extends U> other,

BiFunction
<? super
T
,​? super U,​? extends V> fn,

Executor
executor)
```

Returns a new CompletionStage that, when this and the other
given stage both complete normally, is executed using the
supplied executor, with the two results as arguments to the
supplied function.

See the

CompletionStage

documentation for rules
covering exceptional completion.

**Type Parameters:** U

- the type of the other CompletionStage's result
**Type Parameters:** V

- the function's return type
**Parameters:** other

- the other CompletionStage
**Parameters:** fn

- the function to use to compute the value of the
returned CompletionStage
**Parameters:** executor

- the executor to use for asynchronous execution
**Returns:** the new CompletionStage

- thenAcceptBoth

```java
<U>
CompletionStage
<
Void
> thenAcceptBoth​(
CompletionStage
<? extends U> other,

BiConsumer
<? super
T
,​? super U> action)
```

Returns a new CompletionStage that, when this and the other
given stage both complete normally, is executed with the two
results as arguments to the supplied action.

See the

CompletionStage

documentation for rules
covering exceptional completion.

**Type Parameters:** U

- the type of the other CompletionStage's result
**Parameters:** other

- the other CompletionStage
**Parameters:** action

- the action to perform before completing the
returned CompletionStage
**Returns:** the new CompletionStage

- thenAcceptBothAsync

```java
<U>
CompletionStage
<
Void
> thenAcceptBothAsync​(
CompletionStage
<? extends U> other,

BiConsumer
<? super
T
,​? super U> action)
```

Returns a new CompletionStage that, when this and the other
given stage both complete normally, is executed using this
stage's default asynchronous execution facility, with the two
results as arguments to the supplied action.

See the

CompletionStage

documentation for rules
covering exceptional completion.

**Type Parameters:** U

- the type of the other CompletionStage's result
**Parameters:** other

- the other CompletionStage
**Parameters:** action

- the action to perform before completing the
returned CompletionStage
**Returns:** the new CompletionStage

- thenAcceptBothAsync

```java
<U>
CompletionStage
<
Void
> thenAcceptBothAsync​(
CompletionStage
<? extends U> other,

BiConsumer
<? super
T
,​? super U> action,

Executor
executor)
```

Returns a new CompletionStage that, when this and the other
given stage both complete normally, is executed using the
supplied executor, with the two results as arguments to the
supplied action.

See the

CompletionStage

documentation for rules
covering exceptional completion.

**Type Parameters:** U

- the type of the other CompletionStage's result
**Parameters:** other

- the other CompletionStage
**Parameters:** action

- the action to perform before completing the
returned CompletionStage
**Parameters:** executor

- the executor to use for asynchronous execution
**Returns:** the new CompletionStage

- runAfterBoth

```java
CompletionStage
<
Void
> runAfterBoth​(
CompletionStage
<?> other,

Runnable
action)
```

Returns a new CompletionStage that, when this and the other
given stage both complete normally, executes the given action.

See the

CompletionStage

documentation for rules
covering exceptional completion.

**Parameters:** other

- the other CompletionStage
**Parameters:** action

- the action to perform before completing the
returned CompletionStage
**Returns:** the new CompletionStage

- runAfterBothAsync

```java
CompletionStage
<
Void
> runAfterBothAsync​(
CompletionStage
<?> other,

Runnable
action)
```

Returns a new CompletionStage that, when this and the other
given stage both complete normally, executes the given action
using this stage's default asynchronous execution facility.

See the

CompletionStage

documentation for rules
covering exceptional completion.

**Parameters:** other

- the other CompletionStage
**Parameters:** action

- the action to perform before completing the
returned CompletionStage
**Returns:** the new CompletionStage

- runAfterBothAsync

```java
CompletionStage
<
Void
> runAfterBothAsync​(
CompletionStage
<?> other,

Runnable
action,

Executor
executor)
```

Returns a new CompletionStage that, when this and the other
given stage both complete normally, executes the given action
using the supplied executor.

See the

CompletionStage

documentation for rules
covering exceptional completion.

**Parameters:** other

- the other CompletionStage
**Parameters:** action

- the action to perform before completing the
returned CompletionStage
**Parameters:** executor

- the executor to use for asynchronous execution
**Returns:** the new CompletionStage

- applyToEither

```java
<U>
CompletionStage
<U> applyToEither​(
CompletionStage
<? extends
T
> other,

Function
<? super
T
,​U> fn)
```

Returns a new CompletionStage that, when either this or the
other given stage complete normally, is executed with the
corresponding result as argument to the supplied function.

See the

CompletionStage

documentation for rules
covering exceptional completion.

**Type Parameters:** U

- the function's return type
**Parameters:** other

- the other CompletionStage
**Parameters:** fn

- the function to use to compute the value of the
returned CompletionStage
**Returns:** the new CompletionStage

- applyToEitherAsync

```java
<U>
CompletionStage
<U> applyToEitherAsync​(
CompletionStage
<? extends
T
> other,

Function
<? super
T
,​U> fn)
```

Returns a new CompletionStage that, when either this or the
other given stage complete normally, is executed using this
stage's default asynchronous execution facility, with the
corresponding result as argument to the supplied function.

See the

CompletionStage

documentation for rules
covering exceptional completion.

**Type Parameters:** U

- the function's return type
**Parameters:** other

- the other CompletionStage
**Parameters:** fn

- the function to use to compute the value of the
returned CompletionStage
**Returns:** the new CompletionStage

- applyToEitherAsync

```java
<U>
CompletionStage
<U> applyToEitherAsync​(
CompletionStage
<? extends
T
> other,

Function
<? super
T
,​U> fn,

Executor
executor)
```

Returns a new CompletionStage that, when either this or the
other given stage complete normally, is executed using the
supplied executor, with the corresponding result as argument to
the supplied function.

See the

CompletionStage

documentation for rules
covering exceptional completion.

**Type Parameters:** U

- the function's return type
**Parameters:** other

- the other CompletionStage
**Parameters:** fn

- the function to use to compute the value of the
returned CompletionStage
**Parameters:** executor

- the executor to use for asynchronous execution
**Returns:** the new CompletionStage

- acceptEither

```java
CompletionStage
<
Void
> acceptEither​(
CompletionStage
<? extends
T
> other,

Consumer
<? super
T
> action)
```

Returns a new CompletionStage that, when either this or the
other given stage complete normally, is executed with the
corresponding result as argument to the supplied action.

See the

CompletionStage

documentation for rules
covering exceptional completion.

**Parameters:** other

- the other CompletionStage
**Parameters:** action

- the action to perform before completing the
returned CompletionStage
**Returns:** the new CompletionStage

- acceptEitherAsync

```java
CompletionStage
<
Void
> acceptEitherAsync​(
CompletionStage
<? extends
T
> other,

Consumer
<? super
T
> action)
```

Returns a new CompletionStage that, when either this or the
other given stage complete normally, is executed using this
stage's default asynchronous execution facility, with the
corresponding result as argument to the supplied action.

See the

CompletionStage

documentation for rules
covering exceptional completion.

**Parameters:** other

- the other CompletionStage
**Parameters:** action

- the action to perform before completing the
returned CompletionStage
**Returns:** the new CompletionStage

- acceptEitherAsync

```java
CompletionStage
<
Void
> acceptEitherAsync​(
CompletionStage
<? extends
T
> other,

Consumer
<? super
T
> action,

Executor
executor)
```

Returns a new CompletionStage that, when either this or the
other given stage complete normally, is executed using the
supplied executor, with the corresponding result as argument to
the supplied action.

See the

CompletionStage

documentation for rules
covering exceptional completion.

**Parameters:** other

- the other CompletionStage
**Parameters:** action

- the action to perform before completing the
returned CompletionStage
**Parameters:** executor

- the executor to use for asynchronous execution
**Returns:** the new CompletionStage

- runAfterEither

```java
CompletionStage
<
Void
> runAfterEither​(
CompletionStage
<?> other,

Runnable
action)
```

Returns a new CompletionStage that, when either this or the
other given stage complete normally, executes the given action.

See the

CompletionStage

documentation for rules
covering exceptional completion.

**Parameters:** other

- the other CompletionStage
**Parameters:** action

- the action to perform before completing the
returned CompletionStage
**Returns:** the new CompletionStage

- runAfterEitherAsync

```java
CompletionStage
<
Void
> runAfterEitherAsync​(
CompletionStage
<?> other,

Runnable
action)
```

Returns a new CompletionStage that, when either this or the
other given stage complete normally, executes the given action
using this stage's default asynchronous execution facility.

See the

CompletionStage

documentation for rules
covering exceptional completion.

**Parameters:** other

- the other CompletionStage
**Parameters:** action

- the action to perform before completing the
returned CompletionStage
**Returns:** the new CompletionStage

- runAfterEitherAsync

```java
CompletionStage
<
Void
> runAfterEitherAsync​(
CompletionStage
<?> other,

Runnable
action,

Executor
executor)
```

Returns a new CompletionStage that, when either this or the
other given stage complete normally, executes the given action
using the supplied executor.

See the

CompletionStage

documentation for rules
covering exceptional completion.

**Parameters:** other

- the other CompletionStage
**Parameters:** action

- the action to perform before completing the
returned CompletionStage
**Parameters:** executor

- the executor to use for asynchronous execution
**Returns:** the new CompletionStage

- thenCompose

```java
<U>
CompletionStage
<U> thenCompose​(
Function
<? super
T
,​? extends
CompletionStage
<U>> fn)
```

Returns a new CompletionStage that is completed with the same
value as the CompletionStage returned by the given function.

When this stage completes normally, the given function is
invoked with this stage's result as the argument, returning
another CompletionStage. When that stage completes normally,
the CompletionStage returned by this method is completed with
the same value.

To ensure progress, the supplied function must arrange
eventual completion of its result.

This method is analogous to

Optional.flatMap

and

Stream.flatMap

.

See the

CompletionStage

documentation for rules
covering exceptional completion.

**Type Parameters:** U

- the type of the returned CompletionStage's result
**Parameters:** fn

- the function to use to compute another CompletionStage
**Returns:** the new CompletionStage

- thenComposeAsync

```java
<U>
CompletionStage
<U> thenComposeAsync​(
Function
<? super
T
,​? extends
CompletionStage
<U>> fn)
```

Returns a new CompletionStage that is completed with the same
value as the CompletionStage returned by the given function,
executed using this stage's default asynchronous execution
facility.

When this stage completes normally, the given function is
invoked with this stage's result as the argument, returning
another CompletionStage. When that stage completes normally,
the CompletionStage returned by this method is completed with
the same value.

To ensure progress, the supplied function must arrange
eventual completion of its result.

See the

CompletionStage

documentation for rules
covering exceptional completion.

**Type Parameters:** U

- the type of the returned CompletionStage's result
**Parameters:** fn

- the function to use to compute another CompletionStage
**Returns:** the new CompletionStage

- thenComposeAsync

```java
<U>
CompletionStage
<U> thenComposeAsync​(
Function
<? super
T
,​? extends
CompletionStage
<U>> fn,

Executor
executor)
```

Returns a new CompletionStage that is completed with the same
value as the CompletionStage returned by the given function,
executed using the supplied Executor.

When this stage completes normally, the given function is
invoked with this stage's result as the argument, returning
another CompletionStage. When that stage completes normally,
the CompletionStage returned by this method is completed with
the same value.

To ensure progress, the supplied function must arrange
eventual completion of its result.

See the

CompletionStage

documentation for rules
covering exceptional completion.

**Type Parameters:** U

- the type of the returned CompletionStage's result
**Parameters:** fn

- the function to use to compute another CompletionStage
**Parameters:** executor

- the executor to use for asynchronous execution
**Returns:** the new CompletionStage

- handle

```java
<U>
CompletionStage
<U> handle​(
BiFunction
<? super
T
,​
Throwable
,​? extends U> fn)
```

Returns a new CompletionStage that, when this stage completes
either normally or exceptionally, is executed with this stage's
result and exception as arguments to the supplied function.

When this stage is complete, the given function is invoked
with the result (or

null

if none) and the exception (or

null

if none) of this stage as arguments, and the
function's result is used to complete the returned stage.

**Type Parameters:** U

- the function's return type
**Parameters:** fn

- the function to use to compute the value of the
returned CompletionStage
**Returns:** the new CompletionStage

- handleAsync

```java
<U>
CompletionStage
<U> handleAsync​(
BiFunction
<? super
T
,​
Throwable
,​? extends U> fn)
```

Returns a new CompletionStage that, when this stage completes
either normally or exceptionally, is executed using this stage's
default asynchronous execution facility, with this stage's
result and exception as arguments to the supplied function.

When this stage is complete, the given function is invoked
with the result (or

null

if none) and the exception (or

null

if none) of this stage as arguments, and the
function's result is used to complete the returned stage.

**Type Parameters:** U

- the function's return type
**Parameters:** fn

- the function to use to compute the value of the
returned CompletionStage
**Returns:** the new CompletionStage

- handleAsync

```java
<U>
CompletionStage
<U> handleAsync​(
BiFunction
<? super
T
,​
Throwable
,​? extends U> fn,

Executor
executor)
```

Returns a new CompletionStage that, when this stage completes
either normally or exceptionally, is executed using the
supplied executor, with this stage's result and exception as
arguments to the supplied function.

When this stage is complete, the given function is invoked
with the result (or

null

if none) and the exception (or

null

if none) of this stage as arguments, and the
function's result is used to complete the returned stage.

**Type Parameters:** U

- the function's return type
**Parameters:** fn

- the function to use to compute the value of the
returned CompletionStage
**Parameters:** executor

- the executor to use for asynchronous execution
**Returns:** the new CompletionStage

- whenComplete

```java
CompletionStage
<
T
> whenComplete​(
BiConsumer
<? super
T
,​? super
Throwable
> action)
```

Returns a new CompletionStage with the same result or exception as
this stage, that executes the given action when this stage completes.

When this stage is complete, the given action is invoked
with the result (or

null

if none) and the exception (or

null

if none) of this stage as arguments. The returned
stage is completed when the action returns.

Unlike method

handle

,
this method is not designed to translate completion outcomes,
so the supplied action should not throw an exception. However,
if it does, the following rules apply: if this stage completed
normally but the supplied action throws an exception, then the
returned stage completes exceptionally with the supplied
action's exception. Or, if this stage completed exceptionally
and the supplied action throws an exception, then the returned
stage completes exceptionally with this stage's exception.

**Parameters:** action

- the action to perform
**Returns:** the new CompletionStage

- whenCompleteAsync

```java
CompletionStage
<
T
> whenCompleteAsync​(
BiConsumer
<? super
T
,​? super
Throwable
> action)
```

Returns a new CompletionStage with the same result or exception as
this stage, that executes the given action using this stage's
default asynchronous execution facility when this stage completes.

When this stage is complete, the given action is invoked with the
result (or

null

if none) and the exception (or

null

if none) of this stage as arguments. The returned stage is completed
when the action returns.

Unlike method

handleAsync

,
this method is not designed to translate completion outcomes,
so the supplied action should not throw an exception. However,
if it does, the following rules apply: If this stage completed
normally but the supplied action throws an exception, then the
returned stage completes exceptionally with the supplied
action's exception. Or, if this stage completed exceptionally
and the supplied action throws an exception, then the returned
stage completes exceptionally with this stage's exception.

**Parameters:** action

- the action to perform
**Returns:** the new CompletionStage

- whenCompleteAsync

```java
CompletionStage
<
T
> whenCompleteAsync​(
BiConsumer
<? super
T
,​? super
Throwable
> action,

Executor
executor)
```

Returns a new CompletionStage with the same result or exception as
this stage, that executes the given action using the supplied
Executor when this stage completes.

When this stage is complete, the given action is invoked with the
result (or

null

if none) and the exception (or

null

if none) of this stage as arguments. The returned stage is completed
when the action returns.

Unlike method

handleAsync

,
this method is not designed to translate completion outcomes,
so the supplied action should not throw an exception. However,
if it does, the following rules apply: If this stage completed
normally but the supplied action throws an exception, then the
returned stage completes exceptionally with the supplied
action's exception. Or, if this stage completed exceptionally
and the supplied action throws an exception, then the returned
stage completes exceptionally with this stage's exception.

**Parameters:** action

- the action to perform
**Parameters:** executor

- the executor to use for asynchronous execution
**Returns:** the new CompletionStage

- exceptionally

```java
CompletionStage
<
T
> exceptionally​(
Function
<
Throwable
,​? extends
T
> fn)
```

Returns a new CompletionStage that, when this stage completes
exceptionally, is executed with this stage's exception as the
argument to the supplied function. Otherwise, if this stage
completes normally, then the returned stage also completes
normally with the same value.

**Parameters:** fn

- the function to use to compute the value of the
returned CompletionStage if this CompletionStage completed
exceptionally
**Returns:** the new CompletionStage

- toCompletableFuture

```java
CompletableFuture
<
T
> toCompletableFuture()
```

Returns a

CompletableFuture

maintaining the same
completion properties as this stage. If this stage is already a
CompletableFuture, this method may return this stage itself.
Otherwise, invocation of this method may be equivalent in
effect to

thenApply(x -> x)

, but returning an instance
of type

CompletableFuture

.

**Returns:** the CompletableFuture

---

#### Method Detail

thenApply

```java
<U>
CompletionStage
<U> thenApply​(
Function
<? super
T
,​? extends U> fn)
```

Returns a new CompletionStage that, when this stage completes
normally, is executed with this stage's result as the argument
to the supplied function.

This method is analogous to

Optional.map

and

Stream.map

.

See the

CompletionStage

documentation for rules
covering exceptional completion.

**Type Parameters:** U

- the function's return type
**Parameters:** fn

- the function to use to compute the value of the
returned CompletionStage
**Returns:** the new CompletionStage

---

#### thenApply

<U>

CompletionStage

<U> thenApply​(

Function

<? super

T

,​? extends U> fn)

Returns a new CompletionStage that, when this stage completes
normally, is executed with this stage's result as the argument
to the supplied function.

This method is analogous to

Optional.map

and

Stream.map

.

See the

CompletionStage

documentation for rules
covering exceptional completion.

This method is analogous to

Optional.map

and

Stream.map

.

See the

CompletionStage

documentation for rules
covering exceptional completion.

See the

CompletionStage

documentation for rules
covering exceptional completion.

thenApplyAsync

```java
<U>
CompletionStage
<U> thenApplyAsync​(
Function
<? super
T
,​? extends U> fn)
```

Returns a new CompletionStage that, when this stage completes
normally, is executed using this stage's default asynchronous
execution facility, with this stage's result as the argument to
the supplied function.

See the

CompletionStage

documentation for rules
covering exceptional completion.

**Type Parameters:** U

- the function's return type
**Parameters:** fn

- the function to use to compute the value of the
returned CompletionStage
**Returns:** the new CompletionStage

---

#### thenApplyAsync

<U>

CompletionStage

<U> thenApplyAsync​(

Function

<? super

T

,​? extends U> fn)

Returns a new CompletionStage that, when this stage completes
normally, is executed using this stage's default asynchronous
execution facility, with this stage's result as the argument to
the supplied function.

See the

CompletionStage

documentation for rules
covering exceptional completion.

thenApplyAsync

```java
<U>
CompletionStage
<U> thenApplyAsync​(
Function
<? super
T
,​? extends U> fn,

Executor
executor)
```

Returns a new CompletionStage that, when this stage completes
normally, is executed using the supplied Executor, with this
stage's result as the argument to the supplied function.

See the

CompletionStage

documentation for rules
covering exceptional completion.

**Type Parameters:** U

- the function's return type
**Parameters:** fn

- the function to use to compute the value of the
returned CompletionStage
**Parameters:** executor

- the executor to use for asynchronous execution
**Returns:** the new CompletionStage

---

#### thenApplyAsync

<U>

CompletionStage

<U> thenApplyAsync​(

Function

<? super

T

,​? extends U> fn,

Executor

executor)

Returns a new CompletionStage that, when this stage completes
normally, is executed using the supplied Executor, with this
stage's result as the argument to the supplied function.

See the

CompletionStage

documentation for rules
covering exceptional completion.

thenAccept

```java
CompletionStage
<
Void
> thenAccept​(
Consumer
<? super
T
> action)
```

Returns a new CompletionStage that, when this stage completes
normally, is executed with this stage's result as the argument
to the supplied action.

See the

CompletionStage

documentation for rules
covering exceptional completion.

**Parameters:** action

- the action to perform before completing the
returned CompletionStage
**Returns:** the new CompletionStage

---

#### thenAccept

CompletionStage

<

Void

> thenAccept​(

Consumer

<? super

T

> action)

Returns a new CompletionStage that, when this stage completes
normally, is executed with this stage's result as the argument
to the supplied action.

See the

CompletionStage

documentation for rules
covering exceptional completion.

thenAcceptAsync

```java
CompletionStage
<
Void
> thenAcceptAsync​(
Consumer
<? super
T
> action)
```

Returns a new CompletionStage that, when this stage completes
normally, is executed using this stage's default asynchronous
execution facility, with this stage's result as the argument to
the supplied action.

See the

CompletionStage

documentation for rules
covering exceptional completion.

**Parameters:** action

- the action to perform before completing the
returned CompletionStage
**Returns:** the new CompletionStage

---

#### thenAcceptAsync

CompletionStage

<

Void

> thenAcceptAsync​(

Consumer

<? super

T

> action)

Returns a new CompletionStage that, when this stage completes
normally, is executed using this stage's default asynchronous
execution facility, with this stage's result as the argument to
the supplied action.

See the

CompletionStage

documentation for rules
covering exceptional completion.

thenAcceptAsync

```java
CompletionStage
<
Void
> thenAcceptAsync​(
Consumer
<? super
T
> action,

Executor
executor)
```

Returns a new CompletionStage that, when this stage completes
normally, is executed using the supplied Executor, with this
stage's result as the argument to the supplied action.

See the

CompletionStage

documentation for rules
covering exceptional completion.

**Parameters:** action

- the action to perform before completing the
returned CompletionStage
**Parameters:** executor

- the executor to use for asynchronous execution
**Returns:** the new CompletionStage

---

#### thenAcceptAsync

CompletionStage

<

Void

> thenAcceptAsync​(

Consumer

<? super

T

> action,

Executor

executor)

Returns a new CompletionStage that, when this stage completes
normally, is executed using the supplied Executor, with this
stage's result as the argument to the supplied action.

See the

CompletionStage

documentation for rules
covering exceptional completion.

thenRun

```java
CompletionStage
<
Void
> thenRun​(
Runnable
action)
```

Returns a new CompletionStage that, when this stage completes
normally, executes the given action.

See the

CompletionStage

documentation for rules
covering exceptional completion.

**Parameters:** action

- the action to perform before completing the
returned CompletionStage
**Returns:** the new CompletionStage

---

#### thenRun

CompletionStage

<

Void

> thenRun​(

Runnable

action)

Returns a new CompletionStage that, when this stage completes
normally, executes the given action.

See the

CompletionStage

documentation for rules
covering exceptional completion.

thenRunAsync

```java
CompletionStage
<
Void
> thenRunAsync​(
Runnable
action)
```

Returns a new CompletionStage that, when this stage completes
normally, executes the given action using this stage's default
asynchronous execution facility.

See the

CompletionStage

documentation for rules
covering exceptional completion.

**Parameters:** action

- the action to perform before completing the
returned CompletionStage
**Returns:** the new CompletionStage

---

#### thenRunAsync

CompletionStage

<

Void

> thenRunAsync​(

Runnable

action)

Returns a new CompletionStage that, when this stage completes
normally, executes the given action using this stage's default
asynchronous execution facility.

See the

CompletionStage

documentation for rules
covering exceptional completion.

thenRunAsync

```java
CompletionStage
<
Void
> thenRunAsync​(
Runnable
action,

Executor
executor)
```

Returns a new CompletionStage that, when this stage completes
normally, executes the given action using the supplied Executor.

See the

CompletionStage

documentation for rules
covering exceptional completion.

**Parameters:** action

- the action to perform before completing the
returned CompletionStage
**Parameters:** executor

- the executor to use for asynchronous execution
**Returns:** the new CompletionStage

---

#### thenRunAsync

CompletionStage

<

Void

> thenRunAsync​(

Runnable

action,

Executor

executor)

Returns a new CompletionStage that, when this stage completes
normally, executes the given action using the supplied Executor.

See the

CompletionStage

documentation for rules
covering exceptional completion.

thenCombine

```java
<U,​V>
CompletionStage
<V> thenCombine​(
CompletionStage
<? extends U> other,

BiFunction
<? super
T
,​? super U,​? extends V> fn)
```

Returns a new CompletionStage that, when this and the other
given stage both complete normally, is executed with the two
results as arguments to the supplied function.

See the

CompletionStage

documentation for rules
covering exceptional completion.

**Type Parameters:** U

- the type of the other CompletionStage's result
**Type Parameters:** V

- the function's return type
**Parameters:** other

- the other CompletionStage
**Parameters:** fn

- the function to use to compute the value of the
returned CompletionStage
**Returns:** the new CompletionStage

---

#### thenCombine

<U,​V>

CompletionStage

<V> thenCombine​(

CompletionStage

<? extends U> other,

BiFunction

<? super

T

,​? super U,​? extends V> fn)

Returns a new CompletionStage that, when this and the other
given stage both complete normally, is executed with the two
results as arguments to the supplied function.

See the

CompletionStage

documentation for rules
covering exceptional completion.

thenCombineAsync

```java
<U,​V>
CompletionStage
<V> thenCombineAsync​(
CompletionStage
<? extends U> other,

BiFunction
<? super
T
,​? super U,​? extends V> fn)
```

Returns a new CompletionStage that, when this and the other
given stage both complete normally, is executed using this
stage's default asynchronous execution facility, with the two
results as arguments to the supplied function.

See the

CompletionStage

documentation for rules
covering exceptional completion.

**Type Parameters:** U

- the type of the other CompletionStage's result
**Type Parameters:** V

- the function's return type
**Parameters:** other

- the other CompletionStage
**Parameters:** fn

- the function to use to compute the value of the
returned CompletionStage
**Returns:** the new CompletionStage

---

#### thenCombineAsync

<U,​V>

CompletionStage

<V> thenCombineAsync​(

CompletionStage

<? extends U> other,

BiFunction

<? super

T

,​? super U,​? extends V> fn)

Returns a new CompletionStage that, when this and the other
given stage both complete normally, is executed using this
stage's default asynchronous execution facility, with the two
results as arguments to the supplied function.

See the

CompletionStage

documentation for rules
covering exceptional completion.

thenCombineAsync

```java
<U,​V>
CompletionStage
<V> thenCombineAsync​(
CompletionStage
<? extends U> other,

BiFunction
<? super
T
,​? super U,​? extends V> fn,

Executor
executor)
```

Returns a new CompletionStage that, when this and the other
given stage both complete normally, is executed using the
supplied executor, with the two results as arguments to the
supplied function.

See the

CompletionStage

documentation for rules
covering exceptional completion.

**Type Parameters:** U

- the type of the other CompletionStage's result
**Type Parameters:** V

- the function's return type
**Parameters:** other

- the other CompletionStage
**Parameters:** fn

- the function to use to compute the value of the
returned CompletionStage
**Parameters:** executor

- the executor to use for asynchronous execution
**Returns:** the new CompletionStage

---

#### thenCombineAsync

<U,​V>

CompletionStage

<V> thenCombineAsync​(

CompletionStage

<? extends U> other,

BiFunction

<? super

T

,​? super U,​? extends V> fn,

Executor

executor)

Returns a new CompletionStage that, when this and the other
given stage both complete normally, is executed using the
supplied executor, with the two results as arguments to the
supplied function.

See the

CompletionStage

documentation for rules
covering exceptional completion.

thenAcceptBoth

```java
<U>
CompletionStage
<
Void
> thenAcceptBoth​(
CompletionStage
<? extends U> other,

BiConsumer
<? super
T
,​? super U> action)
```

Returns a new CompletionStage that, when this and the other
given stage both complete normally, is executed with the two
results as arguments to the supplied action.

See the

CompletionStage

documentation for rules
covering exceptional completion.

**Type Parameters:** U

- the type of the other CompletionStage's result
**Parameters:** other

- the other CompletionStage
**Parameters:** action

- the action to perform before completing the
returned CompletionStage
**Returns:** the new CompletionStage

---

#### thenAcceptBoth

<U>

CompletionStage

<

Void

> thenAcceptBoth​(

CompletionStage

<? extends U> other,

BiConsumer

<? super

T

,​? super U> action)

Returns a new CompletionStage that, when this and the other
given stage both complete normally, is executed with the two
results as arguments to the supplied action.

See the

CompletionStage

documentation for rules
covering exceptional completion.

thenAcceptBothAsync

```java
<U>
CompletionStage
<
Void
> thenAcceptBothAsync​(
CompletionStage
<? extends U> other,

BiConsumer
<? super
T
,​? super U> action)
```

Returns a new CompletionStage that, when this and the other
given stage both complete normally, is executed using this
stage's default asynchronous execution facility, with the two
results as arguments to the supplied action.

See the

CompletionStage

documentation for rules
covering exceptional completion.

**Type Parameters:** U

- the type of the other CompletionStage's result
**Parameters:** other

- the other CompletionStage
**Parameters:** action

- the action to perform before completing the
returned CompletionStage
**Returns:** the new CompletionStage

---

#### thenAcceptBothAsync

<U>

CompletionStage

<

Void

> thenAcceptBothAsync​(

CompletionStage

<? extends U> other,

BiConsumer

<? super

T

,​? super U> action)

Returns a new CompletionStage that, when this and the other
given stage both complete normally, is executed using this
stage's default asynchronous execution facility, with the two
results as arguments to the supplied action.

See the

CompletionStage

documentation for rules
covering exceptional completion.

thenAcceptBothAsync

```java
<U>
CompletionStage
<
Void
> thenAcceptBothAsync​(
CompletionStage
<? extends U> other,

BiConsumer
<? super
T
,​? super U> action,

Executor
executor)
```

Returns a new CompletionStage that, when this and the other
given stage both complete normally, is executed using the
supplied executor, with the two results as arguments to the
supplied action.

See the

CompletionStage

documentation for rules
covering exceptional completion.

**Type Parameters:** U

- the type of the other CompletionStage's result
**Parameters:** other

- the other CompletionStage
**Parameters:** action

- the action to perform before completing the
returned CompletionStage
**Parameters:** executor

- the executor to use for asynchronous execution
**Returns:** the new CompletionStage

---

#### thenAcceptBothAsync

<U>

CompletionStage

<

Void

> thenAcceptBothAsync​(

CompletionStage

<? extends U> other,

BiConsumer

<? super

T

,​? super U> action,

Executor

executor)

Returns a new CompletionStage that, when this and the other
given stage both complete normally, is executed using the
supplied executor, with the two results as arguments to the
supplied action.

See the

CompletionStage

documentation for rules
covering exceptional completion.

runAfterBoth

```java
CompletionStage
<
Void
> runAfterBoth​(
CompletionStage
<?> other,

Runnable
action)
```

Returns a new CompletionStage that, when this and the other
given stage both complete normally, executes the given action.

See the

CompletionStage

documentation for rules
covering exceptional completion.

**Parameters:** other

- the other CompletionStage
**Parameters:** action

- the action to perform before completing the
returned CompletionStage
**Returns:** the new CompletionStage

---

#### runAfterBoth

CompletionStage

<

Void

> runAfterBoth​(

CompletionStage

<?> other,

Runnable

action)

Returns a new CompletionStage that, when this and the other
given stage both complete normally, executes the given action.

See the

CompletionStage

documentation for rules
covering exceptional completion.

runAfterBothAsync

```java
CompletionStage
<
Void
> runAfterBothAsync​(
CompletionStage
<?> other,

Runnable
action)
```

Returns a new CompletionStage that, when this and the other
given stage both complete normally, executes the given action
using this stage's default asynchronous execution facility.

See the

CompletionStage

documentation for rules
covering exceptional completion.

**Parameters:** other

- the other CompletionStage
**Parameters:** action

- the action to perform before completing the
returned CompletionStage
**Returns:** the new CompletionStage

---

#### runAfterBothAsync

CompletionStage

<

Void

> runAfterBothAsync​(

CompletionStage

<?> other,

Runnable

action)

Returns a new CompletionStage that, when this and the other
given stage both complete normally, executes the given action
using this stage's default asynchronous execution facility.

See the

CompletionStage

documentation for rules
covering exceptional completion.

runAfterBothAsync

```java
CompletionStage
<
Void
> runAfterBothAsync​(
CompletionStage
<?> other,

Runnable
action,

Executor
executor)
```

Returns a new CompletionStage that, when this and the other
given stage both complete normally, executes the given action
using the supplied executor.

See the

CompletionStage

documentation for rules
covering exceptional completion.

**Parameters:** other

- the other CompletionStage
**Parameters:** action

- the action to perform before completing the
returned CompletionStage
**Parameters:** executor

- the executor to use for asynchronous execution
**Returns:** the new CompletionStage

---

#### runAfterBothAsync

CompletionStage

<

Void

> runAfterBothAsync​(

CompletionStage

<?> other,

Runnable

action,

Executor

executor)

Returns a new CompletionStage that, when this and the other
given stage both complete normally, executes the given action
using the supplied executor.

See the

CompletionStage

documentation for rules
covering exceptional completion.

applyToEither

```java
<U>
CompletionStage
<U> applyToEither​(
CompletionStage
<? extends
T
> other,

Function
<? super
T
,​U> fn)
```

Returns a new CompletionStage that, when either this or the
other given stage complete normally, is executed with the
corresponding result as argument to the supplied function.

See the

CompletionStage

documentation for rules
covering exceptional completion.

**Type Parameters:** U

- the function's return type
**Parameters:** other

- the other CompletionStage
**Parameters:** fn

- the function to use to compute the value of the
returned CompletionStage
**Returns:** the new CompletionStage

---

#### applyToEither

<U>

CompletionStage

<U> applyToEither​(

CompletionStage

<? extends

T

> other,

Function

<? super

T

,​U> fn)

Returns a new CompletionStage that, when either this or the
other given stage complete normally, is executed with the
corresponding result as argument to the supplied function.

See the

CompletionStage

documentation for rules
covering exceptional completion.

applyToEitherAsync

```java
<U>
CompletionStage
<U> applyToEitherAsync​(
CompletionStage
<? extends
T
> other,

Function
<? super
T
,​U> fn)
```

Returns a new CompletionStage that, when either this or the
other given stage complete normally, is executed using this
stage's default asynchronous execution facility, with the
corresponding result as argument to the supplied function.

See the

CompletionStage

documentation for rules
covering exceptional completion.

**Type Parameters:** U

- the function's return type
**Parameters:** other

- the other CompletionStage
**Parameters:** fn

- the function to use to compute the value of the
returned CompletionStage
**Returns:** the new CompletionStage

---

#### applyToEitherAsync

<U>

CompletionStage

<U> applyToEitherAsync​(

CompletionStage

<? extends

T

> other,

Function

<? super

T

,​U> fn)

Returns a new CompletionStage that, when either this or the
other given stage complete normally, is executed using this
stage's default asynchronous execution facility, with the
corresponding result as argument to the supplied function.

See the

CompletionStage

documentation for rules
covering exceptional completion.

applyToEitherAsync

```java
<U>
CompletionStage
<U> applyToEitherAsync​(
CompletionStage
<? extends
T
> other,

Function
<? super
T
,​U> fn,

Executor
executor)
```

Returns a new CompletionStage that, when either this or the
other given stage complete normally, is executed using the
supplied executor, with the corresponding result as argument to
the supplied function.

See the

CompletionStage

documentation for rules
covering exceptional completion.

**Type Parameters:** U

- the function's return type
**Parameters:** other

- the other CompletionStage
**Parameters:** fn

- the function to use to compute the value of the
returned CompletionStage
**Parameters:** executor

- the executor to use for asynchronous execution
**Returns:** the new CompletionStage

---

#### applyToEitherAsync

<U>

CompletionStage

<U> applyToEitherAsync​(

CompletionStage

<? extends

T

> other,

Function

<? super

T

,​U> fn,

Executor

executor)

Returns a new CompletionStage that, when either this or the
other given stage complete normally, is executed using the
supplied executor, with the corresponding result as argument to
the supplied function.

See the

CompletionStage

documentation for rules
covering exceptional completion.

acceptEither

```java
CompletionStage
<
Void
> acceptEither​(
CompletionStage
<? extends
T
> other,

Consumer
<? super
T
> action)
```

Returns a new CompletionStage that, when either this or the
other given stage complete normally, is executed with the
corresponding result as argument to the supplied action.

See the

CompletionStage

documentation for rules
covering exceptional completion.

**Parameters:** other

- the other CompletionStage
**Parameters:** action

- the action to perform before completing the
returned CompletionStage
**Returns:** the new CompletionStage

---

#### acceptEither

CompletionStage

<

Void

> acceptEither​(

CompletionStage

<? extends

T

> other,

Consumer

<? super

T

> action)

Returns a new CompletionStage that, when either this or the
other given stage complete normally, is executed with the
corresponding result as argument to the supplied action.

See the

CompletionStage

documentation for rules
covering exceptional completion.

acceptEitherAsync

```java
CompletionStage
<
Void
> acceptEitherAsync​(
CompletionStage
<? extends
T
> other,

Consumer
<? super
T
> action)
```

Returns a new CompletionStage that, when either this or the
other given stage complete normally, is executed using this
stage's default asynchronous execution facility, with the
corresponding result as argument to the supplied action.

See the

CompletionStage

documentation for rules
covering exceptional completion.

**Parameters:** other

- the other CompletionStage
**Parameters:** action

- the action to perform before completing the
returned CompletionStage
**Returns:** the new CompletionStage

---

#### acceptEitherAsync

CompletionStage

<

Void

> acceptEitherAsync​(

CompletionStage

<? extends

T

> other,

Consumer

<? super

T

> action)

Returns a new CompletionStage that, when either this or the
other given stage complete normally, is executed using this
stage's default asynchronous execution facility, with the
corresponding result as argument to the supplied action.

See the

CompletionStage

documentation for rules
covering exceptional completion.

acceptEitherAsync

```java
CompletionStage
<
Void
> acceptEitherAsync​(
CompletionStage
<? extends
T
> other,

Consumer
<? super
T
> action,

Executor
executor)
```

Returns a new CompletionStage that, when either this or the
other given stage complete normally, is executed using the
supplied executor, with the corresponding result as argument to
the supplied action.

See the

CompletionStage

documentation for rules
covering exceptional completion.

**Parameters:** other

- the other CompletionStage
**Parameters:** action

- the action to perform before completing the
returned CompletionStage
**Parameters:** executor

- the executor to use for asynchronous execution
**Returns:** the new CompletionStage

---

#### acceptEitherAsync

CompletionStage

<

Void

> acceptEitherAsync​(

CompletionStage

<? extends

T

> other,

Consumer

<? super

T

> action,

Executor

executor)

Returns a new CompletionStage that, when either this or the
other given stage complete normally, is executed using the
supplied executor, with the corresponding result as argument to
the supplied action.

See the

CompletionStage

documentation for rules
covering exceptional completion.

runAfterEither

```java
CompletionStage
<
Void
> runAfterEither​(
CompletionStage
<?> other,

Runnable
action)
```

Returns a new CompletionStage that, when either this or the
other given stage complete normally, executes the given action.

See the

CompletionStage

documentation for rules
covering exceptional completion.

**Parameters:** other

- the other CompletionStage
**Parameters:** action

- the action to perform before completing the
returned CompletionStage
**Returns:** the new CompletionStage

---

#### runAfterEither

CompletionStage

<

Void

> runAfterEither​(

CompletionStage

<?> other,

Runnable

action)

Returns a new CompletionStage that, when either this or the
other given stage complete normally, executes the given action.

See the

CompletionStage

documentation for rules
covering exceptional completion.

runAfterEitherAsync

```java
CompletionStage
<
Void
> runAfterEitherAsync​(
CompletionStage
<?> other,

Runnable
action)
```

Returns a new CompletionStage that, when either this or the
other given stage complete normally, executes the given action
using this stage's default asynchronous execution facility.

See the

CompletionStage

documentation for rules
covering exceptional completion.

**Parameters:** other

- the other CompletionStage
**Parameters:** action

- the action to perform before completing the
returned CompletionStage
**Returns:** the new CompletionStage

---

#### runAfterEitherAsync

CompletionStage

<

Void

> runAfterEitherAsync​(

CompletionStage

<?> other,

Runnable

action)

Returns a new CompletionStage that, when either this or the
other given stage complete normally, executes the given action
using this stage's default asynchronous execution facility.

See the

CompletionStage

documentation for rules
covering exceptional completion.

runAfterEitherAsync

```java
CompletionStage
<
Void
> runAfterEitherAsync​(
CompletionStage
<?> other,

Runnable
action,

Executor
executor)
```

Returns a new CompletionStage that, when either this or the
other given stage complete normally, executes the given action
using the supplied executor.

See the

CompletionStage

documentation for rules
covering exceptional completion.

**Parameters:** other

- the other CompletionStage
**Parameters:** action

- the action to perform before completing the
returned CompletionStage
**Parameters:** executor

- the executor to use for asynchronous execution
**Returns:** the new CompletionStage

---

#### runAfterEitherAsync

CompletionStage

<

Void

> runAfterEitherAsync​(

CompletionStage

<?> other,

Runnable

action,

Executor

executor)

Returns a new CompletionStage that, when either this or the
other given stage complete normally, executes the given action
using the supplied executor.

See the

CompletionStage

documentation for rules
covering exceptional completion.

thenCompose

```java
<U>
CompletionStage
<U> thenCompose​(
Function
<? super
T
,​? extends
CompletionStage
<U>> fn)
```

Returns a new CompletionStage that is completed with the same
value as the CompletionStage returned by the given function.

When this stage completes normally, the given function is
invoked with this stage's result as the argument, returning
another CompletionStage. When that stage completes normally,
the CompletionStage returned by this method is completed with
the same value.

To ensure progress, the supplied function must arrange
eventual completion of its result.

This method is analogous to

Optional.flatMap

and

Stream.flatMap

.

See the

CompletionStage

documentation for rules
covering exceptional completion.

**Type Parameters:** U

- the type of the returned CompletionStage's result
**Parameters:** fn

- the function to use to compute another CompletionStage
**Returns:** the new CompletionStage

---

#### thenCompose

<U>

CompletionStage

<U> thenCompose​(

Function

<? super

T

,​? extends

CompletionStage

<U>> fn)

Returns a new CompletionStage that is completed with the same
value as the CompletionStage returned by the given function.

When this stage completes normally, the given function is
invoked with this stage's result as the argument, returning
another CompletionStage. When that stage completes normally,
the CompletionStage returned by this method is completed with
the same value.

To ensure progress, the supplied function must arrange
eventual completion of its result.

This method is analogous to

Optional.flatMap

and

Stream.flatMap

.

See the

CompletionStage

documentation for rules
covering exceptional completion.

When this stage completes normally, the given function is
invoked with this stage's result as the argument, returning
another CompletionStage. When that stage completes normally,
the CompletionStage returned by this method is completed with
the same value.

To ensure progress, the supplied function must arrange
eventual completion of its result.

This method is analogous to

Optional.flatMap

and

Stream.flatMap

.

See the

CompletionStage

documentation for rules
covering exceptional completion.

To ensure progress, the supplied function must arrange
eventual completion of its result.

This method is analogous to

Optional.flatMap

and

Stream.flatMap

.

See the

CompletionStage

documentation for rules
covering exceptional completion.

This method is analogous to

Optional.flatMap

and

Stream.flatMap

.

See the

CompletionStage

documentation for rules
covering exceptional completion.

See the

CompletionStage

documentation for rules
covering exceptional completion.

thenComposeAsync

```java
<U>
CompletionStage
<U> thenComposeAsync​(
Function
<? super
T
,​? extends
CompletionStage
<U>> fn)
```

Returns a new CompletionStage that is completed with the same
value as the CompletionStage returned by the given function,
executed using this stage's default asynchronous execution
facility.

When this stage completes normally, the given function is
invoked with this stage's result as the argument, returning
another CompletionStage. When that stage completes normally,
the CompletionStage returned by this method is completed with
the same value.

To ensure progress, the supplied function must arrange
eventual completion of its result.

See the

CompletionStage

documentation for rules
covering exceptional completion.

**Type Parameters:** U

- the type of the returned CompletionStage's result
**Parameters:** fn

- the function to use to compute another CompletionStage
**Returns:** the new CompletionStage

---

#### thenComposeAsync

<U>

CompletionStage

<U> thenComposeAsync​(

Function

<? super

T

,​? extends

CompletionStage

<U>> fn)

Returns a new CompletionStage that is completed with the same
value as the CompletionStage returned by the given function,
executed using this stage's default asynchronous execution
facility.

When this stage completes normally, the given function is
invoked with this stage's result as the argument, returning
another CompletionStage. When that stage completes normally,
the CompletionStage returned by this method is completed with
the same value.

To ensure progress, the supplied function must arrange
eventual completion of its result.

See the

CompletionStage

documentation for rules
covering exceptional completion.

When this stage completes normally, the given function is
invoked with this stage's result as the argument, returning
another CompletionStage. When that stage completes normally,
the CompletionStage returned by this method is completed with
the same value.

To ensure progress, the supplied function must arrange
eventual completion of its result.

See the

CompletionStage

documentation for rules
covering exceptional completion.

To ensure progress, the supplied function must arrange
eventual completion of its result.

See the

CompletionStage

documentation for rules
covering exceptional completion.

See the

CompletionStage

documentation for rules
covering exceptional completion.

thenComposeAsync

```java
<U>
CompletionStage
<U> thenComposeAsync​(
Function
<? super
T
,​? extends
CompletionStage
<U>> fn,

Executor
executor)
```

Returns a new CompletionStage that is completed with the same
value as the CompletionStage returned by the given function,
executed using the supplied Executor.

When this stage completes normally, the given function is
invoked with this stage's result as the argument, returning
another CompletionStage. When that stage completes normally,
the CompletionStage returned by this method is completed with
the same value.

To ensure progress, the supplied function must arrange
eventual completion of its result.

See the

CompletionStage

documentation for rules
covering exceptional completion.

**Type Parameters:** U

- the type of the returned CompletionStage's result
**Parameters:** fn

- the function to use to compute another CompletionStage
**Parameters:** executor

- the executor to use for asynchronous execution
**Returns:** the new CompletionStage

---

#### thenComposeAsync

<U>

CompletionStage

<U> thenComposeAsync​(

Function

<? super

T

,​? extends

CompletionStage

<U>> fn,

Executor

executor)

Returns a new CompletionStage that is completed with the same
value as the CompletionStage returned by the given function,
executed using the supplied Executor.

When this stage completes normally, the given function is
invoked with this stage's result as the argument, returning
another CompletionStage. When that stage completes normally,
the CompletionStage returned by this method is completed with
the same value.

To ensure progress, the supplied function must arrange
eventual completion of its result.

See the

CompletionStage

documentation for rules
covering exceptional completion.

When this stage completes normally, the given function is
invoked with this stage's result as the argument, returning
another CompletionStage. When that stage completes normally,
the CompletionStage returned by this method is completed with
the same value.

To ensure progress, the supplied function must arrange
eventual completion of its result.

See the

CompletionStage

documentation for rules
covering exceptional completion.

To ensure progress, the supplied function must arrange
eventual completion of its result.

See the

CompletionStage

documentation for rules
covering exceptional completion.

See the

CompletionStage

documentation for rules
covering exceptional completion.

handle

```java
<U>
CompletionStage
<U> handle​(
BiFunction
<? super
T
,​
Throwable
,​? extends U> fn)
```

Returns a new CompletionStage that, when this stage completes
either normally or exceptionally, is executed with this stage's
result and exception as arguments to the supplied function.

When this stage is complete, the given function is invoked
with the result (or

null

if none) and the exception (or

null

if none) of this stage as arguments, and the
function's result is used to complete the returned stage.

**Type Parameters:** U

- the function's return type
**Parameters:** fn

- the function to use to compute the value of the
returned CompletionStage
**Returns:** the new CompletionStage

---

#### handle

<U>

CompletionStage

<U> handle​(

BiFunction

<? super

T

,​

Throwable

,​? extends U> fn)

Returns a new CompletionStage that, when this stage completes
either normally or exceptionally, is executed with this stage's
result and exception as arguments to the supplied function.

When this stage is complete, the given function is invoked
with the result (or

null

if none) and the exception (or

null

if none) of this stage as arguments, and the
function's result is used to complete the returned stage.

When this stage is complete, the given function is invoked
with the result (or

null

if none) and the exception (or

null

if none) of this stage as arguments, and the
function's result is used to complete the returned stage.

handleAsync

```java
<U>
CompletionStage
<U> handleAsync​(
BiFunction
<? super
T
,​
Throwable
,​? extends U> fn)
```

Returns a new CompletionStage that, when this stage completes
either normally or exceptionally, is executed using this stage's
default asynchronous execution facility, with this stage's
result and exception as arguments to the supplied function.

When this stage is complete, the given function is invoked
with the result (or

null

if none) and the exception (or

null

if none) of this stage as arguments, and the
function's result is used to complete the returned stage.

**Type Parameters:** U

- the function's return type
**Parameters:** fn

- the function to use to compute the value of the
returned CompletionStage
**Returns:** the new CompletionStage

---

#### handleAsync

<U>

CompletionStage

<U> handleAsync​(

BiFunction

<? super

T

,​

Throwable

,​? extends U> fn)

Returns a new CompletionStage that, when this stage completes
either normally or exceptionally, is executed using this stage's
default asynchronous execution facility, with this stage's
result and exception as arguments to the supplied function.

When this stage is complete, the given function is invoked
with the result (or

null

if none) and the exception (or

null

if none) of this stage as arguments, and the
function's result is used to complete the returned stage.

When this stage is complete, the given function is invoked
with the result (or

null

if none) and the exception (or

null

if none) of this stage as arguments, and the
function's result is used to complete the returned stage.

handleAsync

```java
<U>
CompletionStage
<U> handleAsync​(
BiFunction
<? super
T
,​
Throwable
,​? extends U> fn,

Executor
executor)
```

Returns a new CompletionStage that, when this stage completes
either normally or exceptionally, is executed using the
supplied executor, with this stage's result and exception as
arguments to the supplied function.

When this stage is complete, the given function is invoked
with the result (or

null

if none) and the exception (or

null

if none) of this stage as arguments, and the
function's result is used to complete the returned stage.

**Type Parameters:** U

- the function's return type
**Parameters:** fn

- the function to use to compute the value of the
returned CompletionStage
**Parameters:** executor

- the executor to use for asynchronous execution
**Returns:** the new CompletionStage

---

#### handleAsync

<U>

CompletionStage

<U> handleAsync​(

BiFunction

<? super

T

,​

Throwable

,​? extends U> fn,

Executor

executor)

Returns a new CompletionStage that, when this stage completes
either normally or exceptionally, is executed using the
supplied executor, with this stage's result and exception as
arguments to the supplied function.

When this stage is complete, the given function is invoked
with the result (or

null

if none) and the exception (or

null

if none) of this stage as arguments, and the
function's result is used to complete the returned stage.

When this stage is complete, the given function is invoked
with the result (or

null

if none) and the exception (or

null

if none) of this stage as arguments, and the
function's result is used to complete the returned stage.

whenComplete

```java
CompletionStage
<
T
> whenComplete​(
BiConsumer
<? super
T
,​? super
Throwable
> action)
```

Returns a new CompletionStage with the same result or exception as
this stage, that executes the given action when this stage completes.

When this stage is complete, the given action is invoked
with the result (or

null

if none) and the exception (or

null

if none) of this stage as arguments. The returned
stage is completed when the action returns.

Unlike method

handle

,
this method is not designed to translate completion outcomes,
so the supplied action should not throw an exception. However,
if it does, the following rules apply: if this stage completed
normally but the supplied action throws an exception, then the
returned stage completes exceptionally with the supplied
action's exception. Or, if this stage completed exceptionally
and the supplied action throws an exception, then the returned
stage completes exceptionally with this stage's exception.

**Parameters:** action

- the action to perform
**Returns:** the new CompletionStage

---

#### whenComplete

CompletionStage

<

T

> whenComplete​(

BiConsumer

<? super

T

,​? super

Throwable

> action)

Returns a new CompletionStage with the same result or exception as
this stage, that executes the given action when this stage completes.

When this stage is complete, the given action is invoked
with the result (or

null

if none) and the exception (or

null

if none) of this stage as arguments. The returned
stage is completed when the action returns.

Unlike method

handle

,
this method is not designed to translate completion outcomes,
so the supplied action should not throw an exception. However,
if it does, the following rules apply: if this stage completed
normally but the supplied action throws an exception, then the
returned stage completes exceptionally with the supplied
action's exception. Or, if this stage completed exceptionally
and the supplied action throws an exception, then the returned
stage completes exceptionally with this stage's exception.

When this stage is complete, the given action is invoked
with the result (or

null

if none) and the exception (or

null

if none) of this stage as arguments. The returned
stage is completed when the action returns.

Unlike method

handle

,
this method is not designed to translate completion outcomes,
so the supplied action should not throw an exception. However,
if it does, the following rules apply: if this stage completed
normally but the supplied action throws an exception, then the
returned stage completes exceptionally with the supplied
action's exception. Or, if this stage completed exceptionally
and the supplied action throws an exception, then the returned
stage completes exceptionally with this stage's exception.

Unlike method

handle

,
this method is not designed to translate completion outcomes,
so the supplied action should not throw an exception. However,
if it does, the following rules apply: if this stage completed
normally but the supplied action throws an exception, then the
returned stage completes exceptionally with the supplied
action's exception. Or, if this stage completed exceptionally
and the supplied action throws an exception, then the returned
stage completes exceptionally with this stage's exception.

whenCompleteAsync

```java
CompletionStage
<
T
> whenCompleteAsync​(
BiConsumer
<? super
T
,​? super
Throwable
> action)
```

Returns a new CompletionStage with the same result or exception as
this stage, that executes the given action using this stage's
default asynchronous execution facility when this stage completes.

When this stage is complete, the given action is invoked with the
result (or

null

if none) and the exception (or

null

if none) of this stage as arguments. The returned stage is completed
when the action returns.

Unlike method

handleAsync

,
this method is not designed to translate completion outcomes,
so the supplied action should not throw an exception. However,
if it does, the following rules apply: If this stage completed
normally but the supplied action throws an exception, then the
returned stage completes exceptionally with the supplied
action's exception. Or, if this stage completed exceptionally
and the supplied action throws an exception, then the returned
stage completes exceptionally with this stage's exception.

**Parameters:** action

- the action to perform
**Returns:** the new CompletionStage

---

#### whenCompleteAsync

CompletionStage

<

T

> whenCompleteAsync​(

BiConsumer

<? super

T

,​? super

Throwable

> action)

Returns a new CompletionStage with the same result or exception as
this stage, that executes the given action using this stage's
default asynchronous execution facility when this stage completes.

When this stage is complete, the given action is invoked with the
result (or

null

if none) and the exception (or

null

if none) of this stage as arguments. The returned stage is completed
when the action returns.

Unlike method

handleAsync

,
this method is not designed to translate completion outcomes,
so the supplied action should not throw an exception. However,
if it does, the following rules apply: If this stage completed
normally but the supplied action throws an exception, then the
returned stage completes exceptionally with the supplied
action's exception. Or, if this stage completed exceptionally
and the supplied action throws an exception, then the returned
stage completes exceptionally with this stage's exception.

When this stage is complete, the given action is invoked with the
result (or

null

if none) and the exception (or

null

if none) of this stage as arguments. The returned stage is completed
when the action returns.

Unlike method

handleAsync

,
this method is not designed to translate completion outcomes,
so the supplied action should not throw an exception. However,
if it does, the following rules apply: If this stage completed
normally but the supplied action throws an exception, then the
returned stage completes exceptionally with the supplied
action's exception. Or, if this stage completed exceptionally
and the supplied action throws an exception, then the returned
stage completes exceptionally with this stage's exception.

Unlike method

handleAsync

,
this method is not designed to translate completion outcomes,
so the supplied action should not throw an exception. However,
if it does, the following rules apply: If this stage completed
normally but the supplied action throws an exception, then the
returned stage completes exceptionally with the supplied
action's exception. Or, if this stage completed exceptionally
and the supplied action throws an exception, then the returned
stage completes exceptionally with this stage's exception.

whenCompleteAsync

```java
CompletionStage
<
T
> whenCompleteAsync​(
BiConsumer
<? super
T
,​? super
Throwable
> action,

Executor
executor)
```

Returns a new CompletionStage with the same result or exception as
this stage, that executes the given action using the supplied
Executor when this stage completes.

When this stage is complete, the given action is invoked with the
result (or

null

if none) and the exception (or

null

if none) of this stage as arguments. The returned stage is completed
when the action returns.

Unlike method

handleAsync

,
this method is not designed to translate completion outcomes,
so the supplied action should not throw an exception. However,
if it does, the following rules apply: If this stage completed
normally but the supplied action throws an exception, then the
returned stage completes exceptionally with the supplied
action's exception. Or, if this stage completed exceptionally
and the supplied action throws an exception, then the returned
stage completes exceptionally with this stage's exception.

**Parameters:** action

- the action to perform
**Parameters:** executor

- the executor to use for asynchronous execution
**Returns:** the new CompletionStage

---

#### whenCompleteAsync

CompletionStage

<

T

> whenCompleteAsync​(

BiConsumer

<? super

T

,​? super

Throwable

> action,

Executor

executor)

Returns a new CompletionStage with the same result or exception as
this stage, that executes the given action using the supplied
Executor when this stage completes.

When this stage is complete, the given action is invoked with the
result (or

null

if none) and the exception (or

null

if none) of this stage as arguments. The returned stage is completed
when the action returns.

Unlike method

handleAsync

,
this method is not designed to translate completion outcomes,
so the supplied action should not throw an exception. However,
if it does, the following rules apply: If this stage completed
normally but the supplied action throws an exception, then the
returned stage completes exceptionally with the supplied
action's exception. Or, if this stage completed exceptionally
and the supplied action throws an exception, then the returned
stage completes exceptionally with this stage's exception.

When this stage is complete, the given action is invoked with the
result (or

null

if none) and the exception (or

null

if none) of this stage as arguments. The returned stage is completed
when the action returns.

Unlike method

handleAsync

,
this method is not designed to translate completion outcomes,
so the supplied action should not throw an exception. However,
if it does, the following rules apply: If this stage completed
normally but the supplied action throws an exception, then the
returned stage completes exceptionally with the supplied
action's exception. Or, if this stage completed exceptionally
and the supplied action throws an exception, then the returned
stage completes exceptionally with this stage's exception.

Unlike method

handleAsync

,
this method is not designed to translate completion outcomes,
so the supplied action should not throw an exception. However,
if it does, the following rules apply: If this stage completed
normally but the supplied action throws an exception, then the
returned stage completes exceptionally with the supplied
action's exception. Or, if this stage completed exceptionally
and the supplied action throws an exception, then the returned
stage completes exceptionally with this stage's exception.

exceptionally

```java
CompletionStage
<
T
> exceptionally​(
Function
<
Throwable
,​? extends
T
> fn)
```

Returns a new CompletionStage that, when this stage completes
exceptionally, is executed with this stage's exception as the
argument to the supplied function. Otherwise, if this stage
completes normally, then the returned stage also completes
normally with the same value.

**Parameters:** fn

- the function to use to compute the value of the
returned CompletionStage if this CompletionStage completed
exceptionally
**Returns:** the new CompletionStage

---

#### exceptionally

CompletionStage

<

T

> exceptionally​(

Function

<

Throwable

,​? extends

T

> fn)

Returns a new CompletionStage that, when this stage completes
exceptionally, is executed with this stage's exception as the
argument to the supplied function. Otherwise, if this stage
completes normally, then the returned stage also completes
normally with the same value.

toCompletableFuture

```java
CompletableFuture
<
T
> toCompletableFuture()
```

Returns a

CompletableFuture

maintaining the same
completion properties as this stage. If this stage is already a
CompletableFuture, this method may return this stage itself.
Otherwise, invocation of this method may be equivalent in
effect to

thenApply(x -> x)

, but returning an instance
of type

CompletableFuture

.

**Returns:** the CompletableFuture

---

#### toCompletableFuture

CompletableFuture

<

T

> toCompletableFuture()

Returns a

CompletableFuture

maintaining the same
completion properties as this stage. If this stage is already a
CompletableFuture, this method may return this stage itself.
Otherwise, invocation of this method may be equivalent in
effect to

thenApply(x -> x)

, but returning an instance
of type

CompletableFuture

.

---

