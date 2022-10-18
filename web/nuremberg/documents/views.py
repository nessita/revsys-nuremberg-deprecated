from django.shortcuts import render
from django.views.generic import View

from .models import Document, author_metadata


class Show(View):
    template_name = 'documents/show.html'

    def get(self, request, document_id, *args, **kwargs):
        document = (
            Document.objects.prefetch_related('images')
            .select_related('language')
            .select_related('source')
            .get(id=document_id)
        )

        return render(
            request,
            self.template_name,
            {'document': document, 'query': request.GET.get('q')},
        )


def author_details(request, author_name):
    # XXX: Using the author name as author key could be flaky. Though currently
    # author names are reasonable "unique", we can't guarantee this condition.
    # But, in order to obtain an author ID, we should change the document
    # search indexes so they also store author ID in addition to author name,
    # and then return both in the search response.
    # In that case, the author query would be:
    # get_object_or_404(DocumentPersonalAuthor, id=author_id)
    metadata, image = author_metadata(author_name)
    context = {'author': author_name, 'image': image, 'metadata': metadata}
    return render(request, 'documents/author.html', context)
