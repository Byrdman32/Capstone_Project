export function toCapitalCase(input: string): string {
    return input
        .split(' ')
        .map(word => word.charAt(0).toUpperCase() + word.slice(1).toLowerCase())
        .map(word => (word === 'Id' ? 'ID' : word))
        .join(' ');
}

export function removeUnderscores(input: string): string {
    return input.replace(/_/g, ' '); // Replace underscores with spaces
}
