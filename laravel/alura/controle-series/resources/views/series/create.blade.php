<x-layout title='Nova Serie'>
    <form action='/series' method='post'>
        @csrf
        <div class="mb-3">
        <label class="form-label" for="nome">Nome:</label>
        <input type="text" id="nome" name="nome" class="form-control">
        </div>
        <button type="submit" class="btn btn-primary">Adicionar</button>
    </form>
</x-layout>
